# Generated by Django 4.1.3 on 2022-11-06 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0)),
                ('time', models.DateTimeField(auto_now=True)),
                ('organization', models.CharField(blank=True, max_length=512)),
                ('description', models.CharField(blank=True, max_length=2056)),
                ('profit', models.BooleanField(default=False)),
                ('category', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='manager.category')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]