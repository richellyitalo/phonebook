from rest_framework import viewsets, permissions
from .models import Contact
from .serializers import ContactSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import status
from rest_framework.response import Response
from rest_framework import filters


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
