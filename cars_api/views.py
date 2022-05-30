from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from .models import Cars
from .serializers import CarsSerializer

class CarsListView(ListCreateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    permission_classes = (IsAuthenticated,)


class CarsDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)