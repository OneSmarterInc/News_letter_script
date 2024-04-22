from .views import Sign_in,add_Credentials,get_Credentials
from django.urls import path
urlpatterns = [
    path('add_credentials', add_Credentials.as_view()),
    path('get_credentials', get_Credentials.as_view()),
    path('Sign_In', Sign_in.as_view())
]