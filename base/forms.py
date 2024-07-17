from django.forms import ModelForm
from .models import Topic, Task

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'description', 'deadline']

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['user', 'title', 'topic']