# Generated by Django 3.1.4 on 2021-03-31 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0005_auto_20210328_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='imgae',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]