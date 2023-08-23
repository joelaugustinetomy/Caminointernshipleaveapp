# Generated by Django 4.0.5 on 2022-07-29 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaveapp', '0002_leaveapply_endingdate_leaveapply_startingdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leavedetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.TextField(default='', max_length=15, null=True)),
                ('name', models.CharField(max_length=100)),
                ('empid', models.CharField(max_length=100)),
                ('startingdate', models.CharField(default='', max_length=100)),
                ('endingdate', models.CharField(default='', max_length=100)),
                ('reason', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]