# Generated by Django 3.0.4 on 2020-03-24 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0005_project_statement'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='condition',
            field=models.IntegerField(choices=[(1, '按时'), (2, '延期'), (3, '延误'), (4, '取消')], default=1, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='remark',
            field=models.CharField(default='暂无', max_length=200, null=True),
        ),
    ]
