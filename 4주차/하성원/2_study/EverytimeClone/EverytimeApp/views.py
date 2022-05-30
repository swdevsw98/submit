from django.shortcuts import get_object_or_404, render, redirect
from .models import Board, Comment
from django.utils import timezone
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
    #page에 해당하는 값 가져옴
    page_num = request.GET.get('page')
    posts = paginator.get_page(page_num)
    return render(request, 'freeBoard.html', {'posts' : posts})

def graduateBoard(request):
    return render(request, 'graduateBoard.html')

def create(request):
    if(request.method == 'POST'):
        post = Board()
        post.title = request.POST['title']
        post.content = request.POST['text']
        post.file = request.FILES.get('file')
        post.user = request.user
        post.date = timezone.now()
        post.save()
        return redirect('freeBoard')
    else:
        return render(request, 'freeBoard.html')

def detail(request, post_id):
    post_detail = get_object_or_404(Board, pk=post_id)
    return render(request, 'freeBoardDetail.html', {'post_detail':post_detail})


def createComment(request, post_id):
    if(request.method == 'POST'):
        comment = Comment()
        comment.comment = request.POST['comment']
        comment.user = request.user
        comment.post = get_object_or_404(Board, pk=post_id)
        comment.date = timezone.now()
        comment.save()
        return redirect('detail', post_id)
    else:
        return render(request, 'freeBoardDetail.html')

def update(request, post_id):
    post_detail = get_object_or_404(Board, pk=post_id)
    if (request.method == 'POST'):
        post_detail.title = request.POST['title']
        post_detail.content = request.POST['content']

        if request.FILES.get('file'):
            post_detail.file = request.FILES.get('file')

        post_detail.date = timezone.now()
        post_detail.save()
        return redirect('/freeBoard/'+str(post_id), {'post_detail':post_detail})
    else:
        return render(request, 'freeBoardUpdate.html', {'post_detail':post_detail})

def delete(request, post_id):
    post = get_object_or_404(Board, pk=post_id)
    post.delete()
    return redirect('freeBoard')

def updateComment(request, post_id, comment_id):
    post_detail = get_object_or_404(Board, pk=post_id)
    comment_detail = get_object_or_404(Comment, pk=comment_id)
    if (request.method == 'POST'):
        comment_detail.comment = request.POST['title']
        comment_detail.date = timezone.now()
        comment_detail.save()
        return redirect('/freeBoard/'+str(post_id), {'post_detail':post_detail})
    else:
        return render(request, 'freeBoardDetailUpdate.html', {'post_detail':post_detail})


def deleteComment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('detail', post_id)