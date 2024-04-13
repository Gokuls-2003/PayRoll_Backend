from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    employee = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employee")
    email_id = models.EmailField("Email Id", max_length=100, blank=True, null=True)
    phone_number = models.CharField("Phone Number", null=True, blank=True)
    role = models.CharField("role", max_length=3, default=None, choices=[
        ('SD', 'Software Developer'),
        ('T', 'Tester'),
        ('D', 'Designer'),
        ('M', 'Manager')
    ]
)