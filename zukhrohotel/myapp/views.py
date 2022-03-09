from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import PricingRooms, GalleryModel
import telebot

token = '5264106705:AAHdfaGC-afFIDlTAW9Dt-i-9u0d9fUMAS-i-Tk0'

bot = telebot.TeleBot(token)


class IndexView(ListView):
	context_object_name = 'price_list'    
	template_name = 'index.html'
	queryset = PricingRooms.objects.all()

	def post(self, request, *args, **kwargs):

		if self.request.method == "POST":
			fullname = request.POST.get('fullname')
			email = request.POST.get('email')
			number = request.POST.get('number')
			checkIn = request.POST.get('checkIn')
			checkOut = request.POST.get('checkOut')
			adults = request.POST.get('adults')
			children = request.POST.get('children')
			rooms = request.POST.get('rooms')

			msg = f""" 
					full name: {fullname} 
					email: {email} 
					whatsapp number:{number}

					check-in: {checkIn} 
					check-out: {checkOut} 
					adults: {adults} 
					children: {children} 
					rooms: {rooms}
				
					THIS IS REGISTERED BY {fullname}...
				
				"""

			bot.send_message(1260142263, msg )

			context = {"fullname":fullname}
			return render(request, "index.html", context)

		else:
			return render(request, "index.html")

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['gallerys'] = GalleryModel.objects.all()

		# And so on for more models
		return context

