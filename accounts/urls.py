from django.urls import path
from accounts.views import UserRegistrationView, activate
from django.contrib.auth.views import LoginView, LogoutView
# here capital letter starts( UserRegistration,loginView ) are class and small letter(activate) are methods
# class harulai .as_view() import garnu parxa
# urls
urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="user_register"),
    path("activate/<uidb64>/<token>", activate, name="activate"),
    path("login/", LoginView.as_view(template_name="accounts/login.html"), name="login"),# template_name="accounts/login.html is used because its default gives template_name="register/login.html
    path("logout/", LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
]