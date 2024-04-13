from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    employee = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="employee")
    email_id = models.EmailField(
        "Email Id", max_length=100, blank=True, null=True)
    contact_number = models.CharField(
        "Phone Number", max_length=15, null=True, blank=True)
    role = models.CharField("role", max_length=3, default=None, choices=[
        ('SD', 'Software Developer'),
        ('T', 'Tester'),
        ('D', 'Designer'),
        ('M', 'Manager')
    ])


class Leave(models.Model):
    start_date = models.DateField("Strart Date")
    end_date = models.DateField("end Date")
    Employee = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField("Reason", max_length=200)
    leave_status = models.CharField('Leave Status', max_length=1, default="P", choices=[
        ('P', 'Pending'),
        ('A', 'Approved'),
        ('D', 'Denied')
    ])
