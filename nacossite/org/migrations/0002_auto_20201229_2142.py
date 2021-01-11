# Generated by Django 2.2.5 on 2020-12-29 20:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('org', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=6)),
                ('description', models.TextField(default='')),
                ('instructor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='org.Level')),
            ],
        ),
        migrations.AddField(
            model_name='material',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='org.Course'),
            preserve_default=False,
        ),
    ]