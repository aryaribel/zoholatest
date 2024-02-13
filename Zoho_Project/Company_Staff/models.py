from django.db import models

# Create your models here.
from Register_Login.models import LoginDetails,CompanyDetails,Company_Payment_Term

#---------------- models for zoho modules--------------------

#-----------------Arya E.R----------------------------------------

class Vendor(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True)
    first_name = models.CharField(max_length=255,null=True,blank=True)
    last_name = models.CharField(max_length=255,null=True,blank=True)
    vendor_display_name = models.CharField(max_length=255,null=True,blank=True)
    vendor_email = models.EmailField()
    mobile = models.CharField(max_length=15,default='')
    phone = models.CharField(max_length=15,default='')
    company_name = models.CharField(max_length=255,null=True,blank=True)
    skype_name_number = models.CharField(max_length=255,null=True,blank=True)
    designation = models.CharField(max_length=255,null=True,blank=True)
    department = models.CharField(max_length=255,null=True,blank=True)
    website = models.URLField(blank=True, null=True,default='')
    gst_treatment = models.CharField(max_length=255,null=True,blank=True)
    gst_number = models.CharField(max_length=20,null=True,blank=True)
    pan_number = models.CharField(max_length=20,null=True,blank=True)
    currency = models.CharField(max_length=3,null=True,blank=True)
    opening_balance_type = models.CharField(max_length=255,null=True,blank=True)
    opening_balance = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    current_balance = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    source_of_supply = models.CharField(max_length=255,null=True,blank=True)
    payment_term = models.ForeignKey(Company_Payment_Term, on_delete=models.SET_NULL,null=True,blank=True)
    billing_attention = models.CharField(max_length=255,null=True,blank=True)
    billing_address = models.TextField(null=True,blank=True)
    billing_city = models.CharField(max_length=255,null=True,blank=True)
    billing_state = models.CharField(max_length=255,null=True,blank=True)
    billing_country = models.CharField(max_length=255,null=True,blank=True)
    billing_pin_code = models.CharField(max_length=10,null=True,blank=True)
    billing_phone = models.CharField(max_length=15,null=True,blank=True)
    billing_fax = models.CharField(max_length=15,null=True,blank=True)
    shipping_attention = models.CharField(max_length=255,null=True,blank=True)
    shipping_address = models.TextField(null=True,blank=True)
    shipping_city = models.CharField(max_length=255,null=True,blank=True)
    shipping_state = models.CharField(max_length=255,null=True,blank=True)
    shipping_country = models.CharField(max_length=255,null=True,blank=True)
    shipping_pin_code = models.CharField(max_length=10,null=True,blank=True)
    shipping_phone = models.CharField(max_length=15,null=True,blank=True)
    shipping_fax = models.CharField(max_length=15,null=True,blank=True)
    remarks = models.TextField(null=True,blank=True)
    vendor_status = models.CharField(max_length=10,null=True,blank=True)
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE,null=True,blank=True)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class VendorContactPerson(models.Model):
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
    action = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return f"{self.vendor} - {self.action}"
    
class Vendor_remarks_table(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE,null=True)
    remarks=models.CharField(max_length=500)

class Vendor_comments_table(models.Model):
    login_details=models.ForeignKey(LoginDetails,on_delete=models.CASCADE,null=True)
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
    login_details=models.ForeignKey(LoginDetails,on_delete=models.CASCADE,null=True)
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE,null=True)
    title=models.TextField(max_length=200)
    document=models.FileField(upload_to='doc/')

#--------------------------------------end-----------------------------------------------------------