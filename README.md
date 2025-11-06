# 🌐 Multi-language Translator API

A lightweight and fast multilingual translation API built with **FastAPI**, integrating **OpenAI** and **Deep Translator**.  
It allows translation of text into multiple languages in a single request, with translation tasks managed and stored in **PostgreSQL**.

---

## ⚙️ Tech Stack

- **FastAPI** — Modern asynchronous Python web framework
- **Python** — Core backend language
- **SQLAlchemy** — ORM for database models
- **PostgreSQL** — Database for persistent storage
- **OpenAI API** & **Deep Translator** — For translation processing
- **Uvicorn** — ASGI web server
- **Docker** & **Docker Compose** — Containerization and deployment
- **GitHub Actions** — CI/CD automation

---

## 🚀 Setup & Run

### 1️⃣ Clone the Repository

```bash
git clone <repo-url>
cd translator_app
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # For Linux/Mac
.venv\Scripts\activate     # For Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup Environment Variables

A `.env.example` file is included for reference.  
Create a `.env` file in the project root:

### 5️⃣ Run the Server

```bash
uvicorn app.main:app --reload
```

Then open your browser at:  
👉 **http://127.0.0.1:8000/index**

---

## 🧩 Example Request

**Endpoint:** `POST /translate/`  
**Payload:**

```json
{
  "text": "Hello my friend",
  "languages": ["fr", "es", "bn"]
}
```

**Response:**

```json
{
  "fr": "Bonjour mon ami",
  "es": "Hola mi amigo",
  "bn": "ওহে বন্ধু"
}
```

---

## 🐳 Run with Docker

### Build and run directly:

```bash
docker build -t translator .
docker run -d -p 8000:8000 translator
```

---

## 🧱 Run with Docker Compose (Recommended)

This project includes a **Docker Compose** file that launches the API along with PostgreSQL:

```bash
docker compose up --build
```

This will:

- Start the FastAPI server
- Initialize PostgreSQL using environment values from `.env`
- Expose the API at **http://localhost:8000**

---

## 🔄 CI/CD (GitHub Actions)

This repository includes a **CI pipeline** that automatically runs on every push or pull request to `main`:

The pipeline:

- Checks code formatting (Black)
- Runs automated tests
- Builds the Docker image using Buildx
- Logs in to Docker Hub
- Pushes the updated image to Docker Hub

This ensures consistent quality and deploy-ready builds.

---

## 📘 Project Overview

This project demonstrates:

- API development with FastAPI
- Asynchronous request handling
- Integration with third-party APIs (OpenAI, Deep Translator)
- Database-backed task management with PostgreSQL
- Containerization using Docker & Docker Compose
- CI/CD setup via GitHub Actions (build + test + push to DockerHub)

---

## ✨ Future Enhancements

- Read aloud translated text
- Voice based translation
- Include a web UI for interactive translation

---

## 👤 Author

**Arghya Malakar**  
📧 arghyaapply2016@gmail.com  
💻 [GitHub](https://github.com/hunterarghya)
