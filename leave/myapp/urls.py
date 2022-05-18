
from django.urls import path
from myapp.views import EnrollView,EntryView,StudentView,TearchView,PermitView
urlpatterns = [
    path('enroll/',EnrollView.as_view(),name='enroll'),
path('entry/',EntryView.as_view(),name='entry'),
path('student/',StudentView.as_view(),name='student'),
path('treach/',TearchView.as_view(),name='treach'),
path('permit/',PermitView.as_view(),name='permit')
]