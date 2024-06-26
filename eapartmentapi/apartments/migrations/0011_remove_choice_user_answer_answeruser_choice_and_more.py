# Generated by Django 5.0.4 on 2024-06-09 10:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0010_answeruser_choice_user_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='user_answer',
        ),
        migrations.AddField(
            model_name='answeruser',
            name='choice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apartments.choice'),
        ),
        migrations.AddField(
            model_name='answeruser',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apartments.question'),
        ),
    ]
