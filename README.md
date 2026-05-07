# mini-rag 

RAG to Production: Architecture & Implementation
This repository documents the evolution of a Retrieval-Augmented Generation (RAG) application, transitioning from experimental notebooks into a scalable, production-grade system.

- System Architecture
The project is built on a modular, decoupled architecture designed to handle intensive AI workloads while maintaining high availability and data integrity.

1. Backend Framework & API Design
The core service is built with FastAPI, prioritizing high performance and asynchronous execution.

Scalable Routing: Implementation of nested routes for clean API versioning and resource management.

Environment Management: Robust handling of secrets and configurations across development and production stages.

File Processing: A dedicated pipeline for uploading and pre-processing raw documents for the RAG engine.

2. Data Layer Evolution
We document the transition from flexible prototyping to structured, high-performance production storage:

Prototyping Phase: Utilized MongoDB with Motor (asynchronous driver) for rapid schema iteration and initial indexing.

Production Phase: Migrated to PostgreSQL using SQLAlchemy ORM for relational integrity, with Alembic handling automated database migrations.

Vector Engine: Implementation of semantic search using Qdrant for high-performance vector indexing, and PGVector for integrated relational/vector queries within PostgreSQL.

3. AI & LLM Orchestration
The system utilizes a Factory Pattern to remain model-agnostic and flexible:

LLM Factory: A centralized provider to switch between different model backends seamlessly.

Local Inference: Integration with Ollama to enable local LLM execution, reducing latency and API costs.

RAG Logic: Advanced semantic search algorithms that retrieve contextually relevant data to generate "Augmented Answers."

4. Production-Grade Tooling
To move beyond the "it works on my machine" stage, we integrated industry-standard DevOps tools:

Asynchronous Processing: Celery manages background tasks (like document embedding) to keep the API responsive.

Containerization: Full Docker integration ensures environment parity across the entire development lifecycle.

Deployment Pipeline: A two-stage deployment strategy focused on stability and zero-downtime updates

##  Requrements 

- Python 3.10 or later 

### install pythong using miniconda 

- go to the cmd  and write these commands 

1) download and install mini conda from [here](https://www.anaconda.com/docs/getting-started/miniconda/install/linux-install)

``` bash 
$ curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh 
```
2) create the environment 
``` bash
~ conda create -n mini-rag-app python=3.10 
``` 
3) Activate the environment:
``` bash 
$ conda activate mini-rag-app
``` 

### install required packages 

``` bash
$ pip install -r requirements.txt 
``` 
### setup environment variables
$ cp .env.example .env

- Set your environment variables in your `.env` like `OPEN_API_KEY` to your actual key in OpenAI.

### Starting the application

1) run fastapi
```bash
$ uvicorn src.main:app --reload
``` 

