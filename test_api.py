
import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from posts.models import Post

@pytest.fixture
def api_client():
    """ ایجاد کلاینت API برای ارسال درخواست‌ها """
    return APIClient()

@pytest.fixture
def test_user(db):
    """ ایجاد یک کاربر تستی """
    User = get_user_model()
    user = User.objects.create_user(email="testuser@example.com", password="TestPass123", name="Test User")
    return user

@pytest.fixture
def auth_client(api_client, test_user):
    """ ایجاد یک کاربر احراز هویت شده و دریافت توکن """
    response = api_client.post("/api/token/", {"email": "testuser@example.com", "password": "TestPass123"})
    token = response.data["access"]
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return api_client

@pytest.fixture
def test_post(test_user):
    """ ایجاد یک پست تستی """
    return Post.objects.create(user=test_user, content="این یک پست تستی است!")

# ✅ **تست ثبت‌نام کاربر**
@pytest.mark.django_db
def test_signup(api_client):
    response = api_client.post("/api/signup/", {"email": "newuser@example.com", "password": "NewPass123", "name": "New User"})
    assert response.status_code == 201
    assert "id" in response.data

# ✅ **تست ورود کاربر**
def test_login(api_client, test_user):
    response = api_client.post("/api/token/", {"email": "testuser@example.com", "password": "TestPass123"})
    assert response.status_code == 200
    assert "access" in response.data

# ✅ **تست دریافت پروفایل کاربر لاگین شده**
def test_get_profile(auth_client):
    response = auth_client.get("/api/profile/")
    assert response.status_code == 200
    assert response.data["email"] == "testuser@example.com"

# ✅ **تست ایجاد پست**
def test_create_post(auth_client):
    response = auth_client.post("/api/add-post/", {"content": "این یک پست جدید است!"})
    assert response.status_code == 201
    assert response.data["content"] == "این یک پست جدید است!"

# ✅ **تست دریافت لیست پست‌ها**
def test_get_posts(api_client, test_post):
    response = api_client.get("/api/posts/")
    assert response.status_code == 200
    assert len(response.data) > 0

# ✅ **تست دریافت جزئیات یک پست**
def test_get_single_post(api_client, test_post):
    response = api_client.get(f"/api/post/{test_post.id}/")
    assert response.status_code == 200
    assert response.data["content"] == "این یک پست تستی است!"

# ✅ **تست ویرایش پست**
def test_update_post(auth_client, test_post):
    response = auth_client.put(f"/api/post/{test_post.id}/", {"content": "ویرایش پست"})
    assert response.status_code == 200
    assert response.data["content"] == "ویرایش پست"

# ✅ **تست حذف پست**
def test_delete_post(auth_client, test_post):
    response = auth_client.delete(f"/api/post/{test_post.id}/")
    assert response.status_code == 204
