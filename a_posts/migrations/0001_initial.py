# Generated by Django 5.1.4 on 2024-12-21 09:22

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(max_length=500)),
                ('image', models.URLField(max_length=500)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=100, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
