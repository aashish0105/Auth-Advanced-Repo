from django.urls import path
from .views import *

urlpatterns=[
    path("password_reset",password_reset_request, name="password_reset")
]