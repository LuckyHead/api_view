from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from user.models import User
from user.serializers import UserSerializer


@api_view(['GET'])
def users(request):
    if request.method=='GET':
        users=User.objects.all()
        serializer= UserSerializer(users, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def user_detail(request, pk):

    try:
        user=User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(
            status=status.HTTP_404_NOT_FOUND
        )
    
    if request.method=='GET':
        serializer = UserSerializer(user)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    if request.method=='PUT':
        serializer=UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_202_ACCEPTED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_406_NOT_ACCEPTABLE
        )
    if request.method=='PATCH':
        serializer=UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_202_ACCEPTED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_406_NOT_ACCEPTABLE
        )
    elif request.method=='DELETE':
        user.delete()
        return Response(
            'Deleted successfully',
            status=status.HTTP_202_ACCEPTED
        )

