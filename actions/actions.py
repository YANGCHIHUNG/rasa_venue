# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pymysql


class QueryResourceType(Action):

    def name(self) -> Text:
        return "query_resource_type"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # conn = DbQueryMethods.create_connection(db_file="D://User//Rasa//edu_db//venueDB.db")
        db_settings = { "host": "140.83.85.111",
                        "port": 3306,
                        "user": "admin",
                        "password": "@050610AIoT",
                        "db": "test_database",
                        "charset": "utf8"}
        conn = pymysql.connect(**db_settings)

        try:
            with conn.cursor() as cursor:

                cursor.execute("select * from Stadium ORDER BY set_time")
                rows = cursor.fetchall()

                for row in rows:
                    result = f"The following is the information:\npeople flow:{row[1]}\ntemp:{row[2]}\nhumidity:{row[3]}\nair_quality:{row[4]}"
        except Exception as ex:
            print(ex)

        dispatcher.utter_message(text=str(result))

        return []

# class DbQueryMethods:
#     # def create_connection(db_file):
#     #     """ create a database connection to the SQLite database
#     #         specified by the db_file
#     #     :param db_file: database file
#     #     :return: Connection object or None
#     #     """
#     #     conn = None
#     #     try:
#     #         conn = sqlite3.connect(db_file)
#     #     except Error as e:
#     #         print(e)

#     #     return conn

#     def select_by_slot(conn, slot_value):

#         try:
#             with conn.cursor() as cursor:

#                 # command = "SELECT * FROM "+ test_table + ";"
#                 cursor.execute("SELECT * FROM "+ slot_value + ";")
#                 result = cursor.fetchone()
#                 return result
#         except Exception as ex:
#             return ex