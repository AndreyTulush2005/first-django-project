from django.db import models

# Create your models here.


class Advertisement(models.Model):
    title = models.CharField('Загаловок', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, если торг уместен')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"title={self.title}, description={self.description}, price={self.price}, auction={self.auction}"

    class Meta:
        db_table = 'Advertisement'