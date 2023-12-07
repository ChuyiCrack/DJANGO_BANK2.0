# Generated by Django 5.0 on 2023-12-06 19:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movement',
            name='Date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bank_account',
            name='movements',
            field=models.ManyToManyField(blank=True, to='app1.movement'),
        ),
    ]
