from django.db import models

# Create your models here.


class PublishingHouse(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    year_of_establishment = models.IntegerField()
    website = models.URLField()


class Book(models.Model):
    title = models.CharField(max_length=30)
    cover_image = models.ImageField(upload_to="cover_images/", null=True, blank=True)
    isbn = models.CharField(max_length=17)
    year_of_publishing = models.IntegerField()
    publishing_house = models.ForeignKey(PublishingHouse, on_delete=models.CASCADE)
    number_of_pages = models.IntegerField()
    dimensions = models.CharField(max_length=10)
    cover_type = models.CharField(max_length=2, choices=[("H", "Hard"), ("S", "Soft")])
    category = models.CharField(max_length=3, choices=[("R", "Romance"), ("T", "Thriller"), ("B", "Biography"), ("C", "Classic"), ("D", "Drama"), ("H", "Historical")])
    price = models.DecimalField(max_digits=6, decimal_places=2)
