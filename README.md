# **Kafka Event LLM Backend**

This project is an async, event-driven backend for running LLM tasks using Kafka, FastAPI, Redis, and independent worker processes.
It’s designed so your API stays fast while the heavy LLM work happens in the background.

---

## **📌 Features**

### **1. FastAPI entrypoint**

* `/process` accepts an LLM job (provider, model, prompt)
* Generates a unique `request_id`
* Publishes the job to Kafka instantly
* Returns immediately to the client

### **2. Background LLM worker**

A separate worker service:

* Listens to `llm.requests`
* Runs the correct LLM provider (Groq, OpenAI, etc.)
* Handles retries and error capture
* Publishes final output to `llm.responses`

### **3. Redis result storage**

* Stores pending state (`status: pending`)
* Stores final LLM output or error
* Results expire automatically (TTL)
* FastAPI reads results through `/result/{request_id}`

### **4. Kafka-based architecture**

* Fully async
* Horizontal scaling: run more workers any time
* Decoupled API and inference pipeline
* Works with any LLM provider through `llm_factory`

---

## **📦 System Architecture**

```
Client → FastAPI → Kafka (llm.requests) → Worker → LLM Provider
                                               ↓
                                             Redis
                                               ↓
                                   FastAPI /result/{id}
```

Each part runs as its own service via Docker Compose.

---

## **🚀 Endpoints**

### **POST /process**

Submit an LLM job.

```json
{
  "provider": "groq",
  "model": "openai/gpt-oss-120b",
  "prompt": "Hello world"
}
```

**Response:**

```json
{
  "request_id": "uuid-123..."
}
```

The LLM runs in the background.

---

### **GET /result/{request_id}**

Check job output.

**Possible responses:**

Pending:

```json
{"status": "pending"}
```

Success:

```json
{
  "provider": "groq",
  "model": "mixtral-8x7b",
  "output": "Hello!",
  "error": null
}
```

Failed:

```json
{
  "error": "Model does not exist"
}
```

---

## **🧱 Tech Stack**

* **FastAPI** — main HTTP API
* **Kafka** — event streaming backbone
* **Redis** — result cache (with TTL)
* **Groq / OpenAI** — LLM providers
* **Docker Compose** — multi-service orchestration
* **Async Python** — end-to-end asyncio

---

## **⚙️ Environment Variables**

Create a `.env` file:

```
KAFKA_BOOTSTRAP_SERVERS=kafka:9092
REQUEST_TOPIC=llm.requests
RESPONSE_TOPIC=llm.responses
DLQ_TOPIC=llm.dlq

# Workers
KAFKA_GROUP_ID=worker

# Redis
REDIS_HOST=redis
REDIS_PORT=6379

# LLM Providers
GROQ_API_KEY=your_key
OPENAI_API_KEY=your_key
```

---

## **🐳 Running the System**

Start all services:

```
docker compose up --build
```

Services included:

* zookeeper
* kafka
* fastapi_app
* llm_worker
* redis

---

## **🧪 Testing the Pipeline**

### 1️⃣ Send a request:

```
curl -X POST http://localhost:8000/process \
  -H "Content-Type: application/json" \
  -d '{"provider":"groq","model":"openai/gpt-oss-120b","prompt":"hello"}'
```

Response:

```json
{"request_id": "123e..."}
```

### 2️⃣ Check result:

```
curl http://localhost:8000/result/123e...
```

---

## **📈 Scaling Workers**

You can run more workers:

```
docker compose up --scale worker=3
```

Kafka will auto-balance the workload across consumers in the group.

---

## **🧹 Automatic Cleanup**

Each result in Redis auto-expires after **5 minutes**.
This keeps memory usage low and avoids having to maintain a database.