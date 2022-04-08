from django.db import models
import random
from accounts.models import UserAccount
# Create your models here.

class Code(models.Model):

    number = models.CharField(max_length=5, blank=True)
    user = models.OneToOneField(UserAccount, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.number
        
        



