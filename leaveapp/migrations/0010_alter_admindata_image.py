# Generated by Django 4.0.5 on 2022-08-26 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaveapp', '0009_alter_admindata_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admindata',
            name='image',
            field=models.BinaryField(null=True),
        ),
    ]
