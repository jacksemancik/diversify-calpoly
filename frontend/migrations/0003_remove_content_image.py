# Generated by Django 2.0.3 on 2018-03-21 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_auto_20180321_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='image',
        ),
    ]