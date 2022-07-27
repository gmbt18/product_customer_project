# Generated by Django 4.0.4 on 2022-05-29 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crms_app', '0018_alter_authuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Product Manager'), (4, 'Reviewer'), (2, 'Customer'), (3, 'Customer Manager')], null=True),
        ),
    ]
