from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

from order.serializers import OrderSerializer
from order.models import Order
from client.models import Client

@permission_classes([AllowAny])
class CreateOrder(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([AllowAny])
class OrderUrgent(APIView):
        def get(self, request):
            users = CLient.objects.filter(type="PLATINO").values_list('id', flat=True)
            orders = Order.objects.filter(urgent=True,warehouse__isnull=False, date_supply__isnull=False,client__in=users)
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data)
