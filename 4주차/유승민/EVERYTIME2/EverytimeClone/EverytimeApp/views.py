from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from django.core.paginator import Paginator

# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def main(request):
    return render(request, 'main.html')

# 자게 html
def freeBoard(request):
    posts = Board.objects.filter().order_by('-date')
    paginator = Paginator(posts, 3)
    page_num = request.GET.get('page')
    posts = paginator.get_page(page_num)
    return render(request, 'freeBoard.html', {'posts':posts})

def detail(request, post_id):
    post_detail = get_object_or_404(Board, pk=post_id)
    return render(request, 'freeBoardDetail.html', {'post_detail':post_detail})

def graduateBoard(request):
    return render(request, 'graduateBoard.html')
# 게시글 관련
def create(request):
    if request.method =='POST':
        post = Board()
        post.title = request.POST['title']
        post.content = request.POST['text']
        post.file = request.FILES.get('file')
        post.user = request.user
        post.date = datetime.now()
        post.save()
        return redirect('freeBoard')
    else:
        return render(request, 'freeBoard.html')

def update(request, post_id):
    post_detail = get_object_or_404(Board, pk=post_id)
    if request.method == 'POST':
        # post_detail = Board()
        post_detail.title = request.POST['title']
        post_detail.content = request.POST['content']
        if request.FILES.get('file'):
            post_detail.file = request.FILES.get('file')
        post_detail.user = request.user
        post_detail.date = datetime.now()
        post_detail.save()
        return redirect('/freeBoard/'+str(post_id), {'post_detail' : post_detail})
    else:
        return render(request, 'freeBoardUpdate.html', {'post_detail' : post_detail})

def delete(request, post_id):
    post = get_object_or_404(Board, pk=post_id)
    post.delete()
    return redirect('freeBoard')

# 댓글 관련
def createComment(request, post_id):
    id = get_object_or_404(Board, pk=post_id)
    if request.method == 'POST':
        comment = Comment()
        comment.comment = request.POST['comment']
        comment.user = request.user
        comment.post = id
        comment.date = datetime.now()
        comment.save()
        return redirect('detail', post_id)
    else:
        return render(request, 'freeBoard.html')

def updateComment(request, post_id, comment_id):
    post_detail = get_object_or_404(Board, pk=post_id)
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        # comment = Comment()
        comment.comment = request.POST['title']
        comment.user = request.user
        comment.post = post_detail
        comment.date = datetime.now()
        comment.save()
        return redirect('/freeBoard/'+str(post_id), {'post_detail' : post_detail})
    else:
        return render(request, 'freeBoardDetailUpdate.html', {'post_detail' : post_detail})

def deleteComment(request, post_id, comment_id):
    post_detail = get_object_or_404(Board, pk=post_id)
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('/freeBoard/'+str(post_id), {'post_detail' : post_detail})
