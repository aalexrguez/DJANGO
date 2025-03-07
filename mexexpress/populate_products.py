import os
os.environ.setdefault('DJANGO_SETTING_MODULE','mexexpress.settings')
import django
django.setup()



#script para poblar la tabla Product
from faker import Faker
import random
from shopApp.models import Product


faker_generator = Faker() # se crear el objeto faker

if __name__ == '__main__':
    print('Empezar a poblar la base de datos')

    print('finalizado')