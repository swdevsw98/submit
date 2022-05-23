from turtle import pos
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from .models import *

# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def main(request):
    return render(request, 'main.html')

# 자게 html
def freeBoard(request):
    posts = Board.objects.filter().order_by('-date')
    return render(request, 'freeBoard.html', {'posts':posts})

def detail(request, post_id):
    post_detail = get_object_or_404(Board, pk=post_id)
    return render(request, 'freeBoardDetail.html', {'post_detail':post_detail})

def graduateBoard(request):
    return render(request, 'graduateBoard.html')

def create(request):
    if request.method =='POST':
        post = Board()
        post.title = request.POST['title']
        post.content = request.POST['text']
        post.file = request.FILES.get('file')
        post.user = request.user
        # post.date = timezone.now()
        post.save()
        return redirect('freeBoard')
    else:
        return render(request, 'freeBoard.html')
# 게시판 댓글 작성함수
def createComment(request, post_id):
    id = get_object_or_404(Board, pk=post_id)
    if request.method == 'POST':
        comment = Comment()
        comment.comment = request.POST['comment']
        comment.user = request.user
        comment.post = id
        comment.save()
        return redirect('detail', post_id)
    else:
        return render(request, 'freeBoard.html')