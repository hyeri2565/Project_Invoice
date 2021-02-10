from django.shortcuts import render
from django.contrib.auth import authenticate, login
# Create your views here.

def index(request):
    return render(request,'index.html')
def loginTest(request):
    try:
        i_id=request.GET['id']
        i_pw=request.GET['pw']
        context={'id':i_id,'pw':i_pw}
    except context.DoesNotExist:
        context2={'error':1}
        return render(request, 'index.html',context2)
    else:
        return render(request,'login.html',context)

def login_view(request):
    if request.method=="POST":
        username=request.POST['name']
        password=request.POST['pw']
        user=authenticate(username=username,password=password)
        if user is not None:
            print('인증성공')
            login(request,user)
        else:
            print('인증실패')
    return render(request,'auth.html')
#실제 db안에있는 값을 입력하면 성공처리
#login(re,user)해주면 로그인된상태 ->표시해주는 작업들어가야함
# 로그인 성공상태 =>user.is_authenticated
