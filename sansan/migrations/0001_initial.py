# Generated by Django 5.0.1 on 2024-01-17 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='barang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_barang', models.CharField(max_length=100)),
                ('size_barang', models.IntegerField()),
                ('warna_barang', models.TextField()),
            ],
        ),
    ]