# Generated by Django 3.0.4 on 2020-03-23 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0002_auto_20200321_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=32, unique=True)),
                ('pwd', models.CharField(max_length=64)),
            ],
        ),
    ]
