# Generated by Django 4.0.4 on 2022-06-01 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crms_app', '0028_alter_authuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(4, 'Reviewer'), (1, 'Product Manager'), (3, 'Customer Manager'), (2, 'Customer')], null=True),
        ),
    ]
