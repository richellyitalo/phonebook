from rest_framework import viewsets, permissions
from .models import Contact
from .serializers import ContactSerializer
from .permissions import IsOwnerOrReadOnly


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def create(self, request):
        print('criar')
        pass

    def get_queryset(self):
        user = self.request.user
        return Contact.objects.filter(user=user)
