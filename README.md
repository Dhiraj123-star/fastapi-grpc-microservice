
---

# FastAPI + gRPC Microservice 🚀

## Overview

This project demonstrates a simple microservice architecture combining **FastAPI** for building HTTP APIs and **gRPC** for efficient, high-performance communication between services.

## Core Functionality

* **User Service via gRPC**
  A gRPC server exposes two RPC methods:

  * `GetUser`: Retrieves user details using a unique user ID.
  * `AddFakeUser`: Generates and stores a new fake user using the `Faker` library and returns the created user's details.

* **gRPC Client Integration**
  The FastAPI application includes a gRPC client that communicates with the gRPC server. It sends structured requests and receives user data in response, leveraging gRPC’s speed and strong typing.

* **FastAPI REST API Layer**
  Provides a user-friendly HTTP interface for clients:

  * `GET /users/{user_id}`: Fetches user details by ID.
  * `POST /users/add`: Creates a fake user and returns the new record.
    These endpoints internally invoke gRPC calls to retrieve or create users.

## Key Benefits

* Combines the simplicity of REST APIs with the efficiency of gRPC communication.
* Maintains a clean separation between external HTTP APIs and internal service communication.
* Enables modular, scalable architecture ideal for distributed systems and microservices.
* Simplifies data modeling with Protocol Buffers, ensuring consistent message formats.

## How to Run

```bash
# 1. Compile the .proto file
python -m grpc_tools.protoc -I=./proto --python_out=./app/proto --grpc_python_out=./app/proto ./proto/user.proto

# 2. Start the gRPC server
python grpc_server/server.py

# 3. Start the FastAPI app
uvicorn app.main:app --reload

# 4. Add a fake user
curl -X POST http://localhost:8000/users/add

# 5. Fetch user by ID (replace `2` with a valid ID)
curl http://localhost:8000/users/2
```

## Ideal For

* Developers exploring microservices using modern Python tooling.
* Prototyping backend communication with high-performance, low-latency RPC.
* Building scalable systems with separate transport layers for external and internal communication.

---
