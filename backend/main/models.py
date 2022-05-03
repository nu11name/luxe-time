from django.db import models
from django.utils.safestring import mark_safe


class Manufacturer(models.Model):
    title = models.CharField('Title', max_length=256)
    slug = models.SlugField('Public Url', unique=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField('Title', max_length=256)
    slug = models.SlugField('Public Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Type(models.Model):
    title = models.CharField('Title', max_length=256)
    slug = models.SlugField('Public Url', unique=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    CONDITION_CHOICES = (
        ("new", "New"),
        ("used", "Used")
    )
    title = models.CharField('Title', max_length=256)
    brand = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True, blank=True)
    condition = models.CharField(max_length=120, choices=CONDITION_CHOICES, default="New")

    price = models.DecimalField('Price', max_digits=11, decimal_places=2)
    old_price = models.DecimalField('Old Price', max_digits=11, decimal_places=2, null=True, blank=True)
    image = models.ImageField('Image', upload_to='product-images')
    Description = models.TextField('Description_en', max_length=1000, null=True, blank=True)
    Description_ge = models.TextField('Description_ge', max_length=1000, null=True, blank=True)
    Description_ru = models.TextField('Description_ru', max_length=1000, null=True, blank=True)

    sold_out = models.BooleanField('Sold out', default=False)

    date_uploaded = models.DateTimeField(auto_now_add=True)
    position = models.IntegerField('Position', help_text='1 - higher priority ', null=True, blank=True)

    slug = models.SlugField('URL', unique=True, null=True, blank=True)

    is_sale = models.BooleanField('Is sale', null=True, blank=True, editable=False)

    views = models.PositiveIntegerField('Views', editable=False, default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('position', 'date_uploaded')

    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % self.image.url)

    def save(self, *args, **kwargs):
        if self.old_price:
            self.is_sale = True
        else:
            self.is_sale = False

        super(Product, self).save(*args, **kwargs)


class ProductImage(models.Model):
    image = models.ImageField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")


class SpecialOffer(models.Model):
    title = models.CharField('Title', max_length=256)
    slug = models.SlugField('Public Url', unique=True)

    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.title


class ProductDetails(models.Model):
    title_en = models.CharField('Title_en', max_length=256, null=True, blank=True)
    title_ge = models.CharField('Title_ge', max_length=256, null=True, blank=True)
    title_ru = models.CharField('Title_ru', max_length=256, null=True, blank=True)
    desc_en = models.CharField('Description_en', max_length=256, null=True, blank=True)
    desc_ge = models.CharField('Description_ge', max_length=256, null=True, blank=True)
    desc_ru = models.CharField('Description_ru', max_length=256, null=True, blank=True)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_desc")

    def __str__(self):
        return self.title_en