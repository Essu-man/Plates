from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=255)
    plate_range = models.CharField(max_length=255)
    barcode = models.ImageField(upload_to='barcodes/')
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Approved', 'Approved')])