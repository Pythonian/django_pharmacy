import imp
from rest_framework import serializers

from ..models import Company, Medicine, Employee, Bill, BillDetails


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'license_no', 'address', 'contact_no', 'email', 'description']


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'

    def to_representation(self, instance):
        # Link to foreign key
        response = super().to_representation(instance)
        response['company'] = CompanySerializer(instance.company).data
        return response


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
