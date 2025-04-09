# 🍽️ Restaurant Table Reservation API

RESTful API-сервис для бронирования столиков в ресторане. Создан с использованием FastAPI, SQLAlchemy, Alembic, PostgreSQL и Docker.

## 📦 Технологии

- **FastAPI** — современный, быстрый (high-performance) веб-фреймворк
- **SQLAlchemy** — ORM для работы с PostgreSQL
- **Alembic** — инструмент миграций для SQLAlchemy
- **PostgreSQL** — надежная реляционная СУБД
- **Docker / docker-compose** — контейнеризация
- **Pydantic** — валидация и сериализация данных

---

## 🚀 Быстрый старт

### 1. Клонируй репозиторий

```bash
git clone https://github.com/Lyudvig33/Python-task


2. Создай .env файл
Создай файл .env в корне проекта:
env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=restaurant
DATABASE_URL=postgresql://postgres:postgres@db:5432/restaurant


3. Запусти проект с помощью Docker
docker-compose up --build

Миграции Alembic
Создание миграции
alembic revision --autogenerate -m "Initial migration"

Применение миграции
alembic upgrade head

```
