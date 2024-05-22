from django.contrib.auth.models import User
from django.db import models
from items.models import Item

class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.CharField(max_length=100)
    items = models.ManyToManyField(Item)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order {self.id} by {self.owner.username}'
