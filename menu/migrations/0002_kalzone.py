# Generated by Django 5.0.2 on 2024-02-08 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kalzone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pasta', models.CharField(max_length=100)),
                ('flavor', models.CharField(max_length=100)),
            ],
        ),
    ]
