# Generated by Django 2.1.7 on 2019-03-15 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0007_appl'),
    ]

    operations = [
        migrations.AddField(
            model_name='appl',
            name='regno',
            field=models.CharField(default=1111, max_length=15),
            preserve_default=False,
        ),
    ]
