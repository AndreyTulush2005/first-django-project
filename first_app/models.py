from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth import get_user_model

from django.urls import reverse

User = get_user_model()

# Create your models here.

class Advertisement(models.Model):
    title = models.CharField('Загаловок', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, если торг уместен')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='firstProject/')

    def get_absolute_url(self):
        return reverse('adv_detail', kwargs={'pk' : self.id})
    def __str__(self):
        return f"Advertisement(title={self.title}, description={self.description}, price={self.price}, auction={self.auction})"

    @admin.display(description='Дата создания')
    def created_at(self):
        if self.created_date.date() == timezone.now().date():
            created_time = self.created_date.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
            )

        return self.created_date.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description='Дата обновления')
    def update_at(self):
        if self.updated_date.date() == timezone.now().date():
            created_time = self.updated_date.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: yellow; font-weight: bold;">Сегодня в {}</span>', created_time
            )

        return self.updated_date.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description='Изображение')
    def imageAdmin(self):
        if self.image:
            return format_html(
                '<img src="{}" width="100px">', self.image.url
            )

    class Meta:
        db_table = 'Advertisement'