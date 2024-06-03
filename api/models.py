from django.db import models


    
class Technology(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    icon = models.TextField()
    startDate = models.DateField()
    


    def __str__(self):
        return self.name
    

class Social(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    icon = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.name
    
class KnowTechs(models.Model):
    techs = models.ManyToManyField(Technology)

    def save(self, *args, **kwargs):
        if not self.pk and KnowTechs.objects.exists():
            raise ValueError('Já existe uma instancia de PageInfo.')
        return super(KnowTechs, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        raise ValueError('Estes dados não podem ser deletados.')
    

class PageInfo(models.Model):
    slug = models.SlugField('home')
    name = models.CharField(max_length=100)
    introduction = models.TextField()
    profilePicture = models.ImageField(upload_to='profilePicture/')
    technologies = models.ManyToManyField(Technology)
    socials = models.ManyToManyField(Social)

    
    def save(self, *args, **kwargs):
        if not self.pk and PageInfo.objects.exists():
            raise ValueError('Já existe uma instancia de PageInfo.')
        return super(PageInfo, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        raise ValueError('Estes dados não podem ser deletados.')

    def __str__(self):
        return self.slug