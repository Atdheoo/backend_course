from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

from .models import Order
from .serializers import OrderSerializer

from django.core.mail import send_mail
from backend.settings import EMAIL_USER_HOST

logger = logging.getLogger(__name__)

class OrderView(APIView):
    def get(self, request):
        try:
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)
            return Response({
                'data': serializer.data,
                'message': "Orders Data Fetched Successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error fetching orders: {str(e)}")
            return Response({
                'data': {},
                'message': "Something went wrong while fetching the data"
            }, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            data = request.data
            serializer = OrderSerializer(data=data)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': "Validation error"
                }, status=status.HTTP_400_BAD_REQUEST)
            
            subject = "New Order is Placed"
            message = "Dear Customer" + " " + data['customer_name'] + " Your order is placed now. Thanks for your order."
            email = data['customer_email']
            recipient_list = [email]
            send_mail(subject, message, EMAIL_USER_HOST, recipient_list, fail_silently=True)
            serializer.save()

            return Response({
                'data': serializer.data,
                'message': "New order created successfully"
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(f"Error creating order: {str(e)}")
            return Response({
                'data': {},
                'message': "Something went wrong while creating the order"
            }, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:
            data = request.data
            order_instance = get_object_or_404(Order, id=data.get('id'))
            serializer = OrderSerializer(order_instance, data=data, partial=True)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': "Validation error"
                }, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()

            return Response({
                'data': serializer.data,
                'message': "Order updated successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error updating order: {str(e)}")
            return Response({
                'data': {},
                'message': "Something went wrong while updating the order"
            }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            data = request.data
            order_instance = get_object_or_404(Order, id=data.get('id'))
            order_instance.delete()
            return Response({
                'data': {},
                'message': "Order deleted successfully"
            }, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            logger.error(f"Error deleting order: {str(e)}")
            return Response({
                'data': {},
                'message': "Something went wrong while deleting the order"
            }, status=status.HTTP_400_BAD_REQUEST)
