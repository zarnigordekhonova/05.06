# Generated by Django 5.0.6 on 2024-06-04 21:17

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharedclass',
            name='uu_id',
            field=models.UUIDField(default=uuid.UUID('aa454198-ce6a-4ac5-85e5-36bff69c632f'), editable=False, primary_key=True, serialize=False),
        ),
    ]
