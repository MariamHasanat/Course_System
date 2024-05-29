# Generated by Django 5.0.4 on 2024-05-29 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0016_remove_student_email_remove_student_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=90, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
