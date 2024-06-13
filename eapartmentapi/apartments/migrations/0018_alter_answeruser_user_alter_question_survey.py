# Generated by Django 5.0.4 on 2024-06-12 10:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0017_remove_survey_user_survey_user_create_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answeruser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='apartments.survey'),
        ),
    ]