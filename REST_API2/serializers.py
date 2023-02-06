from rest_framework import serializers
from .models import employees


class employeesSerializer(serializers.ModelSerializer):
    firstname = serializers.CharField(max_length=15)
    lastname = serializers.CharField(max_length=10)
    Email = serializers.EmailField(max_length=254)
    phn_no = serializers.IntegerField()
    emp_id = serializers.IntegerField()

    class Meta:
        model = employees
        fields = ('__all__')
