from django import forms
class inputweb(forms.Form):
    
    input1=forms.IntegerField(label="from")
    input2=forms.IntegerField(label="to")
    #input=forms.CharField("enter the text")