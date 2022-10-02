from django.shortcuts import render
from django.http import HttpResponse
from .models import Contracts

import pandas as pd
import json
# Create your views here.

def index(responce):
    if responce.method == 'POST' and responce.POST.get('SearchLine') != '':
        print(responce.POST.get('SearchLine'))
        contracts = Contracts.objects.raw('SELECT id, product_name, price, country_name FROM Contracts LIMIT 5')
        return render(responce, 'index.html', {'contracts': contracts})
    return render(responce, 'index.html')
    #return render(responce, 'index.html', {'contracts': contracts})

def table(request):
    df = pd.read_csv("~/Проекты/rosseltorg/big_data/norm_data.csv")
    # parsing the DataFrame in json format.
    json_records = df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
  
    return render(request, 'table.html', context)

# def search(responce):
#     contracts = Contracts.objects.raw('SELECT id, product_name, price, country_name FROM Contracts LIMIT 5')
#     return render(responce, 'index.html', {'contracts': contracts})
