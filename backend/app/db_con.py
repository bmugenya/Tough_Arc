import psycopg2

url = "dbname='shiriki' user='postgres' host='localhost' port=5432 password='Qw12Er34'"


class database_setup(object):

    def __init__(self):
        self.conn = psycopg2.connect(url)
        self.cursor = self.conn.cursor()

    def destroy_tables(self):
        self.cursor.execute("""DROP TABLE IF EXISTS User CASCADE;""")
        self.cursor.execute("""DROP TABLE IF EXISTS Share CASCADE;""")

        self.conn.commit()

    def create_tables(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Users (
            student_id VARCHAR(25) NOT NULL PRIMARY KEY,
            firstname VARCHAR(25) NOT NULL,
            lastname  VARCHAR(25) NOT NULL,
            email       VARCHAR(25)    NOT NULL,
            phonenumber  VARCHAR(50)    NOT NULL,
            password VARCHAR(255) NOT NULL,
            isAdmin   BOOLEAN NOT NULL
            );""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Share (
            book_id SERIAL PRIMARY KEY,
            postedOn timestamp default current_timestamp,
            title VARCHAR(25) NOT NULL,
            lecture   VARCHAR(50)    NOT NULL,
            condition   VARCHAR(25)   NOT NULL,
            comment    VARCHAR(25)

            );""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Orders (
            book_id INT ,
            postedOn timestamp default current_timestamp,
            ostedBy VARCHAR(25) ,
            title VARCHAR(25)    NOT NULL,
            lecture   VARCHAR(50)    NOT NULL,
            condition   VARCHAR(25)   NOT NULL
            );""")

        self.conn.commit()
