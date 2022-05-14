from django.views import View
from student.models import StudentModel,ClassModel
from student.forms import StudentForm
from django.shortcuts import HttpResponse,render,redirect,reverse
from django.core.paginator import *

class SelectView(View):
    def get(self,request):
        number=request.GET.get('number',2)
        page = request.GET.get('page',1)
        sname=request.GET.get('sname')
        print('fffff',sname)
        garde=request.GET.get('garde')
        if not sname or sname=='None':
            print('_________')
            obj=StudentModel.objects.all()
        else:
            print('@@@@@@@@@')
            obj=StudentModel.objects.filter(name=sname)
            print('yyyyyy',obj)
        if (not garde or garde=='None') and (not sname or sname=='None'):
            obj=StudentModel.objects.all()
            print('__________rrrrr')
        else:
            print('ooooooooo')
            b=ClassModel.objects.filter(id=garde)
            print('fffff',b)
            obj = obj.filter(cls=ClassModel.objects.filter(id=garde))
            print('hhhhhhhh',obj)
        link=Paginator(obj,number)
        link_read=link.get_page(page)
        link_db=link_read.object_list
        pre=1
        next=page
        if link_read.has_previous():
            pre=link_read.previous_page_number()
        if link_read.has_next():
            next=link_read.next_page_number()
        return render(request,'all/select.html',{
            'pre':pre,
            'next':next,
            'data':link_db,
            'number':number,
            'page':page,
            'sname':sname,
            'garde':garde,
        })


class InsertView(View):
    def get(self,request):
        form=StudentForm()
        return render(request,'all/insert.html',{'form':form})
    def post(self,request):
        db=StudentForm(request.POST)
        if db.is_valid():
            db.save()
            return redirect(reverse('student:select'))
        else:
            return HttpResponse('插入失败')


class DeleteView(View):
    def get(self,request):
        delete_id=request.GET.get('id')
        delete_db=StudentModel.objects.filter(id=delete_id).first().delete()
        if delete_db:
            return redirect(reverse('student:select'))
        else:
            return HttpResponse('删除失败')


class UpdateView(View):
    def get(self,request):
        update_id=request.GET.get('id')
        update_db=StudentModel.objects.filter(id=update_id).first()
        form=StudentForm(instance=update_db)
        return render(request,'all/update.html',{'form':form,'id':update_id})
    def post(self,request):
        post_id=request.POST.get('id')
        num=StudentForm(request.POST)
        if num.is_valid():
            StudentModel.objects.filter(id=post_id).update(**num.cleaned_data)
            return redirect(reverse('student:select'))
        else:
            return HttpResponse('修改失败')

class OutView(View):
    def get(self,request):
        request.session.clear()
        return redirect(reverse('student:entry'))