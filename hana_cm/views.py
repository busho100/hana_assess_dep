from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic


from .models import Riyousha,RiyoushaAttributes,RiyoushaAssessment
 
from django.shortcuts import redirect
from django.contrib.admin.widgets import AdminDateWidget
from django.shortcuts import render, get_object_or_404
from django.views import View
from .forms import CreateForm,RiyoushaAttributesCreateForm,UpdateForm
from hana_cm.forms import FindForm, RiyoushaAttributesUpdateForm,RiyoushaAttributesOverwriteForm

# Create your views here.
class IndexView(LoginRequiredMixin, generic.ListView):
    model = Riyousha

class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Riyousha
    
    

class CreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Riyousha
    #fields = '__all__'
    form_class = CreateForm
    model = Riyousha

class UpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Riyousha
    form_class = UpdateForm
    model = Riyousha
    success_url = reverse_lazy('hana_cm:index')

class AttributesIndexView(LoginRequiredMixin, generic.ListView):
    model = RiyoushaAttributes

class AttributesDetailView(LoginRequiredMixin, generic.DetailView):
    model = RiyoushaAttributes
    
    

class AttributesCreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = RiyoushaAttributes
    form_class = RiyoushaAttributesCreateForm
    model = RiyoushaAttributes




class AttributesUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = RiyoushaAttributes
    form_class = RiyoushaAttributesUpdateForm
    model = RiyoushaAttributes
    success_url = reverse_lazy('hana_cm:attributes') 

    

def overwrite(LoginRequiredMixin, request,num):
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



class AttributesDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = RiyoushaAttributes 
    success_url = reverse_lazy('hana_cm:attributes')  
    




class DeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Riyousha 
    success_url = reverse_lazy('hana_cm:index')

class Find(View):

    def __init__(self):
        self.context = {
            'title': "要介護認定",
            'message':'認定状況',
            'form':FindForm()
        }

    def get(self,request):
        return render(request, 'hana_cm/find.html', self.context)

    def post(self,request):
        self.context['form'] = FindForm(request.POST)
        return render(request, 'hana_cm/find.html', self.context)

class AssessmentIndexView(LoginRequiredMixin, generic.ListView):
    model = RiyoushaAssessment