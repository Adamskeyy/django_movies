from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

AGE_CHOICES = (
    (7, '7'),
    (13, '13'),
    (16, '16'),
    (18, '18'),
    (21, '21')
)

class Genre(models.Model):
    name = models.CharField(max_length=20, unique=True)
    age_limit = models.IntegerField(null=True, blank=True, choices=AGE_CHOICES)

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)

    class Meta:
        unique_together = ('name', 'surname')

    def __str__(self):
        return f"{self.name} {self.surname}"
    

class Movie(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(
        null=True, validators=[MaxValueValidator(15), MinValueValidator(1)]
    )
    released = models.DateField()
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)
    director = models.ForeignKey(Director, null=True, on_delete=models.SET_NULL)

    class Meta:
        unique_together = ('title', 'released')

    def __str__(self):
        return f"{self.title} from {self.released}"
    