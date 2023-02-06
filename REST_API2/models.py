from django.db import models


class employees(models.Model):
    firstname = models.CharField(("enter your first name"), max_length=15)
    lastname = models.CharField(("enter your first name"), max_length=10)
    Email = models.EmailField(("enter your email"), max_length=254)
    phn_no = models.IntegerField(("enter your phone number"))
    emp_id = models.IntegerField()

    def _str_(self):
        return self.firstname
