from django.db import models
from django.utils.translation import ugettext_lazy as _


class UniqueNameModel(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=256, unique=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name

