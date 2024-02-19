from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from todo.models import Todo
from todo.serializers import TodoSerializer
from rest_framework.permissions import AllowAny


class TodoView(APIView):
    def get(self, request):
        print("all we know")
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        print(serializer)
        data = {
            "data": serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

    @method_decorator(csrf_exempt)
    def post(self, request):
        print(request.data)
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (AllowAny, )

    http_method_names = ['get', 'post']
