# Generated by Django 3.0.4 on 2020-03-27 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0012_task_statement'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='persontotask',
            unique_together={('task', 'person')},
        ),
    ]
