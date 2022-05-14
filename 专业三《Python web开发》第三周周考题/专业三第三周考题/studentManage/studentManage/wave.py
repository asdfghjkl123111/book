from django.shortcuts import redirect,reverse
from django.utils.deprecation import MiddlewareMixin



class Ware(MiddlewareMixin):
    def process_request(self,request):
        if request.path not in ['/student/entry/','/student/enroll/']:
            if not request.session.get('username'):
                return redirect(reverse('student:entry'))


