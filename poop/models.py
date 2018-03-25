from django.db import models

# Create your models here.

class dataset(models.Model):
    name = models.CharField(max_length=100,blank=True)
    dataset_image = models.ImageField(upload_to = 'images/datasets/newfiles', default='images/datasets/none.jpg')


    def __str__(self):
        return self.name
