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