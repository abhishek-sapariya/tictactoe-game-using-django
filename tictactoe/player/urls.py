from django.urls import path
from .views import home,new_invitation,accept_invitation, SignUpView
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('home',home,name="player_home"),
    path('login',LoginView.as_view(template_name="player/login_form.html"),name="player_login"),
    path('logout',LogoutView.as_view(),name="player_logout"),
    path('new_invitation',new_invitation,name="player_new_invitation"),
    path('accept_invitation/<int:id>',accept_invitation,name="player_accept_invitation"),
    path('signup',SignUpView.as_view(),name="player_signup"),
]