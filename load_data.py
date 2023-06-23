import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dishsearch.settings")
django.setup()

from dishsearchapp.models import Dish

def load_data():
    with open('restaurants_small.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            dish_name = row['name']  # Modify this line to match the correct column name
            dish = Dish(name=dish_name)
            dish.save()

load_data()
