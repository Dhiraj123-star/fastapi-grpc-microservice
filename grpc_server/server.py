from concurrent import futures
import grpc
import sys
import os
import sqlite3
from faker import Faker

# Fix import path to find proto generated files
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "proto"))

import user_pb2
import user_pb2_grpc

# Initialize Faker
faker = Faker()

# Database setup
DB_PATH = os.path.join(os.path.dirname(__file__), "users.db")
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE
    )
""")
conn.commit()

# Insert a fake user if not exists
def insert_fake_user():
    name = faker.name()
    email = faker.email()
    cursor.execute("INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    return cursor.lastrowid, name, email

# gRPC Service Implementation
class UserService(user_pb2_grpc.UserServiceServicer):
    def GetUser(self, request, context):
        try:
            user_id = request.id  # ✅ This is correct
            print("USer id type ---> ",type(user_id))
            cursor.execute("SELECT id, name, email FROM users WHERE id = ?", (user_id,))
            row = cursor.fetchone()
            if row:
                return user_pb2.UserResponse(id=row[0], name=row[1], email=row[2])
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("User not found")
            return user_pb2.UserResponse()
        except Exception as e:
            context.set_code(grpc.StatusCode.UNKNOWN)
            context.set_details(str(e))
            return user_pb2.UserResponse()



    def AddFakeUser(self, request, context):
        user_id, name, email = insert_fake_user()
        return user_pb2.UserResponse(id=user_id, name=name, email=email)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:50051')
    print("gRPC Server running on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
