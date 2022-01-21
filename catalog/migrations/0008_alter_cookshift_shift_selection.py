# Generated by Django 4.0 on 2022-01-21 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_cook_cookshift_crew_crewshift_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cookshift',
            name='shift_selection',
            field=models.IntegerField(choices=[(1, 'Full cook shift and head cook'), (2, 'First half of cook shift'), (3, 'Second first half of cook shift'), (4, 'Second half of cook shift'), (5, 'Second second half of cook shift'), (6, 'Full cook shift')], default=1, verbose_name='Shift_Times'),
        ),
    ]
