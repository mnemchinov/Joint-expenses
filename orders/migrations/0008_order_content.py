# Generated by Django 3.1.6 on 2021-02-10 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20210210_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='content',
            field=models.TextField(blank=True, default='', verbose_name='Содержимое'),
        ),
    ]
