from django.utils.translation import gettext_lazy as _
from django.db import models


class Category(models.Model):
    title = models.CharField(
        verbose_name=_('title'),
        blank=False,
        null=False,
        unique=True,
        max_length=127,
    )
