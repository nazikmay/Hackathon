from django import forms
from django.shortcuts import render
from random import randint

class PasswordGeneratorForm(forms.Form):
    CHOICES = [
        ('1', 'Symbols'),
        ('2', 'Numbers'),
        ('3', 'Alphabets'),
        ('4', 'All'),
    ]

    choice = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    length = forms.IntegerField(min_value=1, max_value=50)

def randomaizer_all(length):
    lst_num = ['0','1','2','3','4','5','6','7','8','9']
    lst_abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lst_simbvol = ['!', '@','#','$', '%','^','&','*','(',')','_','+','}','{','/',':','?','>','<','|','~','}']
    lst = lst_abc + lst_num + lst_simbvol
    result = ""
    stopper = 0
    while length > stopper:
        result += lst[randint(0, len(lst)-1)]
        stopper += 1
    return result

def randomaizer_abc(length):
    lst_abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    result = ""
    stopper = 0
    while length > stopper:
        result += lst_abc[randint(0, len(lst_abc)-1)]
        stopper += 1
    return result

def randomaizer_num(length):
    lst_num = ['0','1','2','3','4','5','6','7','8','9']
    result = ""
    stopper = 0
    while length > stopper:
        result += lst_num[randint(0, len(lst_num)-1)]
        stopper += 1
    return result

def randomaizer_sibvol(length):
    lst_simbvol = ['!', '@','#','$', '%','^','&','*','(',')','_','+','}','{','/',':','?','>','<','|','~','}']
    result = ""
    stopper = 0
    while length > stopper:
        result += lst_simbvol[randint(0, len(lst_simbvol)-1)]
        stopper += 1
    return result

def generate_password(request):
    if request.method == 'POST':
        form = PasswordGeneratorForm(request.POST)
        if form.is_valid():
            choice = form.cleaned_data['choice']
            password = ""
            if choice == '1':
                password = randomaizer_sibvol(form.cleaned_data['length'])
            elif choice == '2':
                password = randomaizer_num(form.cleaned_data['length'])
            elif choice == '3':
                password = randomaizer_abc(form.cleaned_data['length'])
            elif choice == '4':
                password = randomaizer_all(form.cleaned_data['length'])

            return render(request, 'generator_password/generate_password.html', {'form': form, 'password': password})

    else:
        form = PasswordGeneratorForm()

    return render(request, 'generator_password/generate_password.html', {'form': form})