# Generated by Django 4.0 on 2022-01-19 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_remove_workchart_slot_day_of_week_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cook',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('mid_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CookShift',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('shift_selection', models.IntegerField(choices=[(1, 'Full cook shift'), (2, 'First half of cook shift'), (3, 'Second half of cook shift')], default=1, verbose_name='Shift_Times')),
                ('is_head_cook', models.BooleanField()),
                ('cook_obj', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.cook')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.member')),
            ],
        ),
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CrewShift',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_pic', models.BooleanField()),
                ('crew_obj', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.crew')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.member')),
            ],
        ),
        migrations.RemoveField(
            model_name='meal',
            name='cook_required_members',
        ),
        migrations.RemoveField(
            model_name='meal',
            name='crew_required_members',
        ),
        migrations.AlterField(
            model_name='meal',
            name='day_of_week',
            field=models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], default=1, verbose_name='Day_Choices'),
        ),
        migrations.DeleteModel(
            name='Workchart_slot',
        ),
        migrations.AddField(
            model_name='crew',
            name='pic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.crewshift'),
        ),
        migrations.AddField(
            model_name='cook',
            name='head_cook',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.cookshift'),
        ),
        migrations.AddField(
            model_name='meal',
            name='cook',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.cook'),
        ),
        migrations.AddField(
            model_name='meal',
            name='crew',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.crew'),
        ),
    ]
