# Generated by Django 3.0.4 on 2020-03-24 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0006_auto_20200324_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='condition',
            field=models.IntegerField(choices=[(0, '完成'), (1, '按时'), (2, '延期'), (3, '延误'), (4, '取消')], default=1, null=True),
        ),
    ]
