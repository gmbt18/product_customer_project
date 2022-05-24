# Generated by Django 4.0.4 on 2022-05-22 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_authuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(2, 'Customer'), (1, 'Product Manager'), (3, 'Customer Manager'), (4, 'Reviewer')], null=True),
        ),
        migrations.AlterField(
            model_name='supplierproduct',
            name='isarchived',
            field=models.BooleanField(default=False),
        ),
    ]
