from django import forms

from .models import Person, Course


class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id).all(

                )
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.order_by('name')


GENDER_CHOICES= [('Male','Male'),('Female','Female'),('Other','Other')]
MATERIALS_PROVIDED = [('Pen','Pen'), ('Debit Notebook','Debit Notebook'), ('Exam Papers','Exam Papers')]
PURPOSE= [('Enquiry','Enquiry'),('Place Order','Place Order'),('Return','Return')]

class PersonCreationForm(forms.ModelForm):
    dob=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, widget=forms.RadioSelect)
    materials_provided = forms.MultipleChoiceField(
        choices=MATERIALS_PROVIDED, widget=forms.CheckboxSelectMultiple)
    purpose=forms.CharField(
        widget=forms.Select(choices=PURPOSE))
    class Meta:
        model = Person
        fields = '__all__'

