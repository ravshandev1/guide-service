# Generated by Django 3.2.18 on 2023-04-09 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guid', '0002_alter_booking_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='contraction',
            field=models.CharField(max_length=5),
        ),
    ]