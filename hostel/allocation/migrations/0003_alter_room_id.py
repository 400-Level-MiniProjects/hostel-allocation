# Generated by Django 3.2.9 on 2022-02-17 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allocation', '0002_auto_20220217_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]
