# Generated by Django 4.1.7 on 2023-03-07 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False, verbose_name='AGE')),
                ('age', models.CharField(max_length=20, verbose_name='age')),
            ],
            options={
                'db_table': 'age',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False, verbose_name='SEX_ABS')),
                ('gender', models.CharField(max_length=8, verbose_name='Sex')),
            ],
            options={
                'db_table': 'gender',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False, verbose_name='ASGS_2016')),
                ('region', models.CharField(max_length=64, verbose_name='Region')),
            ],
            options={
                'db_table': 'region',
            },
        ),
        migrations.CreateModel(
            name='RegionType',
            fields=[
                ('id', models.CharField(editable=False, max_length=4, primary_key=True, serialize=False, verbose_name='REGIONTYPE')),
                ('geography_level', models.CharField(max_length=32, verbose_name='Geography Level')),
            ],
            options={
                'db_table': 'region_type',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False, verbose_name='STATE')),
                ('state', models.CharField(max_length=32, verbose_name='State')),
            ],
            options={
                'db_table': 'state',
            },
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False, verbose_name='TIME')),
                ('year', models.CharField(max_length=6, verbose_name='Census year')),
            ],
            options={
                'db_table': 'year',
            },
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.BigIntegerField(verbose_name='Value')),
                ('flag_codes', models.CharField(max_length=8, verbose_name='Flag Codes')),
                ('flags', models.CharField(max_length=12, verbose_name='Flags')),
                ('age', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.age')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.gender')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.region')),
                ('regiontype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.regiontype')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.state')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.year')),
            ],
            options={
                'db_table': 'statistic',
            },
        ),
    ]
