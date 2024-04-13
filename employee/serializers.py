from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Employee, Leave


class EmployeeSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Employee
        fields = ['employee', 'email_id', 'contact_number', 'role', 'username']

    def get_username(self, obj):
        return obj.employee.username


class LeaveSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Leave
        fields = [
            'start_date', 'end_date', 'Employee', 'reason', 'leave_status', 'username']

    def get_username(self, obj):
        return obj.employee.username
