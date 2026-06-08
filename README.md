# SHRTN — URL Shortener

A full-stack URL shortener built with **FastAPI** and **vanilla HTML/CSS/JS**, backed by **PostgreSQL**.

---

## Features

- **Create** short URLs from any long link
- **Redirect** — visiting a short URL takes you to the original destination
- **Edit** — update the destination of an existing short URL
- **Delete** — permanently remove a short URL
- **Analytics** — view access count, creation date, and last updated time per link

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI, SQLAlchemy 2.x, PostgreSQL |
| Frontend | HTML, CSS, Vanilla JS (no framework) |
| Server | Uvicorn |
| Package Manager | uv |

---

## Project Structure

```
├── backend/
│   ├── app.py              # FastAPI routes
│   ├── db.py               # Database engine & session
│   ├── model.py            # SQLAlchemy ORM model
│   ├── validation_model.py # Pydantic schemas
│   └── utility.py          # Shortcode generator
├── frontend/
│   ├── index.html          # Create short URL
│   ├── edit.html           # Edit destination URL
│   ├── delete.html         # Delete a short URL
│   ├── analytics.html      # View link stats
│   ├── 404.html            # Redirect handler
│   ├── serve.js            # Local dev server (Node.js)
│   ├── css/style.css
│   └── js/utils.js
└── main.py                 # Uvicorn entrypoint
```

---

## Getting Started

### Prerequisites

- Python 3.14+
- PostgreSQL running locally
- Node.js (for local frontend server)
- [uv](https://github.com/astral-sh/uv)

### 1. Clone & install dependencies

```bash
git clone <your-repo-url>
cd url-shortener
uv sync
```

### 2. Configure the database

Update the connection string in `.env`:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/urlshortner
```

### 3. Run the backend

```bash
python main.py
# API available at http://localhost:8000
```

### 4. Run the frontend

```bash
cd frontend
node serve.js
# Frontend available at http://localhost:5500
```

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/shrtn` | Create a short URL |
| `GET` | `/shrtn/{code}` | Get URL info (increments click count) |
| `PUT` | `/shrtn/{code}` | Update destination URL |
| `DELETE` | `/shrtn/{code}` | Delete a short URL |
| `GET` | `/shrtn/{code}/stats` | Get analytics (includes access count) |

---


> Inspired by [roadmap.sh/projects/url-shortening-service](https://roadmap.sh/projects/url-shortening-service)