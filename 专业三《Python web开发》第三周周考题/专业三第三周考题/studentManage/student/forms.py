from student.models import EntryModel,StudentModel,ClassModel
from django import forms


class EntryForm(forms.ModelForm):
    class Meta:
        model=EntryModel
        fields='__all__'

class EnrollForm(forms.ModelForm):
    class Meta:
        model=EntryModel
        fields='__all__'


class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields='__all__'

class ClassForm(forms.ModelForm):
    class Meta:
        model=ClassModel
        fields='__all__'




