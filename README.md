
---

# 🚀 FastAPI + gRPC Microservice

## 🧩 Overview

This project showcases a microservice architecture using **FastAPI** for RESTful APIs and **gRPC** for high-performance internal service communication, now fully containerized with **Docker** and orchestrated using **Docker Compose**.

## ⚙️ Core Functionality

* **🛠️ gRPC User Service**
  A dedicated gRPC server handles user-related operations:

  * `GetUser`: Retrieve a user by ID.
  * `AddFakeUser`: Create and return a fake user using the `Faker` library.

* **🔗 gRPC Client in FastAPI**
  The FastAPI app includes a gRPC client to interact with the gRPC server for user-related operations.

* **🌐 FastAPI REST API**

  * `POST /users/add`: Adds a fake user.
  * `GET /users/{user_id}`: Retrieves a user by ID.
    These endpoints call the gRPC server under the hood.

## 🚀 Dockerized Deployment

This project supports containerized deployment with:

* `Dockerfile` for each service.
* `docker-compose.yml` to spin up both FastAPI and gRPC services together.

## ✅ Benefits

* 🏎️ **High-Performance Communication**: gRPC ensures fast internal RPC.
* 🔀 **Decoupled Services**: Clean separation between REST and internal logic.
* 📦 **Easy Deployment**: One command to launch the full stack.
* 🔧 **Scalable Architecture**: Ideal for microservices and production setups.

## 📦 Deployment Made Easy

Launch the full system with:

```bash
docker-compose up --build
```

Everything is ready to run — no local setup needed!

## 👨‍💻 Perfect For

* Python developers exploring microservices and RPC.
* Teams building scalable and modular systems.
* Anyone looking to combine REST APIs with internal gRPC services.

---
