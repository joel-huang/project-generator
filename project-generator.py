import csv
import random

def generate():
    list_adjectives = []
    list_industries = []
    list_products = []

    with open('products.csv') as products:
        for line in products.read().splitlines():
            list_products.append(line)

    product_index = random.randint(0, len(list_products)-1)
    product = list_products[product_index]

    with open('industries.csv') as industries:
        for line in industries.read().splitlines():
            list_industries.append(line)

        industry = ""
        for i in range(0,random.randint(0,1)):
            industry_index = random.randint(0, len(list_industries)-1)
            industry += list_industries[industry_index] + " "
            list_industries.pop(industry_index)


    with open('adjectives.csv') as adjectives:
        for line in adjectives.read().splitlines():
            list_adjectives.append(line)

        adjectives = ""
        for i in range(0,random.randint(1,2)):
            adjective_index = random.randint(0, len(list_adjectives)-1)
            adjectives += list_adjectives[adjective_index] + " "
            list_adjectives.pop(adjective_index)

    print(adjectives + industry + product)

for i in range(0,25):
    generate()