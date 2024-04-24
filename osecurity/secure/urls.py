from .views import Sign_in,AddCredentials,get_Credentials,Sign_Out
from django.urls import path


urlpatterns = [
    path('add_credentials', AddCredentials.as_view()),
    path('get_credentials', get_Credentials.as_view()),
    path('Sign_In', Sign_in.as_view()),
    path('Sign_Out',Sign_Out.as_view())
]
