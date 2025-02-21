# Generated by Django 5.1.6 on 2025-02-20 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=40)),
                ('url', models.URLField(max_length=50)),
                ('content', models.ManyToManyField(related_name='movies', to='Info.watchlist')),
            ],
        ),
    ]
