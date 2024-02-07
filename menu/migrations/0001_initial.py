# Generated by Django 5.0.2 on 2024-02-07 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=100)),
                ('flavor', models.CharField(max_length=100)),
                ('border', models.BooleanField()),
                ('border_flavor', models.CharField(blank=True, max_length=100)),
                ('price', models.FloatField()),
                ('sweet', models.BooleanField(default=False)),
            ],
        ),
    ]