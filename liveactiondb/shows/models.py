from __future__ import unicode_literals

from django.db import models


class Show(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    currently_origin = models.BooleanField(default=False)

class Episode(models.Model):
    show = models.ForeignKey('shows.Show')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
