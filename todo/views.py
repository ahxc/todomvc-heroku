import simplejson as json

from django.views.generic import ListView
from rest_framework.generics import ListAPIView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from .models import Todo
from .serializers import TodoListSerializer


class IndexView(ListView):
    model = Todo
    template_name = 'index.html'
    # context_object_name = 'todo_list'


class IndexAPIView(ListAPIView):
    serializer_class = TodoListSerializer
    queryset = Todo.objects.all()


@csrf_exempt
def RecvDataView(request):

    if request.method == 'POST':
        Todo.objects.all().delete()
        todos = json.loads(request.body)

        for todo in todos:
            # 字典的取值方法没有'.'
            t = Todo(
                title = todo['title'],
                completed = todo['completed'])
            t.save()

        return HttpResponse(todos)    