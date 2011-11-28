from django.forms import ModelForm
from cad.models import Usuario

class FormUsuario(ModelForm):
    class Meta:
        model = Usuario
        fields = ('nm_usuario','nivel','senha')