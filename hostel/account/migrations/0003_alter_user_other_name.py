# Generated by Django 4.0 on 2021-12-28 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_other_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='other_name',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
    ]
