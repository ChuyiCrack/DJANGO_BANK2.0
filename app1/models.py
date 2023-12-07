from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Movement(models.Model):
    money=models.IntegerField()
    Type_Movement=models.CharField(max_length=50)
    Date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Type_Movement

class Transfer(Movement):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='owner')
    receiver=models.ForeignKey(User,on_delete=models.CASCADE,related_name='receiver')

    def __str__(self):
        return self.owner.username
    
class Bank_Account(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    balance=models.IntegerField()
    movements=models.ManyToManyField(Movement)

    def __str__(self):
        return self.owner.username