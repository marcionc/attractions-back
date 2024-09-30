from rest_framework.viewsets import ModelViewSet
from attractions.models import Attraction
from attractions.api.serializers import AttractionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class AttractionViewSet(ModelViewSet):
    serializer_class = AttractionSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Attraction.objects.all()

    # def perform_destroy(self, instance):
    #     user = self.request.user
    #     if hasattr(instance, 'set_delete_user'):
    #         instance.set_delete_user(user)
    #     instance.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
