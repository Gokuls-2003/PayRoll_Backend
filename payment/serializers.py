from rest_framework import serializers
from .models import Salary, Allowance, Deduction
from employee.serializers import EmployeeSerializer


class SalarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Salary
        fields = [
            'employee', 'basic_salary', 'allowances', 'deductions', 'final_salary', 'generated_at']


class AllowanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Allowance
        fields = ['salary', 'amount']


class DeductionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deduction
        fields = ['salary', 'amount']
