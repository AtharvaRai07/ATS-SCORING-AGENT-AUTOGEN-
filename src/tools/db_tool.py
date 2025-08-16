import json
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

class DBTool:
    ids = []
    DB_NAME = os.getenv("dbname")
    USER = os.getenv("user")
    PASSWORD = os.getenv("password")
    HOST = os.getenv("host")
    PORT = os.getenv("port")

    @staticmethod
    def connect_to_superbase(db_name, user, password, host, port):
        """
        Establish a connection to a PostgreSQL database.

        Args:
            db_name (str): The name of the database.
            user (str): The database user.
            password (str): The user's password.
            host (str): The database host address.
            port (str): The database port.

        Returns:
            psycopg2.extensions.connection | None: A database connection object or None if failed.
        """
        connection = None
        try:
            connection = psycopg2.connect(
                database=db_name,
                user=user,
                password=password,
                host=host,
                port=port
            )
            print(f"[INFO] Connected to PostgreSQL DB: {db_name}")
            return connection
        except Exception as e:
            print(f"[ERROR] Failed to connect to DB {db_name}: {e}")
            return None

    @staticmethod
    def execute_query(connection, query: str, params: tuple | None = None):
        """
        Execute a SQL query with optional parameters.

        Args:
            connection: Active database connection object.
            query (str): SQL query string.
            params (tuple | None): Parameters for the query.

        Returns:
            Any: Query result depending on the operation type.
        """
        cursor = None
        try:
            cursor = connection.cursor()
            cursor.execute(query, params)

            if query.strip().upper().startswith(('CREATE', 'INSERT', 'UPDATE', 'DELETE')):
                connection.commit()
                if "RETURNING" in query.upper():
                    return cursor.fetchone()[0]
                else:
                    return cursor.rowcount
            else:
                return cursor.fetchall()
        except Exception as e:
            print(f"[ERROR] Query execution failed: {e}")
            if connection:
                connection.rollback()
            return None
        finally:
            if cursor:
                cursor.close()

    @staticmethod
    def save_resume_to_db(conn, parsed_string):
        query = """
        INSERT INTO resumes (file_type,parsed_json)
        VALUES (%s, %s)
        RETURNING id;
        """
        params = (
            parsed_string['file_type'],
            json.dumps(parsed_string),
        )
        try:
            if conn:
                resume_id = DBTool().execute_query(conn, query, params)
                DBTool.ids.append(resume_id)
                return resume_id
            else:
                raise Exception("Connection to online database is not established")
        except Exception as e:
            raise Exception(f"Failed to save resume to database: {str(e)}")


    @staticmethod
    def save_jobs_to_db(jobs, conn, resume_id):
        query = """
        INSERT INTO job_descriptions (resume_id, parsed_json)
        VALUES (%s, %s)
        RETURNING id;
        """
        if conn:
            params = (resume_id, json.dumps(jobs))
            result = DBTool.execute_query(conn, query, params)
            return result
        else:
            raise Exception("No database connection.")

    @staticmethod
    def send_ats_score(ats_score, conn, resume_id):
        query = """
        INSERT INTO scores (ats_score, resume_id)
        VALUES (%s, %s)
        """
        if conn:
            params = (json.dumps(ats_score), resume_id)
            return DBTool.execute_query(conn, query, params)
        else:
            raise Exception("No database connection.")

    @staticmethod
    def send_improvement_to_score(result, conn, resume_id):
        query = """
        UPDATE scores SET recommendations = %s WHERE resume_id = %s;
        """
        if conn:
            params = (json.dumps(result), resume_id)
            return DBTool.execute_query(conn, query, params)
        else:
            raise Exception("No database connection.")

    @staticmethod
    def get_resume_by_id(conn, resume_id):
        query = """
        SELECT parsed_json FROM resumes WHERE id = %s;
        """
        if conn:
            params = (resume_id,)
            result = DBTool.execute_query(conn, query, params)
            return result
        else:
            raise Exception("No database connection.")
        
    @staticmethod
    def get_job_by_id(conn, job_id):
        query = """
        SELECT parsed_json FROM job_descriptions WHERE id = %s;
        """
        if conn:
            params = (job_id,)
            result = DBTool.execute_query(conn, query, params)
            return result
        else:
            raise Exception("No database connection.")
    
    @staticmethod
    def get_ats_score_and_improvement_by_id(conn, resume_id):
        query = """
        SELECT ats_score, recommendations FROM scores WHERE resume_id = %s;
        """
        if conn:
            params = (resume_id,)
            result = DBTool.execute_query(conn, query, params)
            return result
        else:
            raise Exception("No database connection.")

