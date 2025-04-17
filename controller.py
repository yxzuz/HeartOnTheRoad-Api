from swagger_server import models
import sys
from flask import abort
from werkzeug.exceptions import BadRequest
import pymysql
from dbutils.pooled_db import PooledDB
from config import OPENAPI_STUB_DIR, DB_HOST, DB_USER, DB_PASSWD, DB_NAME

sys.path.append(OPENAPI_STUB_DIR)

pool = PooledDB(creator=pymysql,
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWD,
                database=DB_NAME,
                maxconnections=1,
                blocking=True)


class HeartOnTheRoadAnalytics:
    class Analytic:
        @classmethod
        def get_analytic_data(cls):
            with pool.connection() as conn, conn.cursor() as cs:
                cs.execute("""
                    WITH record AS (
                        SELECT 
                            COUNT(*) AS total,  
                            COUNT(CASE WHEN isTrafficJam = 1 THEN 1 END) AS trafficjam,  
                            COUNT(CASE WHEN isTrafficJam = 0 THEN 1 END) AS normal,
                            COUNT(DISTINCT trip_id) AS trip
                        FROM HeartOnTheRoad
                    ),
                    tmp AS (
                        SELECT
                            TIMESTAMPDIFF(MINUTE, MIN(timeStamp), MAX(timeStamp)) AS duration,
                            trip_id
                        FROM HeartOnTheRoad
                        GROUP BY trip_id
                    ),
                    average_duration AS (
                        SELECT 
                            AVG(duration) AS avg_duration
                        FROM tmp
                    ),
                    heartrate AS (
                        SELECT 
                            AVG(heartrate) AS average,
                            AVG(CASE WHEN isTrafficJam = 1 THEN heartrate END) AS trafficjam,
                            AVG(CASE WHEN isTrafficJam = 0 THEN heartrate END) AS normal
                        FROM HeartOnTheRoad
                    ),
                    last_timestamp AS (
                        SELECT MAX(timeStamp) AS last_time_stamp
                        FROM HeartOnTheRoad
                    )
                    SELECT 
                        record.total, 
                        record.trafficjam, 
                        record.normal,
                        record.trip,
                        average_duration.avg_duration, 
                        heartrate.average, 
                        heartrate.trafficjam, 
                        heartrate.normal,
                        last_timestamp.last_time_stamp
                    FROM record, average_duration, heartrate, last_timestamp;
                """)
                row = cs.fetchone()
            if not row:
                return None
            total, trafficjam, normal, trip, avg_duration, avg_heartrate, trafficjam_heartrate, normal_heartrate, last_time_stamp = row
            return models.AnalyticData(
                last_time_stamp=last_time_stamp,
                record={"total": total, "trafficjam": trafficjam,
                        "normal": normal, "trip": trip},
                average_duration=avg_duration,
                heartrate={"average": avg_heartrate,
                           "trafficjam": trafficjam_heartrate, "normal": normal_heartrate}
            )

        @classmethod
        def get_analytic_relation(cls):
            with pool.connection() as conn, conn.cursor() as cs:
                cs.execute("""
                    SELECT heartrate, currentSpeed/freeFlowSpeed AS ratio
                    FROM HeartOnTheRoad
                """)
                return [models.AnalyticRelation(heartrate, ratio) for heartrate, ratio in cs.fetchall()]

        @classmethod
        def get_number_of_trips(cls):
            with pool.connection() as conn, conn.cursor() as cs:
                cs.execute(
                    "SELECT COUNT(DISTINCT trip_id) AS number_of_trip FROM HeartOnTheRoad")
                result = cs.fetchone()
                if result:
                    return models.NumberOfTrip(number_of_trip=result[0])
                abort(404)

    class Trip:
        @classmethod
        def get_heart_rate_trip(cls, trip_id):
            if not isinstance(trip_id, (int, float)) or trip_id <= 0 or trip_id >= 29:
                raise BadRequest("Invalid trip_id: must be a positive number.")
            with pool.connection() as conn, conn.cursor() as cs:
                cs.execute("""
                    SELECT timestamp, heartrate
                    FROM HeartOnTheRoad 
                    WHERE trip_id = %s
                """, [trip_id])
                return [models.HeartRateTrip(timestamp, heartrate) for timestamp, heartrate in cs.fetchall()]

        @classmethod
        def get_location_trip(cls, trip_id):
            if not isinstance(trip_id, (int, float)) or trip_id <= 0 or trip_id >= 29:
                raise BadRequest("Invalid trip_id: must be a positive number.")
            with pool.connection() as conn, conn.cursor() as cs:
                cs.execute("""
                    SELECT latitude, longitude, currentSpeed, freeFlowSpeed 
                    FROM HeartOnTheRoad 
                    WHERE trip_id = %s
                """, [trip_id])
                return [models.LocationTrip(latitude, longitude, currentSpeed, freeFlowSpeed) for latitude, longitude, currentSpeed, freeFlowSpeed in cs.fetchall()]

        @classmethod
        def get_trip_details(cls, trip_id):
            if not isinstance(trip_id, (int, float)) or trip_id <= 0 or trip_id >= 29:
                raise BadRequest("Invalid trip_id: must be a positive number.")
            with pool.connection() as conn, conn.cursor() as cs:
                cs.execute("""
                    WITH filtered_trip_id AS (
                        SELECT * FROM HeartOnTheRoad WHERE trip_id = %s
                    ), 
                    record AS (
                        SELECT 
                            COUNT(*) AS total,  
                            COUNT(CASE WHEN isTrafficJam = 1 THEN 1 END) AS trafficjam,  
                            COUNT(CASE WHEN isTrafficJam = 0 THEN 1 END) AS normal  
                        FROM filtered_trip_id
                    ),
                    stats AS (
                        SELECT 
                            MIN(timeStamp) AS start_time,
                            TIMEDIFF(MAX(timeStamp), MIN(timeStamp)) AS duration, 
                            MIN(heartrate) AS min_heartrate,
                            MAX(heartrate) AS max_heartrate,
                            AVG(heartrate) AS average_heartrate
                        FROM filtered_trip_id
                    )
                    SELECT 
                        record.total, 
                        record.trafficjam, 
                        record.normal,
                        stats.start_time, 
                        stats.duration, 
                        stats.min_heartrate, 
                        stats.max_heartrate, 
                        stats.average_heartrate
                    FROM record, stats
                """, [trip_id])
                row = cs.fetchone()
                if not row:
                    return None
                total, trafficjam, normal, start_time, duration, min_heartrate, max_heartrate, average_heartrate = row
                return models.TripDetails(
                    record=models.Record(
                        total=total, trafficjam=trafficjam, normal=normal),
                    start_time=start_time,
                    duration=duration,
                    min_heartrate=min_heartrate,
                    max_heartrate=max_heartrate,
                    average_heartrate=average_heartrate
                )

    class Traffic:
        @classmethod
        def get_traffic_summary(cls, is_traffic_jam):
            with pool.connection() as conn, conn.cursor() as cs:
                cs.execute("""
                    WITH filtered_records AS (
                        SELECT * 
                        FROM HeartOnTheRoad 
                        WHERE isTrafficJam = %s
                    ),
                    trip_durations AS (
                        SELECT 
                            trip_id,
                            TIMESTAMPDIFF(MINUTE, MIN(timeStamp), MAX(timeStamp)) AS duration
                        FROM filtered_records
                        GROUP BY trip_id
                    ),
                    stats AS (
                        SELECT 
                            COUNT(*) AS total_records,
                            MIN(heartrate) AS min_heartrate,
                            MAX(heartrate) AS max_heartrate,
                            AVG(heartrate) AS average_heartrate,
                            AVG(currentSpeed) AS average_currentspeed,
                            AVG(currentTravelTime) AS average_travel_time
                        FROM filtered_records fr
                        JOIN trip_durations td ON fr.trip_id = td.trip_id
                    )
                    SELECT * FROM stats;
                """, [is_traffic_jam])
                row = cs.fetchone()
            if not row:
                return None
            total_records, min_heartrate, max_heartrate, average_heartrate, average_currentspeed, average_travel_time = row
            return models.TrafficSummary(
                number_of_records=total_records,
                min_heartrate=min_heartrate,
                max_heartrate=max_heartrate,
                average_heartrate=average_heartrate,
                average_speed=average_currentspeed,
                average_travel_time=average_travel_time
            )

        @classmethod
        def get_heartrate_by_traffic(cls, is_traffic_jam):
            with pool.connection() as conn, conn.cursor() as cs:
                cs.execute("""
                    SELECT timeStamp, heartrate FROM HeartOnTheRoad
                    WHERE isTrafficJam = %s
                """, [is_traffic_jam])
                return [models.HeartRateByTraffic(timeStamp, heartrate) for timeStamp, heartrate in cs.fetchall()]

        @classmethod
        def get_speed_by_traffic(cls, is_traffic_jam):
            with pool.connection() as conn, conn.cursor() as cs:
                cs.execute("""
                    SELECT timeStamp, currentSpeed FROM HeartOnTheRoad
                    WHERE isTrafficJam = %s
                """, [is_traffic_jam])
                return [models.SpeedByTraffic(timeStamp, currentSpeed) for timeStamp, currentSpeed in cs.fetchall()]
