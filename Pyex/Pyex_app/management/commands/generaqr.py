import qrcode, cv2
from django.core.management.base import BaseCommand, CommandError
from Pyex_app.models import Question as Pyex_app

class creaQR(BaseCommand):
	
	help= 'Genera un QR a partir del código'
	codigo =input("Código a insertar")
	img = qrcode.make(codigo)
	type(img)
	nombre = codigo+".png"
	img.save(/var/www/Pyex/media/fotus/nombre)
