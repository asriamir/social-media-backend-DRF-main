from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    RegisterView,
    CustomTokenObtainPairView,
    UserListView,
    UserDetailView,
    ProfileUpdateView,
    VisitProfileView
)

urlpatterns = [
    path("signup/", RegisterView.as_view(), name="signup"),
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain"),
    path("refresh-token/", TokenRefreshView.as_view(), name="token_refresh"),
    path("accounts/", UserListView.as_view(), name="accounts"),
    path("accounts/<int:pk>/", UserDetailView.as_view(), name="account_detail"),
    path("profile/", ProfileUpdateView.as_view(), name="profile_update"),  
    path("profile/visit/", VisitProfileView.as_view(), name="visit_profile"),
]
