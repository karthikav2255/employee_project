from django import forms
from owner.models import Employee
# class EmployeeForm(forms.Form):
#     employee_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     designation=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     salary=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
#     experience=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
#     def clean(self):
#         cleaned_data=super().clean()
#         salary=cleaned_data.get('salary')
#         if int(salary)<0:
#             msg='Enter valid salary'
#             self.add_error('salary',msg)

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
        widgets={'employee_name':forms.TextInput(attrs={'class':'form-control'}),
                 'designation':forms.TextInput(attrs={'class':'form-control'}),
                 'salary':forms.NumberInput(attrs={'class':'form-control'}),
                 'experience':forms.NumberInput(attrs={'class':'form-control'}),
                 'image':forms.FileInput(attrs={'class':'form-control'}),

        }