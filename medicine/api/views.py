from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication

from ..models import Company

from .serializers import CompanySerializer
from medicine.api import serializers


# class CompanyViewSet(viewsets.ModelViewSet):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer

class CompanyViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True, context={'request': request})
        response_dict = {'error': False, 'message': 'List of all Companies', 'data': serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = CompanySerializer(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()

            # Save Medicines produced by a Company when creating the Company info
            # company_id = serializer.data['id']
            # company_details_list = []
            # for company_detail in request.data['company_details']:
            #     company_detail['company_id'] = company_id
            #     company_details_list.append(company_detail)
            # company_detail_serializer = CompanyDetailSerializer(data=company_details_list, many=True, context={'request': request})
            # company_detail_serializer.is_valid()
            # company_detail_serializer.save()

            dict_response = {'error': False, 'message': 'Company data saved successfully.'}
        except:
            dict_response = {'error': True, 'message': 'Error occured while saving data.'}
        return Response(dict_response)

    def retrieve(self, request, pk=None):
        queryset = Company.objects.all()
        company = get_object_or_404(queryset, pk=pk)
        serializer = CompanySerializer(company, context={'request': request})
        return Response({'error': False, 'message': 'Object data instance', 'data': serializer.data})

    def update(self, request, pk=None):
        try:
            queryset = Company.objects.all()
            company = get_object_or_404(queryset, pk=pk)
            serializer = CompanySerializer(company, data=request.data, context={'request': request})
            serializer.is_valid()
            serializer.save()
            dict_response = {'error': False, 'message': 'Company data updated successfully.'}
        except:
            dict_response = {'error': True, 'message': 'Error occured while updating data.'}
        return Response(dict_response)

company_list = CompanyViewSet.as_view({'get': 'list'})
company_create = CompanyViewSet.as_view({'post': 'create'})
company_update = CompanyViewSet.as_view({'put': 'update'})
