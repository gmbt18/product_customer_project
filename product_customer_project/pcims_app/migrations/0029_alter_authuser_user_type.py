# Generated by Django 4.0.4 on 2022-05-24 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0028_alter_authuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(2, 'Customer'), (4, 'Reviewer'), (3, 'Customer Manager'), (1, 'Product Manager')], null=True),
        ),
    ]
