from django.shortcuts import render
from django.http import HttpResponse
from .models import Board
# Create your views here.
def home(request):
  boards = Board.objects.all()
  return render(
    request,"home.html",
    {"boards":boards}
    )
def board_topics(request,board_id):
  board = Board.objects.get(pk=board_id)
  return render(request,'topics.html',{'board':board})



def home(request):  
  

  boards = Board.objects.all()  
  # جلب جميع الكائنات (السجلات) من نموذج Board وتخزينها في المتغير boards

  return render(
    request, "home.html",
    {"boards": boards}
  )  
  


def board_topics(request, board_id):  
  # تعريف دالة view اسمها board_topics تستقبل كائن الطلب ومعرّف (ID) للوحة معينة

  board = Board.objects.get(pk=board_id)  
  # جلب كائن واحد من نموذج Board باستخدام المفتاح الأساسي (primary key) المرسل في board_id

  return render(request, 'topics.html', {'board': board})  
  