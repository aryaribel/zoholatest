# Generated by Django 4.2.3 on 2024-02-03 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Register_Login', '0010_company_payment_term'),
        ('Company_Staff', '0010_rename_customercontactperson_vendorcontactperson_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor_comments_table',
            name='login_details',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails'),
        ),
    ]