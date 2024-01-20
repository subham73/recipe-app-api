"""
Views for the user API
"""
from rest_framework import generics

from user.sertializers import UserSerializer

class createUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer