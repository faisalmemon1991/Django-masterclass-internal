# Generated by Django 4.0 on 2022-04-23 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='location',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.location'),
        ),
    ]
