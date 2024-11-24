from rest_framework import serializers

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    department_fullname = serializers.CharField(source='get_department_display', read_only=True)
    age = serializers.IntegerField(read_only=True)

    class Meta:
        model = Employee
        fields =  '__all__'
