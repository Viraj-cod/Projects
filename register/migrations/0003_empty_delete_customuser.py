# Generated by Django 5.1.2 on 2024-11-30 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_rename_user_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='empty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ptr', models.CharField(default='hello', max_length=20, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Customuser',
        ),
    ]
