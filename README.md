# 📊 Sentiment Analysis Web App

A lightweight **sentiment analysis web application** built with **FastAPI** (backend) and **Streamlit** (frontend), using **NLTK VADER** for efficient sentiment scoring. The project is fully **containerized with Docker Compose**, providing both an interactive UI and REST API.

## 🚀 Features

- ✨ **Real-time sentiment analysis** of user input text
- 🪶 **Lightweight NLTK VADER** model (no heavy ML/transformer dependency)
- ⚡ **FastAPI backend** exposing REST API endpoints
- 🖥️ **Streamlit frontend** for interactive user experience
- 🐳 **Containerized with Docker Compose** for easy deployment
- 📝 **Swagger UI documentation** for API exploration


## 🛠️ Getting Started

### Prerequisites

- Docker
- Docker Compose

### 1. Clone the Repository

```bash
git clone https://github.com/Bharat-Sh/Sentiment-analysis.git
cd Sentiment-analysis
```

### 2. Run with Docker Compose

Make sure you have Docker installed and running.

```bash
docker compose up --build
```

### 3. Access the Application

- **Streamlit Frontend** → [http://localhost:8501](http://localhost:8501)
- **FastAPI Docs (Swagger UI)** → [http://localhost:8000/docs](http://localhost:8000/docs)
- **FastAPI Backend** → [http://localhost:8000](http://localhost:8000)

## 📊 API Usage

### Analyze Sentiment

**Endpoint:** `POST /analyze`

**Request Body:**
```json
{
  "sentence": "I love using FastAPI!"
}
```

**Response:**
```json
{
  "sentence": "I love using FastAPI!",
  "scores": {
    "neg": 0.0,
    "neu": 0.33,
    "pos": 0.67,
    "compound": 0.85
  },
  "sentiment": "positive"
}
```

### Health Check

**Endpoint:** `GET /health`

**Response:**
```json
{
  "status": "healthy",
  "service": "sentiment-analysis-api"
}
```

## 🧰 Tech Stack

- **[FastAPI](https://fastapi.tiangolo.com/)** – Modern, fast web framework for building APIs
- **[Streamlit](https://streamlit.io/)** – Interactive web app framework
- **[NLTK VADER](https://www.nltk.org/)** – Sentiment analysis lexicon and rule-based tool
- **[Docker](https://www.docker.com/)** & **Docker Compose** – Containerization and orchestration
- **[Python 3.9+](https://www.python.org/)** – Programming language

## 📈 VADER Sentiment Scores

VADER (Valence Aware Dictionary and sEntiment Reasoner) provides four sentiment scores:

- **`neg`** - Negative sentiment score (0.0 to 1.0)
- **`neu`** - Neutral sentiment score (0.0 to 1.0)  
- **`pos`** - Positive sentiment score (0.0 to 1.0)
- **`compound`** - Overall sentiment score (-1.0 to +1.0)

**Classification Rules:**
- `compound >= 0.05` → **Positive**
- `compound <= -0.05` → **Negative**
- `-0.05 < compound < 0.05` → **Neutral**

## 🔧 Development Setup

### Backend Development

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Development

```bash
cd frontend  
pip install -r requirements.txt
streamlit run app.py --server.port 8501
```

## 🚀 Deployment

### Docker Compose (Recommended)

```bash
docker compose up -d --build
```

### Individual Services

**Backend:**
```bash
docker build -t sentiment-backend ./backend
docker run -p 8000:8000 sentiment-backend
```

**Frontend:**
```bash
docker build -t sentiment-frontend ./frontend  
docker run -p 8501:8501 sentiment-frontend
```

## 📝 Example Usage

### Using cURL

```bash
curl -X POST "http://localhost:8000/analyze" \
     -H "Content-Type: application/json" \
     -d '{"sentence": "This is an amazing project!"}'
```

### Using Python requests

```python
import requests

response = requests.post(
    "http://localhost:8000/analyze",
    json={"sentence": "I'm feeling great today!"}
)
print(response.json())
```

## 📌 Future Improvements

- 🌐 Add support for multiple languages
- ☁️ Deploy on AWS / Azure / GCP
- 📦 Extend API for batch sentiment analysis
- 📊 Add sentiment visualization charts
- 🔐 Implement API authentication
- 📈 Add analytics and usage tracking
- 🎯 Fine-tune sentiment classification thresholds
- 💾 Add database integration for storing results





