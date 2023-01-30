from django.forms import ModelForm
from .models import Comentario

class FormComentario(ModelForm):
  def clean(self):
    data = self.cleaned_data
    nome = data.get('nome_comentario')
    email = data.get('email_comentario')
    comentario = data.get('comentario')


    if len(nome) < 3:
      self.add_error(
        'nome_comentario', 'O nome deve ter mais de 5 caracteres'
        )

    if not email:
      self.add_error(
        'email_comentario',
      'O campo email deve ser preenchido!'
      )

  class Meta:
    model = Comentario
    fields = ('nome_comentario', 'email_comentario', 'comentario')