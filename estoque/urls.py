from django.urls import path
from .views import RegisterView, LoginView, UserLogout, UserView

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('logout', UserLogout.as_view(), name='logout'),
    path('user', UserView.as_view(), name='user'),
]

