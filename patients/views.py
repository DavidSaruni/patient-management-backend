
from rest_framework import viewsets
from .models import Patient, Vitals, VisitFormA, VisitFormB
from .serializers import (
    PatientSerializer,
    VitalsSerializer,
    VisitFormASerializer,
    VisitFormBSerializer,
)

# Create your views here.

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by('-registration_date')
    serializer_class = PatientSerializer


class VitalsViewSet(viewsets.ModelViewSet):
    queryset = Vitals.objects.all().order_by('-visit_date')
    serializer_class = VitalsSerializer


class VisitFormAViewSet(viewsets.ModelViewSet):
    queryset = VisitFormA.objects.all().order_by('-visit_date')
    serializer_class = VisitFormASerializer


class VisitFormBViewSet(viewsets.ModelViewSet):
    queryset = VisitFormB.objects.all().order_by('-visit_date')
    serializer_class = VisitFormBSerializer
