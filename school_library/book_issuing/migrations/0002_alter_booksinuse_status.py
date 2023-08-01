# Generated by Django 4.2.3 on 2023-07-31 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_issuing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksinuse',
            name='status',
            field=models.TextField(choices=[('waiting for issuance', 'ожидание выдачи'), ('issued', 'выдана'), ('received', 'получена')], verbose_name='Статус книги'),
        ),
    ]