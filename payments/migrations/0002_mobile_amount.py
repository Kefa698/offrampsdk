# Generated by Django 4.2.7 on 2023-11-15 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobile',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=11),
        ),
    ]