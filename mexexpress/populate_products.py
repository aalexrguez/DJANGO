import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mexexpress.settings')
import django
django.setup()



#script para poblar la tabla Product
from faker import Faker
import random
from shopApp.models import Product,Contacts


faker_generator = Faker() # se crear el objeto faker

def populate_products(n_products=5):

    for i in range(n_products):
        fake_name = faker_generator.sentence(nb_words=6,variable_nb_words=True)
        fake_description = faker_generator.paragraph(nb_sentences=3,variable_nb_sentences=True)
        fake_full_cost = random.uniform(10,14000)
        fake_is_offer = random.random() > 0.5
        fake_offer_cost = random.uniform(5,fake_full_cost) if fake_is_offer else fake_full_cost

        product = Product.objects.get_or_create(
            product_name = fake_name,
            product_description = fake_description,
            product_full_cost = fake_full_cost,
            product_is_offer = fake_is_offer,
            product_offer_cost = fake_offer_cost
        )
def populate_contacts(n_contacts):
    for i in range(n_contacts):
        fake_name = faker_generator.name()
        fake_address = faker_generator.address()
        fake_phone = faker_generator.phone_number[:15]
        fake_activate = faker_generator.boolean()

        contact = Contacts.objects.get_or_create(
            contact_full_name = fake_name,
            contact_address = fake_address,
            contact_phone = fake_phone,
            contact_activate = fake_activate
        )

if __name__ == '__main__':
    print('Empezar a poblar la base de datos')
    populate_products(20)
    print('finalizado')