from django.db import models


# Create your models here

class Video(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.name
    


class bigpp(models.Model):
    ppicon=models.CharField(max_length=500)
    ppcolor=models.CharField(max_length=15,default="#EF476F")
    pptitle=models.CharField(max_length=75)
    ppdetails=models.TextField(max_length=200)

    class Meta():
        verbose_name_plural="bigpp"
    def __str__(self):
        return self.pptitle

class category(models.Model):
    Ctitle=models.CharField(max_length=200)
    Cdetails=models.CharField(max_length=200)
    Cimage=models.ImageField(upload_to='images/', default="https://images.unsplash.com/photo-1527683611643-4009f3a76197?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80")
    Cslug=models.CharField(max_length=100)

    class Meta():
        verbose_name_plural="categories"
    
    def __str__(self):
        return self.Ctitle


class series(models.Model):
    Stitle=models.CharField(max_length=200)
    Sdetails=models.CharField(max_length=200)
    Simage=models.ImageField(upload_to='images/', default="https://images.unsplash.com/photo-1527683611643-4009f3a76197?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80")
    Category=models.ForeignKey(category, default=1, verbose_name="category", on_delete=models.SET_DEFAULT)


    class Meta():
        verbose_name_plural="Series"
    
    def __str__(self):
        return self.Stitle

class skills(models.Model):
    title=models.CharField(max_length=200)
    details=models.TextField()
    image=models.ImageField(upload_to='images/', default="https://images.unsplash.com/photo-1527683611643-4009f3a76197?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80")
    Series=models.ForeignKey(series, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
    slug=models.CharField(max_length=100, default=1)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")
    sno=models.CharField(max_length=3)
    class Meta():
        verbose_name_plural="Skills"
    
    def __str__(self):
        return self.title