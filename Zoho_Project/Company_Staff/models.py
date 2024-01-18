from django.db import models

# Create your models here.
from Register_Login.models import LoginDetails,CompanyDetails,PaymentTerms
from django.contrib.auth.models import User,auth

#---------------- models for zoho modules--------------------


class Vendor(models.Model):
    title = models.CharField(max_length=255,default='')
    first_name = models.CharField(max_length=255,default='')
    last_name = models.CharField(max_length=255,default='')
    vendor_display_name = models.CharField(max_length=255,default='')
    vendor_email = models.EmailField()
    mobile = models.CharField(max_length=15,default='')
    phone = models.CharField(max_length=15,default='')
    company_name = models.CharField(max_length=255,default='')
    skype_name_number = models.CharField(max_length=255,default='')
    designation = models.CharField(max_length=255,default='')
    department = models.CharField(max_length=255,default='')
    website = models.URLField(blank=True, null=True,default='')
    gst_treatment = models.CharField(max_length=255,default='')
    gst_number = models.CharField(max_length=20,default='')
    pan_number = models.CharField(max_length=20,default='')
    currency = models.CharField(max_length=3,default='')
    opening_balance_type = models.CharField(max_length=255,default='')
    opening_balance = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    current_balance = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    source_of_supply = models.CharField(max_length=255,default='')
    payment_term = models.ForeignKey(PaymentTerms, on_delete=models.SET_NULL,null=True,blank=True)
    billing_attention = models.CharField(max_length=255,default='')
    billing_address = models.TextField()
    billing_city = models.CharField(max_length=255,default='')
    billing_state = models.CharField(max_length=255,default='')
    billing_country = models.CharField(max_length=255,default='')
    billing_pin_code = models.CharField(max_length=10,default='')
    billing_phone = models.CharField(max_length=15,default='')
    billing_fax = models.CharField(max_length=15,default='')
    shipping_attention = models.CharField(max_length=255,default='')
    shipping_address = models.TextField()
    shipping_city = models.CharField(max_length=255,default='')
    shipping_state = models.CharField(max_length=255,default='')
    shipping_country = models.CharField(max_length=255,default='')
    shipping_pin_code = models.CharField(max_length=10,default='')
    shipping_phone = models.CharField(max_length=15,default='')
    shipping_fax = models.CharField(max_length=15,default='')
    remarks = models.TextField()
    vendor_status = models.CharField(max_length=10,default='')
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE,null=True,blank=True)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    battention=models.CharField(max_length=100,default='')
    bstreet=models.CharField(max_length=100,default='')
    bcountry=models.CharField(max_length=100,default='')
    baddress=models.CharField(max_length=300,default='')
    bcity=models.CharField(max_length=100,default='')
    bstate=models.CharField(max_length=100,default='')
    bpin=models.CharField(max_length=100,default='')
    bzip=models.CharField(max_length=100,default='')
    bphone=models.CharField(max_length=100,default='')
    bfax=models.CharField(max_length=100,default='')
    sattention=models.CharField(max_length=100,default='')
    sstreet=models.CharField(max_length=100,default='')
    scountry=models.CharField(max_length=100,default='')
    saddress=models.CharField(max_length=300,default='')
    scity=models.CharField(max_length=100,default='')
    sstate=models.CharField(max_length=100,default='')
    szip=models.CharField(max_length=100,default='')
    spin=models.CharField(max_length=100,default='')
    sphone=models.CharField(max_length=100,default='')
    sfax=models.CharField(max_length=100,default='')
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class CustomerContactPerson(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    work_phone = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15)
    skype_name_number = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    department = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class VendorHistory(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateField()
    action = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.vendor} - {self.action}"
class Vendor_remarks_table(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE,null=True)
    remarks=models.CharField(max_length=500)    
class Vendor_comments_table(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE,null=True)
    comment=models.TextField(max_length=500)

class Vendor_mail_table(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE,null=True)
    mail_from=models.TextField(max_length=300)
    mail_to=models.TextField(max_length=300)
    subject=models.TextField(max_length=250)
    content=models.TextField(max_length=900)
    mail_date=models.DateTimeField(auto_now_add=True)

class Vendor_doc_upload_table(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE,null=True)
    title=models.TextField(max_length=200)
    document=models.FileField(upload_to='doc/')
