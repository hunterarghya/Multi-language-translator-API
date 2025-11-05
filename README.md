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
- **Docker** — Containerization and deployment
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

Create a `.env` file in the project root:

```bash
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-3.5-turbo
DATABASE_URL=postgresql://user:password@localhost/translationservice
```

### 5️⃣ Run the Server

```bash
cd app
uvicorn app.main:app --reload
```

Then open your browser at:  
👉 **http://127.0.0.1:8000**

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

Build and run the container:

```bash
docker build -t polyglot-translator .
docker run -d -p 8000:8000 polyglot-translator
```

---

## 🔄 CI/CD (GitHub Actions)

A simple CI pipeline can be set up using **GitHub Actions** to:

- Automatically run tests
- Lint code
- Build and push Docker images

This ensures every commit is validated before deployment.

---

## 📘 Project Overview

This project demonstrates:

- API development with FastAPI
- Asynchronous request handling
- Integration with third-party APIs (OpenAI, Deep Translator)
- Database-backed task management with PostgreSQL
- Containerization using Docker
- CI/CD setup via GitHub Actions

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
