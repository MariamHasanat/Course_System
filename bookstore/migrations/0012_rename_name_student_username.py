# Generated by Django 5.0.4 on 2024-05-28 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0011_student_is_active_student_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='username',
        ),
    ]