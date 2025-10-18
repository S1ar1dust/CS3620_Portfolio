from django.shortcuts import render
from rest_framework import viewsets
from BookAPI.models import BookData
from BookAPI.serializers import BookSerializer
from django.db.models import Q

# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer

class BooksWithRatingOver7(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(rating__gt=7).values()
    serializer_class = BookSerializer

class BooksWithRatingLessThan3(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(rating__lt=3).values()
    serializer_class = BookSerializer

class BookWithNameContainingTHE(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Q(name__contains="the") | Q(name__contains="The")).values()
    serializer_class = BookSerializer

class BookWithCategoryIsFiction(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category__contains="Fiction").values()
    serializer_class = BookSerializer

class BookWithCategoryIsFantasy(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category__contains="Fantasy").values()
    serializer_class = BookSerializer

class BookWithPastInDescription(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Q(name__contains="Past") | Q(name__contains="past")).values()
    serializer_class = BookSerializer

class BookWithWizardInDescription(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Q(name__contains="Wizard") | Q(name__contains="wizard")).values()
    serializer_class = BookSerializer

class BookWithPersonInDescription(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Q(name__contains="Person") | Q(name__contains="person")).values()
    serializer_class = BookSerializer

class BookWithBelieveInDescription(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Q(name__contains="Believe") | Q(name__contains="believe")).values()
    serializer_class = BookSerializer

class BookWithTaleInDescription(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Q(name__contains="Tale") | Q(name__contains="tale")).values()
    serializer_class = BookSerializer
