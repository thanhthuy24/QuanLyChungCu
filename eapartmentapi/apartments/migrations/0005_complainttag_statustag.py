# Generated by Django 5.0.4 on 2024-05-24 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0004_alter_carcard_created_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComplaintTag',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('apartments.tag',),
        ),
        migrations.CreateModel(
            name='StatusTag',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('apartments.tag',),
        ),
    ]