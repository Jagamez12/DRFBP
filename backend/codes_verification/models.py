from django.db import models
from accounts.models import UserAccount
# Create your models here.

class Code(models.Model):

    number = models.CharField(max_length=5, blank=True)
    user = models.CharField(max_length=55, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)  

    def __str__(self):
        return self.number
        
        



