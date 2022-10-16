from django.shortcuts import render

from django.http import HttpResponse
 
from django.shortcuts import render

from projectApp.models import GeeksModel
#from .forms import InputForm
from .forms import GeeksForm
from django.forms import formset_factory
from django.forms import modelformset_factory
import datetime
from django.views.generic.list import ListView
#from .forms import PersonForm
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.views import View
from django.views.generic.edit import CreateView    
from django.views.generic.detail import DetailView                   
from django.views.generic.edit import UpdateView

from django.views.generic.edit import DeleteView
from django.views.generic.edit import FormView

def index(request):
  return HttpResponse("Hello Geeks in the app")

 
# Create your views here.
##### HOME VIEW FUNCTION FOR DJANGO ADMINISTRATION EXERCISE ###############
def home_view(request):
    #context ={}
    #context['form']= GeeksForm()
    #print(request.GET)
    #print(request.POST)
    # context = {}
    # #form = PersonForm(request.POST or None)
    # form = GeeksForm(request.POST or None)
    # context['form'] = form
    # return render(request, "home.html", context)

    # context ={}
 
    # # create object of form
    # form = GeeksForm(request.POST or None, request.FILES or None)
     
    # # check if form data is valid
    # if form.is_valid():
    #     # save the form data to model
    #     form.save()
 
    # context['form']= form
    # return render(request, "home.html", context)

    context ={}
    form = GeeksForm(request.POST or None)
    context['form'] = form
    return render(request, "home.html", context)

##### HOME VIEW FUNCTION FOR DJANGO ADMINISTRATION EXERCISE ###############



############## VIEW FOR FORMSET EXERCISE #################3

def formset_view(request):
    context ={}
  
    # creating a formset
    GeeksFormSet = modelformset_factory(GeeksModel, fields=['title','description'])
    formset = GeeksFormSet(request.POST or None)
    if formset.is_valid():
      for form in formset:
        form.save()
        print(form.cleaned_data)
    # Add the formset to context dictionary
    context['formset']= formset
    return render(request, "home.html", context)
############## VIEW FOR FORMSET EXERCISE #################3


############## VIEW FOR MODEL FORMSET EXERCISE #################3
def modelformset_view(request):
    context ={}
  
    # creating a formset
    GeeksModelFormSet = modelformset_factory(GeeksModel, fields=['title','description'], extra=2)
    Modelformset = GeeksModelFormSet(request.POST or None)
    if Modelformset.is_valid():
      for form in Modelformset:
        form.save()
        print(form.cleaned_data)
        
    # Add the formset to context dictionary
    context['formset']= Modelformset
    return render(request, "home.html", context)
############## VIEW FOR MODEL FORMSET EXERCISE #################3


############## TEMPLATES EXERCISE ##################
# def geeks_view(request):
#     # create a dictionary to pass
#     # data to the template
#     context ={
#         "data":"Gfg is the best",
#         "list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     }
#     # return response with template and context
#     return render(request, "geeks.html", context)
############## TEMPLATES EXERCISE ##################


############## VIEW EXERCISE ##################
def geeks_view(request):
    # fetch date and time
    now = datetime.datetime.now()
    # convert to string
    html = "Time is {}".format(now)
    # return response
    return HttpResponse(html)

def list_view(request):
    # fetch date and time
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = GeeksModel.objects.all()
         
    return render(request, "list_view.html", context)

class GeeksList(ListView):
  model = GeeksModel

############## VIEW EXERCISE ##################

###########################FOR CRUD EXERCISE##########################
def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "create_view.html", context)
###########################FOR CRUD EXERCISE##########################


###########################FOR CRUD DETAILED VIEW EXERCISE##########################
def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = GeeksModel.objects.get(id = id)
         
    return render(request, "detail_view.html", context)


def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, id = id)
 
    # pass the object as instance in form
    form = GeeksForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_view.html", context)

    ###########################FOR CRUD DELETE EXERCISE##########################

def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")
 
    return render(request, "delete_view.html", context)
        ###########################FOR CRUD DELETE EXERCISE##########################


###########################Class  Based Generic Views EXERCISE##########################
def my_view(request):
    if request.method == 'GET':
        # <view logic>
        return HttpResponse('result')

class MyView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')

class GeeksCreate(CreateView):
 
    # specify the model for create view
    model = GeeksModel
 
    # specify the fields to be displayed
 
    fields = ['title', 'description']


class GeeksDetailView(DetailView):
    # specify the model to use
    model = GeeksModel


class GeeksUpdateView(UpdateView):
    # specify the model you want to use
    model = GeeksModel
 
    # specify the fields
    fields = [
        "title",
        "description"
    ]
 
    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url ="/"

 
class GeeksDeleteView(DeleteView):
    # specify the model you want to use
    model = GeeksModel
     
    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url ="/"

class GeeksFormView(FormView):
    # specify the Form you want to use
    form_class = GeeksForm
     
    # specify name of template
    template_name = "projectApp / geeksmodel_form_3.html"
 
    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url ="/thanks/"
###########################Class  Based Generic Views EXERCISE##########################