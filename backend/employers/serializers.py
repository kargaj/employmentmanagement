from rest_framework import serializers

from .models import Employer


class EmployerSerializer(serializers.ModelSerializer):
    department_fullname = serializers.CharField(source='get_department_display', read_only=True)
    age = serializers.IntegerField(read_only=True)

    class Meta:
        model = Employer
        fields =  '__all__'
