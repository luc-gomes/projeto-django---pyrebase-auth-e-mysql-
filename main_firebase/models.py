from django.db import models
#https://docs.djangoproject.com/en/4.2/ref/models/fields/
#https://docs.djangoproject.com/en/4.2/topics/db/models/
# -- fk
#https://docs.djangoproject.com/en/4.2/topics/db/examples/many_to_one/

class SearchAutores(models.Model):
    codigo_autor = models.CharField(max_length=255, primary_key=True)
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=30)
    email =models.CharField(max_length=60)

    class Meta:
        db_table = "autores"


class SearchConteudos(models.Model):
    codigo_pb = models.CharField(max_length=255, primary_key=True)
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    texto =models.CharField(max_length=5000)
    #data_pub = models.DateTimeField(auto_now_add=True, blank=True )
    visibilidade = models.BooleanField(default= True)
    codigo_autor =  models.ForeignKey(SearchAutores, on_delete = models.CASCADE)

    class Meta:
        db_table = "conteudos"