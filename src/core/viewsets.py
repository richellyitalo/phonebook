from rest_framework import viewsets, permissions
from .models import Contact
from .serializers import ContactSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import status
from rest_framework.response import Response
from rest_framework import filters
from django.contrib.auth.models import User
from rest_framework.decorators import api_view


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'phonenumber', 'address', 'name']

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    # def create(self, request):
    #     request.data.user = 1
    #     return super().create(request)

    # def perform_create(self, serializer):
    #     kwargs = {
    #         'user': self.request.user  # Change 'user' to you model user field.
    #     }
    #     serializer.save(**kwargs)

    def get_queryset(self):
        user = self.request.user
        return Contact.objects.filter(user=user)


@api_view(['POST'])
def create_auth(request):
    serialized = UserSerializer(data=request.DATA)
    if serialized.is_valid():
        user = User.objects.create_user(
            serialized.init_data['email'],
            serialized.init_data['username'],
            serialized.init_data['password']
        )
        return Response(user, status=status.HTTP_201_CREATED)
    else:
        return Response('serialized._errors', status=status.HTTP_400_BAD_REQUEST)
