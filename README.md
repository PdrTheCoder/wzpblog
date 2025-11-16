# Blog Project

A personal blog platform built with a Flask backend, PostgreSQL database, and a React frontend.
The project supports both local development and full Docker-based deployment.

---

## Features

* Flask REST API backend
* PostgreSQL database
* React single-page application
* Docker Compose support for dev and production
* Simple and consistent workflow
* Pixel style

---

## Project Structure

```
.
├── backend/        # Flask API service
├── frontend/       # React SPA
├── docker-compose.dev.yml
├── docker-compose.pro.yml
└── README.md
```

---

## Development

### Start Backend + Database (Docker)

```
docker compose -f docker-compose.dev.yml up
```

This will start the Flask backend and PostgreSQL database.

### Start Frontend (Locally)

```
cd frontend
npm install
npm start
```

The frontend will run at:
`http://localhost:3000`

---

## Production

Run backend, database, and frontend (served by Nginx) in Docker:

```
docker compose -f docker-compose.yml up --build -d
```

This will build the React app, serve it via Nginx, and run all services together.

---

## Environment Variables

You can define environment variables in `.env` or `.env.development` files.
Common variables include:

```
DATABASE_URL=postgresql://user:password@db:5432/blogdb
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret
```

---

## License

This is a personal project. All rights reserved unless otherwise stated.

---
