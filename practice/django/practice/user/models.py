from django.db import models
from django.contrib.auth.models import User


# class User_Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    item_id = models.IntegerField()

    def __str__(self):
        if self.user == None:
            return self.item_name
        else:
            return (self.item_name + '- Owned by: ' + self.user.username) 

 