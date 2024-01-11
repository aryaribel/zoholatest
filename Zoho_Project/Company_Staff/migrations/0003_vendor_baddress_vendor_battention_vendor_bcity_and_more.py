# Generated by Django 4.2.3 on 2024-01-11 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Register_Login', '0009_paymenttermsupdates'),
        ('Company_Staff', '0002_alter_customercontactperson_company_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='baddress',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='vendor',
            name='battention',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='vendor',
            name='bcity',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='vendor',
            name='bcountry',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='vendor',
            name='bfax',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='vendor',
            name='bphone',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='vendor',
            name='bpin',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='vendor',
            name='bstate',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='vendor',
            name='bstreet',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='vendor',
            name='bzip',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='vendor',
            name='saddress',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='vendor',
            name='salutation',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='sattention',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='vendor',
            name='scity',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='vendor',
            name='scountry',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='vendor',
            name='sfax',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='vendor',
            name='sphone',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='vendor',
            name='spin',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='vendor',
            name='sstate',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='vendor',
            name='sstreet',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='vendor',
            name='szip',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.CreateModel(
            name='Vendor_remarks_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarks', models.CharField(max_length=500)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor_mail_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_from', models.TextField(max_length=300)),
                ('mail_to', models.TextField(max_length=300)),
                ('subject', models.TextField(max_length=250)),
                ('content', models.TextField(max_length=900)),
                ('mail_date', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor_doc_upload_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200)),
                ('document', models.FileField(upload_to='doc/')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor_comments_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=500)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.vendor')),
            ],
        ),
    ]