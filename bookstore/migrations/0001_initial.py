# Generated by Django 5.0.6 on 2024-05-25 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90, null=True)),
                ('email', models.CharField(max_length=90, null=True)),
                ('age', models.FloatField(null=True)),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
