from django.utils.translation import gettext_lazy as _
from django.db import models


class Product(models.Model):
    category = models.ForeignKey(
        verbose_name=_('category'),
        to='products.Category',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    title = models.CharField(
        verbose_name=_('title'),
        blank=False,
        null=False,
        unique=True,
        max_length=127,
    )
