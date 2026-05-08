from django.db import models

class Memo(models.Model):
    title = models.CharField('タイトル',max_length = 100)
    content = models.TextField('本文')
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    def __str__(self):
        return self.title
