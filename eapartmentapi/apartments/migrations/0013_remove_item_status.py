# Generated by Django 5.0.4 on 2024-06-10 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0012_remove_survey_user_survey_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='status',
        ),
    ]
