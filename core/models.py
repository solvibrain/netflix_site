import uuid # using to create Universal unique Identifier for table.
from django.db import models

# Create your models here.
class Movie(models.Model):
    GENERE_CHOICES = [
        ('comedy','Comedy'),
        ('drama','Drama'),
        ('horror','Horror'),
        ('action','Action'),
        ('romantic','Romantic'),
        ('scifi','Sci-Fi'),
        ('thriller','Thriller'),
        ('fantasy','Fantasy'),
        ('animation','Animation'),
        ('documentary','Documentary'),
        ('crime','Crime'),
        ('western','Western'),
        ('mystery','Mystery'),
        ('biography','Biography'),
        ('history','History'),
        ('music','Music'),
        ('family','Family'),
        ('war','War'),
        ('sport','Sport'),
        ('musical','Musical'),
        ('adventure','Adventure'),
        ('film-noir','Film-Noir'),
        ('short','Short'),
        ('tv-movie','TV-Movie'),
        ('game-show','Game-Show'),
        ('talk-show','Talk-Show'),
        ('news','News'),
        ('reality-tv','Reality-TV'),
        ('talk-show','Talk-Show'),
        ('reality-tv','Reality-TV'),
        ('news','News'),
        ('reality-tv','Reality-TV')
    ]
        
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=255, choices=GENERE_CHOICES) # this will have a dropdown menu from the Genere List while uploading any movie form admin side.
    length = models.IntegerField() # length of the movie
    image_card = models.ImageField(upload_to='movies_images/')
    image_cover = models.ImageField(upload_to='movies_images/')
    video = models.FileField(upload_to="movies_videos/")# storing movie video at the specified location and retrieving also.
    movie_views = models.IntegerField(default=0)# storing data related to movie views in real time
    uu_id = models.UUIDField(default=uuid.uuid4)

    def __str__(self) -> str:
        return self.title