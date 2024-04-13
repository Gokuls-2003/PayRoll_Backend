from django.contrib import admin
from .models import Salary, Allowance, Deduction

admin.site.register(Salary)
admin.site.register(Allowance)
admin.site.register(Deduction)
