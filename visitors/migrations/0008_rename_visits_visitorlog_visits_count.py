# Generated by Django 3.2.3 on 2021-10-21 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0007_visitorlog_max_visits'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitorlog',
            old_name='visits',
            new_name='visits_count',
        ),
    ]
