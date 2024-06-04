# Generated by Django 5.0.6 on 2024-06-04 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followers',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='followers',
            name='phone',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]