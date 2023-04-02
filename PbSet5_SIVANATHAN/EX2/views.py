from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import forms
from django.forms.models import model_to_dict
from django.http import JsonResponse
import logging
from .models import *


# Create your views here.

contents=[]



class NewContent(forms.Form):
    name = forms.ModelChoiceField(label='name',queryset=Person.objects.all().values_list('name', flat=True))
    newcontent = forms.CharField(label='newcontent',max_length=150,min_length=10,widget=forms.TextInput(attrs={'id': 'toAdd'}))

def homepage(request):
    if request.method == 'POST':
        form = NewContent(request.POST)
        if form.is_valid():
            new_content = form.cleaned_data['newcontent']
            author = Person.objects.filter(name=form.cleaned_data['name']).first()
            if not author:
                return redirect('add')
            old_quotes=Quotes.objects.all().values()
            new_quote= Quotes(content=new_content, author=author)
            new_quote.save()
            new= model_to_dict(new_quote)

            return render(request,'EX2/homepage.html',{'contents':old_quotes,'new':new})

        else:
            return redirect('add')
    else:
        old_quotes=Quotes.objects.all().values()
        return render(request,'EX2/homepage.html',{'contents':old_quotes,'new':None})

def add(request):
    return render(request, 'EX2/add.html', {'form': NewContent()})

def entry(request,idEntry):

    content=Quotes.objects.filter(id=idEntry).values()[0]
    """print('!!!!!!!!!!!!!!!',content.values())

    print('!!!!!!!!!!!!!!!',content.values()[0])"""


    if content :
        return JsonResponse(content)
    else:
        return redirect('')



