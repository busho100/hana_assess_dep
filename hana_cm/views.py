from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic


from .models import Riyousha,RiyoushaAttributes,Adl_1 
 
from django.shortcuts import redirect
from django.contrib.admin.widgets import AdminDateWidget
from django.shortcuts import render, get_object_or_404
from django.views import View
from .forms import CreateForm,RiyoushaAttributesCreateForm,UpdateForm
from hana_cm.forms import FindForm, RiyoushaAttributesUpdateForm,Assess_Adl_1,RiyoushaAttributesOverwriteForm

# Create your views here.
class IndexView(generic.ListView):
    model = Riyousha

class DetailView(generic.DetailView):
    model = Riyousha
    
    

class CreateView(generic.edit.CreateView):
    model = Riyousha
    #fields = '__all__'
    form_class = CreateForm
    model = Riyousha

class UpdateView(generic.edit.UpdateView):
    model = Riyousha
    form_class = UpdateForm
    model = Riyousha
    success_url = reverse_lazy('hana_cm:index')

class AttributesIndexView(generic.ListView):
    model = RiyoushaAttributes

class AttributesDetailView(generic.DetailView):
    model = RiyoushaAttributes
    
    

class AttributesCreateView(generic.edit.CreateView):
    model = RiyoushaAttributes
    form_class = RiyoushaAttributesCreateForm
    model = RiyoushaAttributes




class AttributesUpdateView(generic.edit.UpdateView):
    model = RiyoushaAttributes
    form_class = RiyoushaAttributesUpdateForm
    model = RiyoushaAttributes
    success_url = reverse_lazy('hana_cm:attributes') 

    

def overwrite(request,num):
    obj =RiyoushaAttributes.objects.get(id=num)
    if(request.method == 'POST'):
        attributes = RiyoushaAttributesOverwriteForm(request.POST,instance=obj)

        
        
            
        if 'button_1' in request.POST:
            obj.id=None
            obj.save() 

        """ if 'button_1' in request.POST:
            overwrite() """

        return redirect(to='/hana_cm/attributes')

    context = {
        'form':RiyoushaAttributesOverwriteForm(instance=obj)
 
    }
    return render(request, 'hana_cm/riyoushaattributes_overwrite.html',context)



class AttributesDeleteView(generic.edit.DeleteView):
    model = RiyoushaAttributes 
    success_url = reverse_lazy('hana_cm:attributes')  
    




class DeleteView(generic.edit.DeleteView):
    model = Riyousha 
    success_url = reverse_lazy('hana_cm:index')

class Find(View):

    def __init__(self):
        self.context = {
            'title': "???????????????",
            'message':'????????????',
            'form':FindForm()
        }

    def get(self,request):
        return render(request, 'hana_cm/find.html', self.context)

    def post(self,request):
        self.context['form'] = FindForm(request.POST)
        return render(request, 'hana_cm/find.html', self.context)

def assess_mahi(request):
    if(request.method == 'POST'):
        obj = Adl_1()
        friend = Assess_Adl_1(request.POST, instance=obj)
        friend.save()
        return redirect(to='')
    context={
        'form':Assess_Adl_1()
    }
    
    return render(request, 'hana_cm/assess_form.html', context)