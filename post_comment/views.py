from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from post_comment.models import PostComment
from post_comment.serializers import PostCommentSerializer

@api_view(['GET', 'POST'])
def postcomment(request):
    if request.method=='GET':
        post_comments=PostComment.objects.all()
        serializer= PostCommentSerializer(post_comments, many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=PostCommentSerializer(data=request.data)
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
def post_comment_detail(request, pk):
    try:
        post_comment=PostComment.objects.get(pk=pk)
    except PostComment.DoesNotExist:
        return Response(
            status=status.HTTP_404_NOT_FOUND
        )
    if request.method=='GET':
        serializer = PostCommentSerializer(post_comment)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    if request.method=='PUT':
        serializer=PostCommentSerializer(post_comment, data=request.data)
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
        serializer=PostCommentSerializer(post_comment, data=request.data, partial=True)
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
        post_comment.delete()
        return Response(
            'Deleted successfully',
            status=status.HTTP_202_ACCEPTED
        )
