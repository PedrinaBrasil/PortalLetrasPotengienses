from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms
    
# Create your models here.
class Author(models.Model):
    name = models.CharField("Nome", max_length=255, blank=False)
    surname = models.CharField("Sobrenome", max_length=255, blank=False)
    citation = models.CharField("Citação", max_length=255, null=True, blank=True)
    bio = models.TextField("Biografia",  null=True, blank=True)
   
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    
    gender = models.CharField("Gênero", max_length=1, choices=GENDER_CHOICES)
   
    photo =  models.ImageField("Foto",upload_to="authors/", default="authors/no_image.png")

    
    created = models.DateTimeField("Cadastrado", auto_now_add=True)
    updated = models.DateTimeField("Atualizado", auto_now=True)
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural= 'Autores'
        ordering = ("-created","name",)
        
    def __str__(self):
        return self.citation


class Book(models.Model):
    title = models.CharField("Título", max_length=255, null=False, blank= False )
    edition = models.CharField("Edição", max_length=255, null=True, blank= True )
    volume = models.IntegerField("Volume", null=True, blank= True, default= 1)
    publised_date = models.DateField("Publicação", blank=True, null=True)
    summary = models.TextField("Sinopse", null=True, blank= True)
    created = models.DateTimeField("Cadastro", auto_now_add=True)
    updated = models.DateTimeField("Atualização", auto_now=True)
    authors = models.ManyToManyField(Author)
    
    cover =  models.ImageField("Capa", upload_to="covers/", default="covers/no_image.png")
    
    class Meta:
        verbose_name = 'Obra'
        verbose_name_plural= 'Obras'
        ordering = ("-created", "title")

    def __str__(self):
        return self.title
