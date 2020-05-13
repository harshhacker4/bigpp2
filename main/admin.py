from django.contrib import admin
from django.db import models
from .models import skills,category,series, bigpp, Video
from tinymce.widgets import TinyMCE
# Register your models here.

class Vsets(admin.ModelAdmin):
    fieldsets=[("Video Name",{"fields":["name"]}),
               ("Source",{"fields":["videofile"]}),]
               
  
admin.site.register(Video, Vsets)

class ppsets(admin.ModelAdmin):
    fieldsets=[("Image Class",{"fields":["ppicon"]}),
               ("Title",{"fields":["pptitle"]}),
               ("Image Color",{"fields":["ppcolor"]}),
               ("Content",{"fields":["ppdetails"]})]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(bigpp, ppsets)

class catsets(admin.ModelAdmin):
    fieldsets=[("Category",{"fields":["Ctitle"]}),
               ("Summary",{"fields":["Cdetails", "Cimage"]}),
               ("Slug(expected URL)",{"fields":["Cslug"]}),]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(category, catsets)

class sersets(admin.ModelAdmin):
    fieldsets=[("Series",{"fields":["Stitle"]}),
               ("Summary",{"fields":["Sdetails", "Simage"]}),
               ("Category",{"fields":["Category"]}),]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(series, sersets)



class skillsets(admin.ModelAdmin):
    fieldsets = [("Title", {"fields": ["title"]}),
                 ("Content", {"fields": ["details", "image"]}),
                 ("Series", {"fields":["Series"]}),
                 ("URL", {"fields": ["slug"]}),
                 ("Part Number", {"fields": ["sno"]}),]
    
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


admin.site.register(skills, skillsets)

