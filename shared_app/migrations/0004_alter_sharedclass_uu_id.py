# Generated by Django 5.0.6 on 2024-06-04 21:22

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared_app', '0003_alter_sharedclass_uu_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharedclass',
            name='uu_id',
            field=models.UUIDField(default=uuid.UUID('c25e67c5-749e-4321-ba77-fe515e513a55'), editable=False, primary_key=True, serialize=False),
        ),
    ]
