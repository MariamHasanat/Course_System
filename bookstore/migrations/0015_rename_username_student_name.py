# Generated by Django 5.0.4 on 2024-05-29 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0014_student_email_student_password_student_username_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='username',
            new_name='name',
        ),
    ]