# Generated by Django 5.0.4 on 2024-06-11 03:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0016_remove_phonenumber_ecabinet_ecabinet_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='user',
        ),
        migrations.AddField(
            model_name='survey',
            name='user_create',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_create', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='survey_user_done',
            field=models.ManyToManyField(related_name='survey_user_done', to='apartments.survey'),
        ),
    ]
