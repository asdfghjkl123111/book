
from django.urls import path
from student.views.emtry import EntryView,EnrollView
from student.views.all import SelectView,InsertView,DeleteView,UpdateView,OutView
urlpatterns = [
    path('entry/',EntryView.as_view(),name='entry'),
path('enroll/',EnrollView.as_view(),name='enroll'),
path('select/',SelectView.as_view(),name='select'),
path('insert/',InsertView.as_view(),name='insert'),
path('delete/',DeleteView.as_view(),name='delete'),
path('update/',UpdateView.as_view(),name='update'),
path('out/',OutView.as_view(),name='out'),
]
