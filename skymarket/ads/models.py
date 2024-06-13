from django.conf import settings
from django.db import models


class Ad(models.Model):

    image = models.ImageField(upload_to='media_files/', null=True, blank=True)
    title = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=500, null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE,
                               related_name='ads')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ("-created_at",)


class Comment(models.Model):

    text = models.CharField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                               related_name='comments')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ("-created_at",)
