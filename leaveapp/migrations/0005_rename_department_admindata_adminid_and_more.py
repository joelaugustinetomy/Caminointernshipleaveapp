# Generated by Django 4.0.5 on 2022-08-26 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaveapp', '0004_admindata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admindata',
            old_name='department',
            new_name='adminid',
        ),
        migrations.RenameField(
            model_name='admindata',
            old_name='empid',
            new_name='dept',
        ),
        migrations.RemoveField(
            model_name='admindata',
            name='photo',
        ),
        migrations.AddField(
            model_name='admindata',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='filepath'),
        ),
    ]
