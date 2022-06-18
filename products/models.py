from django.db import models
from accounts.models import Firm
from config.settings import AUTH_USER_MODEL

User = AUTH_USER_MODEL
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=120)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='media/product_image/')
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE)
    viloyat = models.CharField(max_length=150)
    tuman = models.CharField(max_length=150)
    cost = models.IntegerField()
    coifsenti = models.IntegerField()
    about = models.TextField()

    def __str__(self):
        return self.name

    @property
    def get_product(self):
        title = self.buyproduct_set.all()

        total = sum([item.count for item in title])

        return total


class BuyProduct(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)

    def __str__(self):
        return self.product.name

