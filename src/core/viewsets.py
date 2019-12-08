from rest_framework import viewsets, permissions
from .models import Contact
from .serializers import ContactSerializer
from .permissions import IsOwnerOrReadOnly


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        request = self.request
        serializer.save(user=1)

    # def create(self, request):
    #     request.data.user = 1
    #     return super().create(request)

    def get_queryset(self):
        user = self.request.user
        return Contact.objects.filter(user=user)
