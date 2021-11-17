from django.shortcuts import render
from rest_framework import authentication
from interviewtest.models import Interview
from rest_framework import generics, permissions
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import InterviewSerializer


def homepage(request):
    interviews = Interview.objects.all()
    return render(request, 'index.html', {'interviews': interviews})

class interviewList(generics.ListCreateAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

class interviewListPublic(generics.ListCreateAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
