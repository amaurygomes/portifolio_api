from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.core.exceptions import ValidationError




    
class Technology(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    icon = models.TextField()
    startDate = models.DateField()
    


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Tech"
        verbose_name_plural = "Techs"
    

class Social(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    icon = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Link Contato"
        verbose_name_plural = "Links Contato"
    
class KnowTechs(models.Model):
    id = models.AutoField(primary_key=True)
    techs = models.ManyToManyField(Technology)
    

    def save(self, *args, **kwargs):
        if not self.pk and KnowTechs.objects.exists():
            raise ValueError('Já existe uma instancia de Knows.')
        return super(KnowTechs, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        raise ValueError('Estes dados não podem ser deletados.')
    
    class Meta:
        verbose_name = "Conhecimento"
        verbose_name_plural = "Conhecimentos"
    


def validate_pdf(value):
     if not value.name.endswith('.pdf'):
        raise ValidationError('Somente arquivos PDF são permitidos.')

class PageInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    introduction = CKEditor5Field()
    profilePicture = models.ImageField(upload_to='profilePicture/')
    cv = models.FileField(upload_to='files/', default='', validators=[validate_pdf])
    technologies = models.ManyToManyField(Technology)
    socials = models.ManyToManyField(Social)

    

    def save(self, *args, **kwargs):
        if not self.pk and PageInfo.objects.exists():
            raise ValueError('Já existe uma instancia de PageInfo.')
        return super(PageInfo, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        raise ValueError('Estes dados não podem ser deletados.')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Home"
        verbose_name_plural = "Home"
    

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    shortDescription = models.TextField()
    description = CKEditor5Field()
    githubUrl = models.URLField()
    liveProjectUrl = models.URLField()
    technologies = models.ManyToManyField(Technology)
    thumbnail = models.ImageField(upload_to='projectImages/')
    pagethumbnail = models.ImageField(upload_to='projectImages/')

    def __str__(self):
        return self.title


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

class Section(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='sections')
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='sectionImages/')

    def __str__(self):
        return self.name