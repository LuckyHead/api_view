from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from post.models import Post
from post.serializers import PostSerializer

def home_page(request):
    context={}
    return JsonResponse(context)

@api_view(['GET', 'POST'])
def posts(request):
    if request.method=='GET':
        posts=Post.objects.all()
        serializer= PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def posts_detail(request, pk):

    try:
        post=Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(
            status=status.HTTP_404_NOT_FOUND
        )
    
    if request.method=='GET':
        serializer = PostSerializer(post)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    if request.method=='PUT':
        serializer=PostSerializer(post, data=request.data)
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
        serializer=PostSerializer(post, data=request.data, partial=True)
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
        post.delete()
        return Response(
            'Deleted successfully',
            status=status.HTTP_202_ACCEPTED
        )
