# Generated by Django 4.2.3 on 2023-11-06 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0002_rename_note_notemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notemodel',
            name='session',
            field=models.CharField(choices=[(1, '1st Semester'), (2, '2nd Semester')], max_length=50),
        ),
    ]
