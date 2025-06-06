
---

# 🚀 FastAPI + gRPC Microservice

## 🧩 Overview

This project showcases a microservice architecture using **FastAPI** for RESTful APIs and **gRPC** for high-performance internal service communication — now **fully containerized** with **Docker**, **Docker Compose**, and **CI/CD integration via GitHub Actions**.

---

## ⚙️ Core Functionality

### 🛠️ gRPC User Service
A dedicated gRPC server handles user operations:
- `GetUser`: Retrieve a user by ID.
- `AddFakeUser`: Generate and return a fake user using the `Faker` library.

### 🔗 FastAPI REST API (gRPC Client)
The FastAPI service exposes RESTful endpoints:
- `POST /users/add`: Adds a fake user (via gRPC).
- `GET /users/{user_id}`: Fetches a user by ID (via gRPC).

This keeps the external API HTTP-friendly, while using gRPC for internal logic.

---

## 📦 Containerized Microservices

- 🐳 `Dockerfile.fastapi`: For FastAPI service (REST + gRPC client)
- 🐳 `Dockerfile.grpc`: For gRPC user service
- 🧰 `docker-compose.yml`: Launches both services together using shared networking

---

## 🔁 CI/CD with GitHub Actions

Automatic build and push to Docker Hub:
- Builds **separate images** for FastAPI and gRPC services
- Pushes to:
  - `dhiraj918106/fastapi-grpc-microservice-fastapi`
  - `dhiraj918106/fastapi-grpc-microservice-grpc`
- Ensures fast, reproducible deployments on every push to `main`

---

## ✅ Key Benefits

- ⚡ **High-Performance RPC**: Fast gRPC communication under the hood
- 🧩 **Decoupled Architecture**: REST interface + isolated internal services
- 🐳 **Easy Local & Cloud Deployment**: Fully Dockerized
- 🚀 **Production-Ready CI/CD**: Pushes directly to Docker Hub

---

## 🚀 Quick Start

### 1️⃣ Build and Run Locally:
```bash
docker-compose up --build
```

### 2️⃣ Test APIs:
```bash
curl -X POST http://localhost:8000/users/add
curl http://localhost:8000/users/1
```

---

## 👨‍💻 Ideal For

- Python developers exploring **microservices** and **RPC**
- Backend engineers designing **modular, scalable systems**
- Teams combining **REST APIs** with **gRPC** services

---
