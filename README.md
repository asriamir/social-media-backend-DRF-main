# Social Media API

## 📌 Introduction

`Social Media API` is a Django REST Framework (DRF) based backend for a social networking platform. Users can sign up, authenticate via JWT, manage profiles, create posts, and interact with the API securely.

### **Tech Stack**

- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** JWT (Simple JWT)
- **Documentation:** Swagger UI (drf-spectacular)
- **Containerization:** Docker & Docker Compose
- **Testing:** Pytest

---

## 📌 Installation & Setup

### **🔹 Method 1: Running Locally**

```sh
# Clone the repository
$ https://github.com/asriamir/social-media-backend-DRF-main.git
$ cd social_media

# Create virtual environment
$ python -m venv venv
$ source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
$ pip install -r requirements.txt

# Apply database migrations
$ python manage.py migrate

# Create superuser for admin panel
$ python manage.py createsuperuser

# Run the development server
$ python manage.py runserver
```

✅ The API is now accessible at `http://127.0.0.1:8000/`

---

### **🔹 Method 2: Running with Docker**

```sh
# Build and start the Docker containers
$ docker-compose up --build -d

# Apply migrations inside Docker
$ docker-compose exec web python manage.py migrate

# Create superuser inside Docker
$ docker-compose exec web python manage.py createsuperuser
```

✅ The API is now running in a Docker container at `http://127.0.0.1:8000/`

### ِDocker Commands for Management

```sh
# Start the containers
$ docker-compose up -d
# Stop the containers
$ docker-compose down
# Rebuild and restart the containers
$ docker-compose up --build -d
# View logs in real-time
$ docker-compose logs -f
```

## 📌 API Documentation

The API is fully documented using Swagger UI and Redoc.

### **🔹 Swagger UI:**

📌 [`http://127.0.0.1:8000/api/swagger/`](http://127.0.0.1:8000/api/swagger/)

### **🔹 Redoc:**

📌 [`http://127.0.0.1:8000/api/redoc/`](http://127.0.0.1:8000/api/redoc/)

### **🔹 OpenAPI Schema:**

📌 [`http://127.0.0.1:8000/api/schema/`](http://127.0.0.1:8000/api/schema/)

---

## 📌 Admin Panel

The Django Admin panel allows for managing users and posts efficiently.

📌 [`http://127.0.0.1:8000/admin/`](http://127.0.0.1:8000/admin/)

---

## 📌 API Endpoints

### **🔹 Authentication & User Management**

| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/api/signup/` | User registration |
| `POST` | `/api/token/` | Obtain access and refresh tokens |
| `POST` | `/api/refresh-token/` | Refresh access token |
| `GET`  | `/api/accounts/` | List all users |
| `GET`  | `/api/accounts/<id>/` | Retrieve a specific user |
| `GET`  | `/api/profile/` | Retrieve authenticated user's profile |
| `PUT`/`PATCH` | `/api/profile/` | Update user profile |
| `POST` | `/api/profile/visit/` | Record profile visits |
| `DELETE` | `/api/profile/` | Delete user account |

### **🔹 Posts Management**

| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/api/add-post/` | Create a new post |
| `GET`  | `/api/posts/` | List all posts |
| `GET`  | `/api/post/<id>/` | Retrieve a single post |
| `PUT`/`PATCH` | `/api/post/<id>/` | Update a post |
| `DELETE` | `/api/post/<id>/` | Delete a post |

✅ **Permissions:**

- Only authenticated users can create and manage posts.
- All users can view public posts.
- Users can only edit or delete their own posts.

---

## 📌 Running Tests

Unit tests are written using `pytest` and `pytest-django`.

```sh
# Run tests
$ pytest -v --disable-warnings
```

✅ **Test cases include:**

- User authentication (`signup`, `login`, `profile retrieval`)
- CRUD operations on posts
- Profile update and visit count

---

## 📌 Managing Docker Containers

```sh
# Restart containers
$ docker-compose restart

# View logs
$ docker-compose logs -f

# Access Django shell inside container
$ docker-compose exec web python manage.py shell
```

---

## 📌 Future Improvements

✅ **Potential features for future updates:**

- Like system for posts ❤️
- Follow/unfollow users 👥
- Real-time notifications 🔔
- Role-based permissions for enhanced security 🔒

---

## 📌 Conclusion

🚀 The `Social Media API` is a fully functional backend for managing users and posts with JWT authentication, PostgreSQL, Docker support, and API documentation via Swagger. This project is scalable and can be extended with more features in the future.

📌 **Developed with Django & DRF** 😃
