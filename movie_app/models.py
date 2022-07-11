from django.db import models
from django.urls import reverse
from django.utils.text import slugify

	
class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True)
    budget= models.IntegerField(default=10000000)
    slug= models.SlugField(default='', null=False)
    #director = models.ForeignKey('Director', on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('one_movie', args=[self.id])

    def __str__(self):
        return f'{self.name} - {self.rating} %'
    

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    director_email = models.EmailField(default='sugar_daddy@gmail.com')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

    
