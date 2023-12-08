# Generated by Django 5.0 on 2023-12-08 02:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_transfer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transfer',
            name='owner',
        ),
        migrations.AddField(
            model_name='transfer',
            name='transmitter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='transmitter', to='app1.bank_account'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='app1.bank_account'),
        ),
    ]