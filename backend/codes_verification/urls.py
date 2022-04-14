from django.urls import path 
from . import views 


urlpatterns = [
    path('code_verification/', views.generate_code),
    path('code_confirmation/', views.consulte_code),
]
