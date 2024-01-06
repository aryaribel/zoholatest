from django.db import models

# Create your models here.
from Register_Login.models import LoginDetails,CompanyDetails,PaymentTerms
from django.contrib.auth.models import User,auth

#---------------- models for zoho modules--------------------


class Vendor(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    vendor_display_name = models.CharField(max_length=255)
    vendor_email = models.EmailField()
    mobile = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    company_name = models.CharField(max_length=255)
    skype_name_number = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    website = models.URLField(blank=True, null=True)
    gst_treatment = models.CharField(max_length=255)
    gst_number = models.CharField(max_length=20)
    pan_number = models.CharField(max_length=20)
    currency = models.CharField(max_length=3)
    opening_balance_type = models.CharField(max_length=255)
    opening_balance = models.DecimalField(max_digits=10, decimal_places=2)
    current_balance = models.DecimalField(max_digits=10, decimal_places=2)
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2)
    source_of_supply = models.CharField(max_length=255)
    payment_term = models.ForeignKey(PaymentTerms, on_delete=models.CASCADE)
    billing_attention = models.CharField(max_length=255)
    billing_address = models.TextField()
    billing_city = models.CharField(max_length=255)
    billing_state = models.CharField(max_length=255)
    billing_country = models.CharField(max_length=255)
    billing_pin_code = models.CharField(max_length=10)
    billing_phone = models.CharField(max_length=15)
    billing_fax = models.CharField(max_length=15)
    shipping_attention = models.CharField(max_length=255)
    shipping_address = models.TextField()
    shipping_city = models.CharField(max_length=255)
    shipping_state = models.CharField(max_length=255)
    shipping_country = models.CharField(max_length=255)
    shipping_pin_code = models.CharField(max_length=10)
    shipping_phone = models.CharField(max_length=15)
    shipping_fax = models.CharField(max_length=15)
    remarks = models.TextField()
    vendor_status = models.CharField(max_length=10)
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE)

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
    

