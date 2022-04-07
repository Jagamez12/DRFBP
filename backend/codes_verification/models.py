from django.db import models
import random
from accounts.models import UserAccount
# Create your models here.


class Code(models.Model):

    number = models.CharField(max_length=5, blank=True)
    user = models.OneToOneField(UserAccount, on_delete = models.CASCADE)
    

