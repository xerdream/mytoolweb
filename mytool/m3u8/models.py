from django.db import models


class M3U8Info(models.Model):
    url_text = models.CharField(max_length=512)
    up_date = models.DateTimeField("date created")

    def __str__(self) -> str:
        return self.url_text
