from django.views import View
from student.models import EntryModel
from student.forms import EntryForm,EnrollForm
from django.shortcuts import HttpResponse,render,redirect,reverse



class EntryView(View):
    def get(self,request):
        form=EntryForm()
        return render(request,'tryroll/entry.html',{'form':form})
    def post(self,request):
        db=EntryForm(request.POST)
        if db.is_valid():
            user=request.POST.get('user')
            password = request.POST.get('password')
            num=EntryModel.objects.filter(user=user,password=password).first()
            if num:
                request.session['username']=num.id
                response=redirect(reverse('student:select'))
                return response
            else:
                return  HttpResponse('登录失败')
        else:
            return HttpResponse(f'{db}')


class EnrollView(View):
    def get(self,request):
        form = EnrollForm()
        return render(request, 'tryroll/enroll.html', {'form': form})
    def post(self,request):
        db=EnrollForm(request.POST)
        if db.is_valid():
            db.save()
            return redirect(reverse('student:entry'))
        else:
            return HttpResponse('注册失败')