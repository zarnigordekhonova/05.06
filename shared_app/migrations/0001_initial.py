# Generated by Django 5.0.6 on 2024-06-04 21:15

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SharedClass',
            fields=[
                ('uu_id', models.UUIDField(default=uuid.UUID('df7b67af-b360-47ef-981c-4afdf36989fa'), editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'shared_class',
            },
        ),
    ]