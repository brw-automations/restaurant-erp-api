# Generated by Django 4.2.5 on 2023-10-01 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_order_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='table',
            field=models.ManyToManyField(blank=True, null=True, to='core.table'),
        ),
    ]
