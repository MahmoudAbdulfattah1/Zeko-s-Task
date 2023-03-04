from django.db import models

# Create your models here.
class Hall(models.Model):
    hall_name = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.hall_name

class ArtObject(models.Model):
    painting = 'P'
    chariot = 'C'
    others = 'O'
    holding = 'H'
    typeChoices = [
        (painting ,'Painting'),
        (chariot ,'Chariot'),
        (others ,'Others'),
        (holding ,'Holding'),
    ]
    borrowed = 'B'
    permenant = 'P'
    categoryChoices = [
        (borrowed,'Borrowed'),
        (permenant,'Permenant')
    ]
    art_name = models.CharField(max_length=255)
    art_type = models.CharField(max_length = 1 ,choices = typeChoices)
    category = models.CharField(max_length = 1, choices = categoryChoices)
    date_added = models.DateTimeField(auto_now_add= 1)
    last_modified = models.DateTimeField(auto_now= 1)
    active = models.BooleanField(default=1)
    hall = models.ForeignKey(Hall,on_delete=models.PROTECT,related_name='art_hall')

    def __str__(self) -> str:
        return self.art_name
    
    class Meta:
        ordering = ['art_name']

class Description(models.Model):
    item_description = models.TextField()
    art_object = models.OneToOneField(
        ArtObject, on_delete= models.CASCADE, primary_key= True , related_name= 'description')
    def __str__(self) -> str:
        return self.item_description
   
    
class ArtStory(models.Model):
    art = models.OneToOneField(ArtObject, on_delete= models.CASCADE, related_name='story',primary_key=1)
    story = models.TextField()
    def __str__(self) -> str:
        return self.story
   

class Chariot(models.Model):
    object_number = models.IntegerField()
    origin = models.CharField(max_length=255)
    chassis_number = models.IntegerField()
    chariot_object = models.OneToOneField(ArtObject,on_delete=models.CASCADE,related_name='chariot_art',primary_key=1)
   

class Painting(models.Model):
    atrist_name = models.CharField(max_length= 255)
    painting_object = models.OneToOneField(ArtObject, on_delete= models.CASCADE,related_name='painting_art',primary_key=1)
   

  

class Holding(models.Model):
    material = models.CharField(max_length=255)
    holding_object = models.OneToOneField(ArtObject,on_delete=models.CASCADE,related_name='holding_art',primary_key=1)
   


class Others(models.Model):
    origin = models.CharField(max_length=255)
    others_object = models.OneToOneField(ArtObject,on_delete=models.CASCADE,related_name='others_art',primary_key=1)
    

    

class BorrowedCollection(models.Model):
    date_borrowed = models.DateTimeField()
    date_returned = models.DateTimeField()
    borrowed_art = models.OneToOneField(ArtObject,on_delete=models.CASCADE,related_name='borrowed',primary_key=1)
    def __str__(self) -> str:
        return self.borrowed_art
  
   
    
class PermanentCollection(models.Model):
   date_aquired = models.DateTimeField()
   permenant_art = models.OneToOneField(ArtObject,on_delete=models.CASCADE,related_name='permenant',primary_key= 1)
   
  

