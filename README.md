# FastAPI CRUD Application

A complete, ready-to-run CRUD (Create, Read, Update, Delete) API built with FastAPI, SQLAlchemy, and SQLite. This project demonstrates best practices for structuring a FastAPI application with a database.

---

## 🚀 Features

- **Full CRUD Operations:** Create, read, update, and delete items via a RESTful API.
- **Automatic Interactive Documentation:** Enjoy live API docs with Swagger UI (`/docs`) and ReDoc (`/redoc`).
- **Database-Agnostic Design:** Uses SQLAlchemy ORM, supporting SQLite for development and easy PostgreSQL upgrade for production.
- **Pydantic Validation:** Robust request and response validation via Pydantic models.
- **Dependency Injection:** Clean management of database sessions.

---

## 📦 Project Structure

```
crud_fastapi/
├── .env                    # Environment variables (optional, for production)
├── .gitignore              # Files/folders not tracked by git
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation (this file)
└── app/
    ├── __init__.py         # Package marker
    ├── main.py             # FastAPI app setup and routes
    ├── database.py         # DB connection and setup
    ├── models.py           # SQLAlchemy ORM models (DB tables)
    ├── schemas.py          # Pydantic models (request/response shapes)
    └── crud.py             # Core CRUD operations
```

---

## ⚡ Setup & Installation

1. **Clone the repository or create the project directory:**
    ```bash
    mkdir crud_fastapi
    cd crud_fastapi
    ```

2. **Create a Virtual Environment (Recommended):**
    ```bash
    # On macOS/Linux
    python -m venv venv
    source venv/bin/activate
    # On Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## ▶️ Running the Application

Start the Uvicorn server:

```bash
uvicorn app.main:app --reload
```
- `--reload`: Enables auto-reload on code changes (for development).

The application will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## 📚 API Endpoints & Interactive Documentation

Once the server is running, interact with the API:

### 1. Swagger UI (Interactive Docs)

Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- Explore and test all endpoints live in your browser.

### 2. ReDoc (Alternative Docs)

Visit: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)  
- Readable, clean documentation format.

---

### 📑 API Endpoints Table

| Method | Endpoint            | Description              | Parameters / Body                         |
|--------|---------------------|--------------------------|-------------------------------------------|
| GET    | `/`                 | Welcome message          | -                                         |
| POST   | `/items/`           | Create a new item        | `{"name": "string", "price": float, "description": "string"}` |
| GET    | `/items/`           | Get a list of items      | `skip` (int), `limit` (int)               |
| GET    | `/items/{item_id}`  | Get a single item by ID  | `item_id` (path)                          |
| PUT    | `/items/{item_id}`  | Update an existing item  | `item_id` (path), JSON body               |
| DELETE | `/items/{item_id}`  | Delete an item           | `item_id` (path)                          |

---

## 🧪 Testing the API

1. **Create an Item (POST):**
    - Go to `/docs`, find `POST /items/`, click "Try it out".
    - Enter:
      ```json
      {
        "name": "Laptop",
        "price": 999.99,
        "description": "A powerful gaming laptop"
      }
      ```
    - Click "Execute". The response shows your new item and its auto-generated ID.

2. **Read Items (GET):**
    - Use `GET /items/` for all items.
    - Use `GET /items/1` (replace `1` with your item's ID) for a single item.

3. **Update an Item (PUT):**
    - Use `PUT /items/1` with a new JSON body to update the item's details.

4. **Delete an Item (DELETE):**
    - Use `DELETE /items/1` to remove the item.

---

## 🛠️ Troubleshooting & Common Issues

### 1. `ModuleNotFoundError: No module named 'app'`
- **Reason:** Running `uvicorn` from the wrong directory.
- **Solution:** Run `uvicorn` from the project root (`crud_fastapi/`), **not** inside `app/`.

### 2. `sqlalchemy.exc.OperationalError: ... unable to open database file`
- **Reason:** Permission issues writing the SQLite file.
- **Solution:** Ensure the user running the app has write permissions in the directory.

### 3. `ValueError: ... keywords must be strings ...` in `crud.py`
- **Reason:** Pydantic version mismatch (`.dict()` vs `.model_dump()`).
- **Solution:** Use `.model_dump()` for Pydantic v2 as in this project, or change to `.dict()` if on v1.

### 4. Port 8000 is already in use
- **Solution:** Stop the other app or run on another port:
    ```bash
    uvicorn app.main:app --reload --port 8001
    ```

---

## 🚀 Next Steps & Production Readiness

- **Switch to PostgreSQL:** Replace the SQLite connection string in `database.py` with your PostgreSQL URL (see `.env`).
- **Use Environment Variables:** With `python-dotenv`, load sensitive config from `.env`.
- **Add Authentication:** Secure endpoints with OAuth2/JWT.
- **Write Tests:** Use `pytest` for unit/integration tests.
- **Containerize:** Add `Dockerfile` and `docker-compose.yml` for deployment.

---

**This starter gives you a professional foundation for building real-world FastAPI applications. Happy coding!**
