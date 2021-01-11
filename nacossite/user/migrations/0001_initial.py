# Generated by Django 2.2.5 on 2020-12-29 17:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('org', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biodata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matric_number', models.CharField(max_length=16)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='org.Level')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='org.Session')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Biodata',
            },
        ),
    ]
