from django.urls import path 
from . import views 


urlpatterns = [
    path('code_verification/', views.generate_code)
]