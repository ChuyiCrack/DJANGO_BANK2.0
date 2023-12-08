from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Movement(models.Model):
    money=models.IntegerField()
    Type_Movement=models.CharField(max_length=50)
    Date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Type_Movement

    
class Bank_Account(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    balance=models.IntegerField()
    movements=models.ManyToManyField(Movement,blank=True)

    def __str__(self):
        return self.owner.username
    
class Transfer(Movement):
    transmitter=models.ForeignKey(Bank_Account,on_delete=models.CASCADE,related_name='transmitter',default=1)
    receiver=models.ForeignKey(Bank_Account,on_delete=models.CASCADE,related_name='receiver')
    title=models.CharField(max_length=25,blank=False)
    message=models.TextField(max_length=200,blank=True)

    def __str__(self):
        return self.transmitter.owner.username+' to '+self.receiver.owner.username