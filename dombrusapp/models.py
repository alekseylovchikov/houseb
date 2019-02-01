from django.db import models
from datetime import datetime
from django.utils.translation import ugettext as _
from .choises import TYPES


class Project(models.Model):
    # TYPES = (
    #     ('Br', 'Брусовые'),
    #     ('Ka', 'Каркасные'),
    #     ('Ba', 'Бани'),
    # )
    # title = models.CharField(max_length=200)
    title = models.CharField(_('Название'), max_length=200)
    description = models.TextField(_('Описание'), blank=True)
    size = models.CharField(_('Размер'), max_length=200)
    price = models.IntegerField(_('Цена'))
    type = models.CharField(_('Тип'), max_length=2, choices=TYPES)
    photo_1 = models.ImageField(_('Главное фото'), upload_to='photos/%Y/%m/%d/', blank=False)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(_('Опубликовано'), default=True)
    is_main_page = models.BooleanField(_('На главной'), default=False)
    project_date = models.DateTimeField(_('Дата публикации'), default=datetime.now, blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    title = models.CharField(_('Название'), max_length=200, default='Пример: телефон')
    value = models.CharField(_('Значение'), max_length=200, default='Пример: +7 555 123-12-12')

    def __str__(self):
        return self.title
