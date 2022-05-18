from django.shortcuts import render,HttpResponse,redirect,reverse
import re
# Create your views here.
from django.views import View
from myapp.models import MouldModel,LevelModel,UserModel
from myapp.forms import UserForm,ErollForm,LevelForm,MouldForm,StudentForm
from django.core.paginator import *
from django.db.models import Count

class EnrollView(View):
    def get(self,request):
        forms=ErollForm()
        return render(request,'enroll.html',{'form':forms})
    def post(self,reuqest):
        db=reuqest.POST.get('file')
        num=ErollForm(reuqest.POST)
        if num.is_valid():
            if num.cleaned_data['upwd']==num.cleaned_data['new_pwd']:
                UserModel.objects.create(uname=num.cleaned_data['uname'],upwd=num.cleaned_data['upwd'],role=db)
                return redirect(reverse('myapp:entry'))
            else:
                return HttpResponse('密码不一致')
        else:
            return HttpResponse('不合法')

class EntryView(View):
    def get(self,request):
        forms=UserForm()
        return render(request,'entry.html',{'form':forms})
    def post(self,request):
        db=UserForm(request.POST)
        if db.is_valid():
            uname=request.POST.get('uname')
            upwd=request.POST.get('upwd')
            num=UserModel.objects.filter(upwd=upwd,uname=uname).first()
            print('gggggggg')
            if num:
                request.session['username'] = num.id
                if num.role==1:

                    response = redirect(reverse('myapp:student'))
                    response.set_cookie('username', num.id, 1800)
                    return response
                if num.role==2:
                    response = redirect(reverse('myapp:treach'))
                    response.set_cookie('username', num.id, 1800)
                    return response
            else:
                return render(request, 'entry.html')
        else:
            return HttpResponse('数据不合法')

class StudentView(View):
    def get(self,request):
        forms=StudentForm()
        return render(request,'student.html',{'form':forms})
    def post(self,request):
        db=StudentForm(request.POST)
        a=request.POST.get('status')
        if db.is_valid():
            num=db.cleaned_data
            all=MouldModel.objects.create(status=a,stu_name=num['stu_name'],context=num['context'],createtime=num['createtime'],tid=num['tid'])
            if all:
                return redirect(reverse('myapp:student'))
            return HttpResponse('失败')
        else:
            return HttpResponse('数据不合法')



class TearchView(View):
    def get(self,request):
        number=request.GET.get('number',2)
        page=request.GET.get('page',1)
        search=request.GET.get('search')
        print(search,'--------------------------------------------------')
        forms=MouldModel.objects.all()
        form=MouldModel.objects.values('tid__tname').annotate(a=Count('id'))
        list_get=[]
        for i in form:
            if i.keys() not in list_get:
                list_get.append((i['tid__tname'],i['a']))
        print(list_get,'******************************************')
        if search:
            forms = MouldModel.objects.filter(tid_id=LevelModel.objects.filter(tname=search).first().id)
        num=Paginator(forms,number)
        show=num.get_page(page)
        list_db=show.object_list
        pre=0
        next=page
        if show.has_previous():
            pre=show.previous_page_number()
        if show.has_next():
            next=show.next_page_number()
        return render(request,'tearch.html',{
            'pre':pre,
            'next':next,
            'data':list_db,
            'number':number,
            'list_get':list_get
        })
        # return render(request,'tearch.html',{'form':forms})

class PermitView(View):
    def get(self,request):
        get_id=request.GET.get('id')
        status=request.GET.get('status')
        num=MouldModel.objects.filter(id=get_id)
        if num:
            num.update(status=status)
            return redirect(reverse('myapp:treach'))
        else:
            return HttpResponse('没有此人')