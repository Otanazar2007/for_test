# Generated by Django 5.1.3 on 2024-12-06 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('this_is_app', '0005_bankcart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankcart',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
