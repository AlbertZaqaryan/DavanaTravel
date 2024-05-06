# Generated by Django 5.0.4 on 2024-05-06 06:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_project_delete_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Gallery name')),
                ('img', models.ImageField(upload_to='gallery', verbose_name='Gallery image')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proj', to='main.project')),
            ],
        ),
    ]