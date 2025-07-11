from django.db import models



# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=28)
class Tag(models.Model):
    name=models.CharField(max_length=28,blank=True)

class Product (models.Model):
    name=models.CharField(max_length=50)
    stock=models.IntegerField()
    price=models.DecimalField(decimal_places=2,max_digits=6)
    description=models.TextField()
    category=models.ForeignKey(Category,null=True,on_delete=models.PROTECT)
    tags=models.ManyToManyField(Tag)
def __str__(self):
    return self.name
# class Membership(models.Model):
#     user=models.ForeignKey(User)

# class Farmer(models.Model):
#     membership=models.OneToOneField(Membership)
