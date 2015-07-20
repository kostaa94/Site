from django.db import models
from django.core.urlresolvers import reverse
from sorl.thumbnail.shortcuts import get_thumbnail


# Create your models here.
class Product(models.Model):
   category = models.CharField(max_length=100)
   name = models.CharField(max_length=200)
   price = models.FloatField()
   brand =models.CharField(max_length=100, default="Verana")
   image = models.ImageField(upload_to='static/bootstrap/itempics')

   def __str__(self):
        return self.name

   def get_thumbnail(self, size):
        img = self.image
        return unicode(get_thumbnail(img, '%(size)ix%(size)i' % {'size': size,}).url)

   def get_thumbnail_38(self):
        return self.get_thumbnail(38)

   def get_thumbnail_64(self):
        return self.get_thumbnail(64)

   def get_thumbnail_150(self):
        return self.get_thumbnail(150)

   def get_thumbnail_250(self):
        return self.get_thumbnail(250)

   def get_thumbnail_html(self):
        img_resize_url = self.get_thumbnail(100)
        html = '<a class="image-picker" href="%s"><img src="%s" alt="%s"/></a>'
        return html % (self.image.url, img_resize_url, self.title)




