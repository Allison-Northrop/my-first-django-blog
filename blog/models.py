# All lines starting with from or import are lines that add some bits from other files. So instead of copying and pasting the same things in every file, we can include some parts with from ... import ....
from django.db import models
from django.utils import timezone

# Create your models here.

# this line below defines our model (object: post)
#models.Model means the post is a Django model, so Django knows that it should be saved in the database.
class Post(models.Model):
    author = models.ForeignKey('auth.User') #this is a link to another model
    title = models.CharField(max_length=200) #CharField means it's a string with a *limited* number of characters.
    text = models.TextField() #TextField string without limit of numbers
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self): #the publish method (saves the post to the database with the time stamp)
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
