from django.db import models


# ================= ---- This is gallery model ---- =========================
class GalleryModel(models.Model):
	title = models.CharField(max_length=45, blank=False)
	img = models.ImageField(upload_to='media', blank=False)
	txtSmall = models.CharField(max_length=50)

	def __str__(self):
		return self.title


# --------- ===============  FOR <li> tag class this will need built any lis in model and template   ================== ---------------

class PricingRooms(models.Model):
	roomType = models.CharField(max_length=35, blank=False)
	price = models.IntegerField(blank=False)
	badli = models.CharField(max_length=50, blank=True)

	li1 = models.CharField(max_length=50, blank=True)
	li2 = models.CharField(max_length=50, blank=True)
	li3 = models.CharField(max_length=50, blank=True)
	
	def __str__(self):
		return self.roomType

