from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.response import Response
from address.api.serializers import AddressSerializer
from address.models import Address


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Address.objects.all()

    def perform_destroy(self, instance):
        user = self.request.user
        if hasattr(instance, 'set_delete_user'):
            instance.set_delete_user(user)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
