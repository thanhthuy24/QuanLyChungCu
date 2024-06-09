# Generated by Django 5.0.4 on 2024-06-09 10:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0011_remove_choice_user_answer_answeruser_choice_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='user',
        ),
        migrations.AddField(
            model_name='survey',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]