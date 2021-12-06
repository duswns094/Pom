from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class LikeRec(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_rec')
    article = models.ForeignKey(Article,on_delete=models.CASCADE, related_name='like_rec')
    # 둘의 관계는 하나만 존재해야 함
    class Meta:
        unique_together = ('user', 'article')
