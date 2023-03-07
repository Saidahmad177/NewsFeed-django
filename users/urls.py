from django.urls import path
from users.views import sign_up, user_logout, login_page, profile, password_chang, password_change

urlpatterns = [
    path('logout/', user_logout, name='logout'),
    path('signup/', sign_up, name='signup'),
    path('login/', login_page, name='login'),
    path('profile/', profile, name='profile'),
    path('password-changew/', password_chang, name='passwor'),
    path('password-change/', password_change, name='password_change'),


]
