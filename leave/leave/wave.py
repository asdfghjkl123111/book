from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect,reverse

class Wave(MiddlewareMixin):
    def process_request(self,request):
        a=request.path
        if a not in ['/myapp/entry/','/myapp/enroll/']:
            if not request.session.get('username'):
                return redirect(reverse('myapp/entry'))

