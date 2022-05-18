from myapp.models import MouldModel,UserModel,LevelModel

from django import forms


class MouldForm(forms.ModelForm):
    class Meta:
        model=MouldModel
        fields='__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model=MouldModel
        fields=('stu_name','context','createtime','tid')

class UserForm(forms.ModelForm):
    class Meta:
        model=UserModel
        fields=('uname','upwd')

class ErollForm(forms.ModelForm):
    new_pwd=forms.CharField(max_length=64,label='确定密码')
    class Meta:
        model=UserModel
        fields=('uname','upwd','new_pwd')

class LevelForm(forms.ModelForm):
    class Meta:
        model=LevelModel
        fields='__all__'



