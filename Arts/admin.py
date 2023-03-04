from django.contrib import admin
from . import models

admin.site.register(models.Hall)
admin.site.register(models.Painting)
admin.site.register(models.Chariot)
admin.site.register(models.Others)
admin.site.register(models.Holding)
admin.site.register(models.ArtStory)
admin.site.register(models.BorrowedCollection)
admin.site.register(models.PermanentCollection)
admin.site.register(models.Description)

class ChariotInline(admin.TabularInline):
    model = models.Chariot

class PaintingInline(admin.TabularInline):
    model = models.Painting

class OthersInline(admin.TabularInline):
    model = models.Others

class HoldingInline(admin.TabularInline):
    model = models.Holding

class BorrowedInline(admin.TabularInline):
    model = models.BorrowedCollection

class PermenantInline(admin.TabularInline):
    model = models.PermanentCollection

class HallInline(admin.TabularInline):
    model = models.Hall

class ArtStoryInline(admin.TabularInline):
    model = models.ArtStory

class ArtDescriptionInline(admin.TabularInline):
    model = models.Description


@admin.register(models.ArtObject)
class ArtObjectAdmin(admin.ModelAdmin):
    list_display = ['art_name','art_type','active','hall','description','story']
    inlines = [ChariotInline,PaintingInline,OthersInline,HoldingInline,BorrowedInline,PermenantInline,ArtStoryInline,ArtDescriptionInline]
    
  

 

# Register your models here.
