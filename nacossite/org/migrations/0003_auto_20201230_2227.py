# Generated by Django 3.1.4 on 2020-12-30 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0002_auto_20201229_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='description',
            field=models.TextField(default='', null=True),
        ),
    ]
