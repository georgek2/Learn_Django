from django.forms import ModelForm
from .models import *

class TopicForm(ModelForm):

    class Meta:

        model = Topic
        fields = '__all__'

