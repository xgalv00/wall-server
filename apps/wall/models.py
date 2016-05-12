from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from common.models import UniqueNameModel
from common.utils import storage_factory, image_path

image_storage = storage_factory(settings.IMAGE_ROOT, settings.IMAGE_URL)


class Post(UniqueNameModel):
    slug = models.SlugField(unique=True, editable=False)
    author = models.ForeignKey('auth.User', related_name='articles', verbose_name=_('author'))
    image = models.ImageField(upload_to=image_path, storage=image_storage, verbose_name=_('Article image'))
    text = models.TextField(verbose_name=_('text'))
    created = models.DateTimeField(verbose_name=_('created date time'), auto_now_add=True, editable=False)
    modified = models.DateTimeField(verbose_name=_('modified date time'), auto_now=True, editable=False)

    @models.permalink
    def get_absolute_url(self):
        return 'article-detail', (), {'slug': self.slug}
