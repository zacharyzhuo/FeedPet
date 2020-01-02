# Generated by Django 2.2.7 on 2019-12-25 17:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favor_feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('fitem', models.CharField(max_length=10)),
                ('fmat', models.CharField(max_length=500)),
                ('fnut', models.CharField(max_length=100)),
                ('fusage1', models.CharField(max_length=50)),
                ('fusage2', models.CharField(max_length=50)),
                ('fusage3', models.CharField(max_length=50)),
                ('flegalname', models.CharField(max_length=20)),
                ('master_feed', models.ManyToManyField(related_name='master_feed', through='feed.Favor_feed', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water', models.PositiveIntegerField()),
                ('amount', models.PositiveIntegerField()),
                ('time', models.DateField(default=datetime.date.today)),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.Feed')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.Pet')),
            ],
        ),
        migrations.AddField(
            model_name='feed',
            name='pet_feed',
            field=models.ManyToManyField(related_name='pet_feed', through='feed.Record', to='master.Pet'),
        ),
        migrations.AddField(
            model_name='favor_feed',
            name='feed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.Feed'),
        ),
        migrations.AddField(
            model_name='favor_feed',
            name='master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
