from django.db import models
from categorias.models import Categoria
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
  id = models.AutoField(primary_key=True)
  titulo_post = models.CharField(max_length=255)
  autor_post = models.ForeignKey(User, on_delete=models.DO_NOTHING)
  data_post = models.DateTimeField(default=timezone.now)
  conteudo_post = models.TextField()
  excerto_post = models.TextField()
  categoria_post = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, blank=True)
  imagem_post = models.ImageField(upload_to='post_img/%Y/%m/%d',blank= True)
  publicado_post = models.BooleanField(default=False)
