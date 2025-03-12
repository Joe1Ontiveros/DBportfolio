import sys
import mysql.connector
from datetime import datetime

class MySQLConnector:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                connection_timeout=5
            )
            self.cursor = self.connection.cursor()
            return True
        except mysql.connector.Error as err:
            print(f"Connection error: {err}")
            return False

    def reconnect(self):
        if self.connection and self.connection.is_connected():
            return True
        return self.connect()

    def add_user(self, name, email, phone_number):
        try:
            self.cursor.execute("SELECT email FROM USER WHERE email = %s", (email,))
            if self.cursor.fetchone():
                return None  # Duplicate email
            
            query = "INSERT INTO USER (name, email, phone_number) VALUES (%s, %s, %s)"
            self.cursor.execute(query, (name, email, phone_number))
            self.connection.commit()
            return self.cursor.lastrowid
        except mysql.connector.Error as err:
            print(f"User error: {err}")
            return None

    # Transaction-enabled methods
    def create_request(self, user_id, submitted_date, foundmethod):
        try:
            query = """INSERT INTO REQUEST (user_id, submitted_date, foundmethod)
                     VALUES (%s, %s, %s)"""
            self.cursor.execute(query, (user_id, submitted_date, foundmethod))
            self.connection.commit()
            return self.cursor.lastrowid
        except mysql.connector.Error as err:
            print(f"Request error: {err}")
            return None

    def create_specific_request(self, req_type, request_id, **kwargs):
        try:
            table_map = {
                'Programming': ('request_id', 'program_language', 'due_date', 'project_description'),
                'Consulting': ('request_id', 'due_date', 'project_desc', 'area_of_focus', 'company_career'),
                'Game Development': ('request_id', 'due_date', 'game_category', 'project_descript'),
                'Tutoring': ('request_id', 'school_year', 'due_date', 'language_choice', 'description')
            }
            
            columns = table_map[req_type]
            values = [request_id] + [kwargs[col] for col in columns[1:]]
            placeholders = ', '.join(['%s'] * len(values))
            columns_str = ', '.join(columns)
            
            query = f"INSERT INTO {req_type}REQ ({columns_str}) VALUES ({placeholders})"
            self.cursor.execute(query, values)
            self.connection.commit()
            return True
        except mysql.connector.Error as err:
            print(f"{req_type} error: {err}")
            return False

class App:
    def __init__(self):
        self.db_connector = MySQLConnector('localhost', 'root', '1523', 'FREELANCE_DB_4')
        self.db = None
        self.start_db_connection()

    def start_db_connection(self):
        if self.db_connector.connect():
            self.db = self.db_connector
            print('Database connection established')
        else:
            print('Database connection failed')
            sys.exit(1)

    def get_user_input(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        phone = input("Enter your phone number: ")
        return name, email, phone

    def get_request_input(self):
        req_type = input("Enter request type (Programming, Consulting, Game Development, Tutoring): ")
        due_date = input("Enter due date (YYYY-MM-DD): ")
        desc = input("Enter project description: ")

        additional_data = {}
        if req_type == 'Programming':
            additional_data['program_language'] = input("Enter programming language: ")
            additional_data['project_description'] = desc
        elif req_type == 'Consulting':
            additional_data['area_of_focus'] = input("Enter focus area: ")
            additional_data['company_career'] = input("Enter industry: ")
            additional_data['project_desc'] = desc
        elif req_type == 'Game Development':
            additional_data['game_category'] = input("Enter game genre: ")
            additional_data['project_descript'] = desc
        elif req_type == 'Tutoring':
            additional_data['school_year'] = input("Enter education level: ")
            additional_data['language_choice'] = input("Enter subject: ")
            additional_data['description'] = desc

        return req_type, due_date, additional_data

    def process_submission(self):
        if not self.db or not self.db.reconnect():
            print('Database connection lost')
            return

        try:
            self.db.connection.start_transaction()
            
            # Create User
            name, email, phone = self.get_user_input()
            user_id = self.db.add_user(name, email, phone)
            if not user_id:
                raise Exception("Failed to create user - possible duplicate email")
            
            # Create Base Request
            req_type, due_date, req_data = self.get_request_input()
            request_id = self.db.create_request(user_id, datetime.now().strftime('%Y-%m-%d'), 'Terminal')
            if not request_id:
                raise Exception("Failed to create base request")
            print("generated base request with id : ",request_id)
            # Create Specific Request
            success = self.db.create_specific_request(req_type, request_id, **req_data)
            
            if success:
                self.db.connection.commit()
                print('Request submitted successfully!')
            else:
                raise Exception("Failed to create specific request")
                
        except Exception as e:
            self.db.connection.rollback()
            print(f"Submission failed: {str(e)}")

if __name__ == '__main__':
    app = App()
    while True:
        app.process_submission()
        cont = input("Do you want to submit another request? (yes/no): ")
        if cont.lower() != 'yes':
            break
    print("Exiting application.")
