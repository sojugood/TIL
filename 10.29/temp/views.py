from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Article, Comment
from .serializers import (
    ArticleSerializer,
    ArticleListSerializer,
    CommentSerializer
)


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        article = Article.objects.all()
        serializer = ArticleListSerializer(article, many=True)
        return Response(serializer.data)
    
    # 문제 2. Article 새 글 작성 코드 완성하기
    #        (201 status code 도 같이 응답 필요)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    # 문제 3. article 수정 동작 코드 완성하기
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    # 문제 4. article 삭제 동작 코드 완성하기
    #        (응답으로 {'msg': 'n번글 삭제'} 와 204 status code 전달필요)
    elif request.method == 'DELETE':
        n = article.pk
        article.delete()
        return Response({'msg': f'{n}번글 삭제'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def comment_list(request):
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)