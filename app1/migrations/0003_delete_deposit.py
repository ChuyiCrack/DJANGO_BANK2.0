# Generated by Django 5.0 on 2023-12-06 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_movement_date_alter_bank_account_movements'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Deposit',
        ),
    ]