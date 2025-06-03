
# FastAPI + gRPC Microservice 🚀

## Overview
This project demonstrates a simple microservice architecture combining **FastAPI** for building HTTP APIs and **gRPC** for efficient, high-performance communication between services.

## Core Functionality
- **gRPC Server**  
  Implements a user service that handles requests via the gRPC protocol, enabling fast and strongly-typed communication.

- **gRPC Client**  
  Acts as a bridge inside the FastAPI application to communicate with the gRPC server and fetch user data.

- **FastAPI HTTP API**  
  Provides a RESTful HTTP interface for clients, internally calling the gRPC client to retrieve user information.

## Key Benefits
- Leverages gRPC's high-performance RPC framework for backend service communication.
- Exposes simple REST endpoints via FastAPI for easy consumption by web or mobile clients.
- Clear separation between transport layers: HTTP for external communication and gRPC for internal microservice calls.
- Scalable and modular architecture suitable for building distributed systems.

## How to Run
1. Start the gRPC server to handle backend requests.
2. Run the FastAPI application which serves HTTP endpoints.
3. Access user data through the FastAPI REST API, which internally communicates with the gRPC service.

## Ideal For
- Developers looking to learn or prototype microservices with modern Python frameworks.
- Systems requiring efficient communication between backend components.
- Applications combining the ease of RESTful APIs with the power of gRPC.


