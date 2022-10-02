from django.shortcuts import render
from django.http import HttpResponse
from .models import Contracts

import pandas as pd
import json
# Create your views here.

def index(responce):
    contracts = Contracts.objects.all()[:5]
    for contract in contracts: print(contract.product_name)
    # return render(responce, 'index.html')
    return render(responce, 'index.html', {'contracts': contracts})

# Create your views here.
def table(request):
    df = pd.read_csv("~/Проекты/rosseltorg/big_data/norm_data.csv")
    # parsing the DataFrame in json format.
    json_records = df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
  
    return render(request, 'table.html', context)
