from rest_framework.viewsets import ModelViewSet
from ratings.models import Rating
from ratings.api.serializers import RatingSerializer

class RatingViewSet(ModelViewSet):
    serializer_class = RatingSerializer

    def get_queryset(self):
        return Rating.objects.all()
