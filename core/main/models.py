from django.db import models

# Create your models here.

class Fav(models.Model):

    icon = models.ImageField('Fav icon', upload_to='Logos')

    def __str__(self):
        return 'Home Favicon'
    
class Logo(models.Model):

    img = models.ImageField('Logo image', upload_to='Logos')

    def __str__(self):
        return 'Home Logo'

class HomeBgInfo(models.Model):

    static_text = models.CharField('HomeBgInfo text static', max_length=50)
    dinamic_text1 = models.CharField('HomeBgInfo text1 dinamic', max_length=50)
    dinamic_text2 = models.CharField('HomeBgInfo text2 dinamic', max_length=50)
    dinamic_text3 = models.CharField('HomeBgInfo text3 dinamic', max_length=50)
    about = models.TextField('HomeBgInfo')
    button_name = models.CharField('HomeBgInfo button name', max_length=20)

    def __str__(self):
        return f'{self.static_text}'
    

class About(models.Model):

    text1 = models.TextField('About text1')
    text2 = models.TextField('About text2')
    text3 = models.TextField('About text3')
    text4 = models.CharField('About text4', max_length=50)
    img = models.ImageField('About image', upload_to='about', blank=True)

    def __str__(self):
        return 'About section info'
    
class Project(models.Model):

    image = models.ImageField('Project image', upload_to='projects')
    name1 = models.CharField('Project name1', max_length=50)
    name2 = models.CharField('Project name2', max_length=50)
    text1 = models.TextField('Project text1')
    text2 = models.TextField('Project text2')

    def __str__(self):
        return self.name1

class Gallery(models.Model):

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='proj')
    name = models.CharField('Gallery name', max_length=60)
    img = models.ImageField('Gallery image', upload_to='gallery')

    def __str__(self):
        return self.name
    
