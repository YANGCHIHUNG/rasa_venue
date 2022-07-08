# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_core_sdk import Action, Tracker
from rasa_core_sdk.executor import CollectingDispatcher
import pymysql


class QueryResourceType(Action):

    def name(self) -> Text:
        return "query_resource_type"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # conn = DbQueryMethods.create_connection(db_file="D://User//Rasa//edu_db//venueDB.db")
        db_settings = {
            "host": "127.0.0.1",
            "port": 3306,
            "user": "root",
            "password": "pisces900221",
            "db": "PeopleFlowDB",
            "charset": "utf8"
        }
        conn = pymysql.connect(**db_settings)

        slot_value = tracker.get_slot("resource_type")
        get_query_results = DbQueryMethods.select_by_slot(conn=conn, slot_value=slot_value)
        dispatcher.utter_message(text=str(get_query_results))

        return []

class DbQueryMethods:
    # def create_connection(db_file):
    #     """ create a database connection to the SQLite database
    #         specified by the db_file
    #     :param db_file: database file
    #     :return: Connection object or None
    #     """
    #     conn = None
    #     try:
    #         conn = sqlite3.connect(db_file)
    #     except Error as e:
    #         print(e)

    #     return conn

    def select_by_slot(conn, slot_value):

        try:
            with conn.cursor() as cursor:

                command = "SELECT * FROM "+ slot_value + ";"
                cursor.execute(command)
                result = cursor.fetchone()
                return result
        except Exception as ex:
            return ex