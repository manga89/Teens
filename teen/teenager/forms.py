from django.forms import ModelForm
from tempus_dominus.widgets import DatePicker
from .models import Student

class StudentCreateForm(ModelForm):
	class Meta:
		model = Student
		fields = ['first_name', 'last_name', 'middle_name','date_of_birth','state_of_origin','email_address', 
			'image', 'phone_number', 'parent_full_name', 'parent_phone_number', 'address',

		 ]

		widgets ={
			'date_of_birth': DatePicker( 
					options = {

					'minDate': '1998-01-01'
					}
				)

		}


	