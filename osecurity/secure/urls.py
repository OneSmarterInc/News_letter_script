from .views import Sign_in,AddCredentials,get_Credentials
from django.urls import path
urlpatterns = [
    path('add_credentials', AddCredentials.as_view()),
    path('get_credentials', get_Credentials.as_view()),
    path('sign_in', Sign_in.as_view())
]