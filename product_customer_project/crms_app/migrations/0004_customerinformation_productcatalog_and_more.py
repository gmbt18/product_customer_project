# Generated by Django 4.0.4 on 2022-05-24 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pcims_app', '0001_initial'),
        ('crms_app', '0003_alter_authuser_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerinformation',
            name='productCatalog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pcims_app.productcatalog'),
        ),
        migrations.AddField(
            model_name='customerreview',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pcims_app.product'),
        ),
        migrations.AddField(
            model_name='productcomplaint',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pcims_app.product'),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Product Manager'), (3, 'Customer Manager'), (4, 'Reviewer'), (2, 'Customer')], null=True),
        ),
    ]