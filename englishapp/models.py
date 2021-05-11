from django.db import models
from django.utils import timezone

class Word(models.Model):
    id = models.AutoField(primary_key=True)
    english = models.CharField('カテゴリ名',max_length=100,unique=True)
    created_at = models.DateTimeField('投稿日',default=timezone.now)

    def __str__(self):
        return self.english

class Answer(models.Model):
    question = models.TextField('問題')
    answer = models.TextField('答え')
    created_at = models.DateTimeField('投稿日',default=timezone.now)
    category = models.ForeignKey(Word, verbose_name='カテゴリ', on_delete=models.PROTECT)

    def __str__(self):
        return self.question