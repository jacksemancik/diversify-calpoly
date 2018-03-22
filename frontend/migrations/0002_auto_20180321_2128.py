# Generated by Django 2.0.3 on 2018-03-21 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('text', models.TextField()),
                ('page', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Introduction',
        ),
    ]