from core.models import BaseModelMixin
from django.db import models
from django.contrib.auth.models import User

class Comment(BaseModelMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
