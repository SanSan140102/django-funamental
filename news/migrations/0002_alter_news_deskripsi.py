# Generated by Django 5.0.1 on 2024-01-24 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='deskripsi',
            field=models.TextField(),
        ),
    ]