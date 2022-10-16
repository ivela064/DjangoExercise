# import the standard Django Forms
# from built-in library
from django import forms
from .models import GeeksModel
   
# creating a form 
# class InputForm(forms.Form):
   
#     first_name = forms.CharField(max_length = 200)
#     last_name = forms.CharField(max_length = 200)
#     roll_number = forms.IntegerField(
#                      help_text = "Enter 6 digit roll number"
#                      )
#     password = forms.CharField(widget = forms.PasswordInput())

# import GeeksModel from models.py

 ########################################## 
# form to work in the Django Administration POST exercise in geeksgeeks
# class GeeksForm(forms.ModelForm):
#     # specify the name of model to use
#     class Meta:
#         model = GeeksModel
#         fields = "__all__"
########################################################v

  

# class PersonForm(forms.Form):

#     # title = forms.CharField(widget = forms.Textarea)
#     # description = forms.CharField(widget = forms.CheckboxInput)
#     # views = forms.IntegerField(widget = forms.TextInput)
#     # available = forms.BooleanField(widget = forms.Textarea)
# #the other options of the exercise in geeksforgeeks
#     # title = forms.CharField()
#     # description = forms.CharField()
#     # views = forms.IntegerField()
#     # date = forms.DateField()

#     title = forms.CharField()
#     description = forms.CharField()
#     views = forms.IntegerField()
#     date = forms.DateField(widget = forms.SelectDateWidget)


##########################
#For the formset exercise in geeksforgeeks
#from django import forms
  
 ###########################FORMSET EXERCISE############### 
#create a form
# class GeeksForm(forms.Form):
#     title = forms.CharField()
#     description = forms.CharField()

###########################FORMSET EXERCISE###############

###########################FOR MODEL FORMSET EXERCISE###############
class GeeksForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = GeeksModel
        fields = "__all__"
###########################FOR MODEL FORMSET EXERCISE###############


###########################FOR CRUD EXERCISE##########################
# class GeeksForm(forms.ModelForm):
 
#     # create meta class
#     class Meta:
#         # specify model to be used
#         model = GeeksModel
 
#         # specify fields to be used
#         fields = [
#             "title",
#             "description",
#             "last_modified",
#         ]


###########################FOR CRUD EXERCISE##########################

###########################Class  Based Generic Views EXERCISE##########################
class GeeksForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = GeeksModel
 
        # specify fields to be used
        fields = [
            "title",
            "description",
        ]
###########################Class  Based Generic Views EXERCISE##########################