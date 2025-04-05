from swagger_server import models
import sys
from flask import abort, jsonify
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


def get_analytic_data():  # noqa: E501
    """Get analytics data

     # noqa: E501


    :rtype: InlineResponse200
    """
    return 'do some magic!'


def get_analytic_relation():  # noqa: E501
    """Get heart rate and traffic ratio relation

     # noqa: E501


    :rtype: List[AnalyticRelation]
    """
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT heartrate, currentSpeed/freeFlowSpeed AS ratio
            FROM HeartOnTheRoad
            """)
    result = [models.AnalyticRelation(heartrate,ratio) 
              for heartrate,ratio in cs.fetchall()]
    return result


def get_heart_rate_trip(trip_id):  # noqa: E501
    """Get heart rate data for a trip

     # noqa: E501

    :param trip_id: 
    :type trip_id: float

    :rtype: List[HeartRateTrip]
    """
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT timestamp, heartrate
            FROM HeartOnTheRoad 
            WHERE trip_id = %s
            """, [trip_id])
    result = [models.HeartRateTrip(timestamp, heartrate)
              for timestamp, heartrate in cs.fetchall()]
    return result


def get_location_trip(trip_id):  # noqa: E501
    """Get location data for a trip

     # noqa: E501

    :param trip_id: 
    :type trip_id: float

    :rtype: List[LocationTrip]
    """
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT latitude,longitude,currentSpeed,freeFlowSpeed 
            FROM HeartOnTheRoad 
            WHERE trip_id = %s
            """, [trip_id])
    result = [models.LocationTrip(latitude, longitude, currentSpeed, freeFlowSpeed)
              for latitude, longitude, currentSpeed, freeFlowSpeed in cs.fetchall()]
    return result


def get_number_of_trips():  # noqa: E501
    """Get number of trips

    :rtype: NumberOfTrip
    """
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute(
            "SELECT COUNT(DISTINCT trip_id) AS number_of_trip FROM HeartOnTheRoad")
        result = cs.fetchone()
        print(result, 'result')
        if result:
            number_of_trip = result[0]
            return models.NumberOfTrip(number_of_trip=number_of_trip)
        else:
            abort(404)


def get_trip_details(trip_id):  # noqa: E501
    """Get trip details

     # noqa: E501

    :param trip_id: 
    :type trip_id: float

    :rtype: TripDetails
    """
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
            return None  # No data found

        total, trafficjam, normal, start_time, duration, min_heartrate, max_heartrate, average_heartrate = row

        return models.TripDetails(
            record=models.Record(total=total, trafficjam=trafficjam, normal=normal),
            start_time=start_time,
            duration=duration, # minutes
            min_heartrate=min_heartrate,
            max_heartrate=max_heartrate,
            average_heartrate=average_heartrate
        )
