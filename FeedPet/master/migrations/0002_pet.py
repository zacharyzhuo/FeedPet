# Generated by Django 2.2.7 on 2019-11-30 13:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('petClass', models.CharField(choices=[('Dog', '狗'), ('Cat', '貓')], max_length=3, null=True)),
                ('petType', models.CharField(max_length=20)),
                ('petName', models.CharField(max_length=20)),
                ('birthday', models.DateField()),
                ('weight', models.PositiveIntegerField()),
                ('ligation', models.BooleanField()),
                ('image', models.ImageField(upload_to='pets/')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
