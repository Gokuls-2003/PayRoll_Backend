from django.db import models
from employee.models import Employee
# Create your models here.


class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    basic_salary = models.IntegerField("Basic Salary")
    allowances = models.IntegerField("Allowance", default=0)
    deductions = models.IntegerField("Deduction", default=0)
    final_salary = models.IntegerField("Final Salary", default=0)
    generated_at = models.DateTimeField()

    def __str__(self):
        return f"{self.staff.user.get_full_name()}'s Salary"


class Allowance(models.Model):
    salary = models.ForeignKey(
        Salary, on_delete=models.CASCADE, related_name="salary_allowances")
    amount = models.FloatField("Amount")


class Deduction(models.Model):
    salary = models.ForeignKey(
        Salary, on_delete=models.CASCADE, related_name="salary_deductions")
    amount = models.FloatField("Amount")
