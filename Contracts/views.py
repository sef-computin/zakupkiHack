from django.shortcuts import render
from django.http import HttpResponse
from .models import Contracts
from .models import SearchHandler

import pandas as pd
import json
# Create your views here.
# print('view')

def index(responce):
    if responce.method == 'POST' and responce.POST.get('SearchLine') != '':
        # passval = SearchHandler.search(responce.POST.get('SearchLine'))
        ids = [id for id in SearchHandler.search(responce.POST.get('SearchLine'))]
        ids = []
        contracts = []
        for id in ids: contracts.append(Contracts.objects.raw(f'SELECT * FROM Contracts WHERE id = {id}'))
        # contracts = Contracts.objects.raw('SELECT id, product_name, price, country_name FROM Contracts LIMIT 5')
        return render(responce, 'index.html', {'contracts': contracts})
    return render(responce, 'index.html')

def table(request):
    df = pd.read_csv("~/Проекты/rosseltorg/big_data/norm_data.csv")
    # parsing the DataFrame in json format.
    json_records = df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
  
    return render(request, 'table.html', context)