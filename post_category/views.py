from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from post_category.models import PostCategory
from post_category.serializers import PostCategorySerializer

@api_view(['GET'])
def post_categories(request):
    if request.method=='GET':
        postcategories=PostCategory.objects.all()
        serializer= PostCategorySerializer(postcategories, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def user_detail(request, pk):

    try:
        post_category=PostCategory.objects.get(pk=pk)
    except PostCategory.DoesNotExist:
        return Response(
            status=status.HTTP_404_NOT_FOUND
        )
    
    if request.method=='GET':
        serializer = PostCategorySerializer(post_category)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    if request.method=='PUT':
        serializer=PostCategorySerializer(post_category, data=request.data)
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
        serializer=PostCategorySerializer(post_category, data=request.data, partial=True)
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
        post_category.delete()
        return Response(
            'Deleted successfully',
            status=status.HTTP_202_ACCEPTED
        )