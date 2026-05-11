from django.db import models
from django.contrib.auth.models import User


class Memo(models.Model):
    title = models.CharField('タイトル',max_length = 100)
    content = models.TextField('本文')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    def __str__(self):
        return self.title
