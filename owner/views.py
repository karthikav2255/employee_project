from django.shortcuts import render,redirect
from django.views.generic import View,ListView,CreateView,UpdateView,DetailView
from owner.form import EmployeeForm
from owner.models import Employee
from django.urls import  reverse_lazy

class EmployeeView(CreateView):
    model = Employee
    template_name = 'add_employee.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('employeelist')
    # def get(self,request):
    #     form=EmployeeForm()
    #     return  render(request,'add_employee.html',{'form':form})
    #
    # def post(self,request):
    #     form=EmployeeForm(request.POST,files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         print(form.cleaned_data)
    #         qs=Employee(employee_name=form.cleaned_data.get("employee_name"),
    #                     designation=form.cleaned_data.get("designation"),
    #                     salary=form.cleaned_data.get('salary'),
    #                     experience=form.cleaned_data.get('experience'))
    #         qs.save()
    #
    #         return render(request,'add_employee.html',{'msg':'An employee is added'})
    #         return redirect('employeelist')
    #     else:
    #         return render(request,'add_employee.html',{'form':form})

class EmployeeListView(ListView):
    model=Employee
    template_name ='employee_list.html'
    context_object_name = 'employees'
    # def get(self,request):
    #     qs=Employee.objects.all()
    #     return render(request,'employee_list.html',{'employees':qs})

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee_list.html'
    context_object_name = 'employee'
    pk_url_kwarg = "id"
    # def get(self,request,**kwargs):
    #     #pass
    #     #kwargs={'id':3}
    #     qs=Employee.objects.get(id=kwargs.get('id'))
    #     return render(request,'employee_detail.html',{'employee':qs})

class EmployeeDeleteView(View):

    def get(self,request,**kwargs):
        qs=Employee.objects.get(id=kwargs.get('id'))
        qs.delete()
        return redirect('employeelist')

class EmployeeChangeDetailsView(UpdateView):
    model=Employee
    template_name = 'employee_edit.html'
    form_class = EmployeeForm
    pk_url_kwarg = "id"
    success_url = reverse_lazy("employeelist")
    # def get(self,request,*args,**kwargs):
    #     qs=Employee.objects.get(id=kwargs.get('id'))
    #     form=EmployeeForm(instance=qs)
    #     return render(request,'employee_edit.html',{'form':form})
    #
    # def post(self,request,*args,**kwargs):
    #     qs=Employee.objects.get(id=kwargs.get('id'))
    #     form=EmployeeForm(request.POST,instance=qs,files=request.FILES)
    #     form.save()
    #     return redirect("employeelist")