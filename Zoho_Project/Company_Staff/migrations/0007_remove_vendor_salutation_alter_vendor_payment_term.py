# Generated by Django 4.2.3 on 2024-01-17 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Register_Login', '0009_paymenttermsupdates'),
        ('Company_Staff', '0006_alter_vendor_credit_limit_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='salutation',
        ),
        migrations.AlterField(
            model_name='vendor',
            name='payment_term',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Register_Login.paymentterms'),
        ),
    ]