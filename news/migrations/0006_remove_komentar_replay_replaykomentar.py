# Generated by Django 5.0.1 on 2024-02-01 10:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_komentar_replay'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='komentar',
            name='replay',
        ),
        migrations.CreateModel(
            name='ReplayKomentar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teks', models.TextField()),
                ('dibuat_pada', models.DateTimeField(auto_now_add=True)),
                ('komentar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.komentar')),
                ('penulis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
