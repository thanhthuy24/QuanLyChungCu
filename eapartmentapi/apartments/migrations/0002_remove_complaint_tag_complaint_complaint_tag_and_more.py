# Generated by Django 5.0.4 on 2024-05-16 13:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='tag',
        ),
        migrations.AddField(
            model_name='complaint',
            name='complaint_tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='complaint_tag', to='apartments.tag'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='status_tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='status_tag', to='apartments.tag'),
        ),
    ]
