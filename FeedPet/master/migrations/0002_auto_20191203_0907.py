# Generated by Django 2.2.7 on 2019-12-03 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
