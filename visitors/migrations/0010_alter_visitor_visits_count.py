# Generated by Django 3.2.3 on 2021-10-21 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0009_rename_visits_count_visitorlog_visits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='visits_count',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
