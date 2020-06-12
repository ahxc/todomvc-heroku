from rest_framework.serializers import ModelSerializer

from .models import Todo

class TodoListSerializer(ModelSerializer):

    class Meta:
        model = Todo
        fields = [
        'id',
        'title',
        'completed',]