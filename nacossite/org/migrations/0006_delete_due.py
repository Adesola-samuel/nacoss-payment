# Generated by Django 3.1.4 on 2021-01-10 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0006_auto_20210110_1848'),
        ('org', '0005_due'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Due',
        ),
    ]
