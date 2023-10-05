from django.urls import path
from .views import (
    CreateListRoles, ListUsers, RetrieveUpdateRole, CreateUsers,
    RetrieveUpdateDeleteUser, UserConfirmEmailAddress, UserForgetPassword,
    UserResetPassword, ApiStatusView, UserLoginView)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    
)



urlpatterns = [
    path("status/", ApiStatusView.as_view(), name="api-status"),
    path("roles/", CreateListRoles.as_view(), name="create-list-Roles"),
    path("roles/<str:pk>/", RetrieveUpdateRole.as_view(), name="retrieve-update-Role"),
    path("auth/sign_up/", CreateUsers.as_view(), name="create-Users"),
    path("users/", ListUsers.as_view(), name="list-Users"),
    path("users/<str:pk>/", RetrieveUpdateDeleteUser.as_view(), name="retrive-update-delete-User"),
    path('auth/sign_in/', UserLoginView.as_view(), name='user-login'),
    path('refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('confirm_email/', UserConfirmEmailAddress.as_view(), name="confirm-user-email"),
    path('forget_password/', UserForgetPassword.as_view(), name="forget-user-password"),
    path('reset_password/', UserResetPassword.as_view(), name="reset-user-password"),

]