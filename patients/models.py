from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    GENDER = [
    ("M", "MALE"),
    ("F", "FEMALE"),
]
    name = models.CharField(max_length=60)
    age = models.IntegerField()
    gender = models.CharField(max_length=50 ,choices=GENDER)
    phone = models.CharField(max_length=10)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name