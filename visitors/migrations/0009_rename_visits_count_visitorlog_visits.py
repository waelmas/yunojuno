# Generated by Django 3.2.3 on 2021-10-21 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0008_rename_visits_visitorlog_visits_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitorlog',
            old_name='visits_count',
            new_name='visits',
        ),
    ]
