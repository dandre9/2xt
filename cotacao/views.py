from django.shortcuts import render
from http.client import HTTPConnection
from .models import Compra
import json, requests

# Create your views here.
def gerar_destinos():
    c = HTTPConnection("staging.segurospromo.com.br")
    headers = { 'Authorization' : 'Basic aWxsYWdlcjpldm9rZXJAMTEx'}
    c.request('GET', '/emitir-seguros/v0/additional-info/destinations', headers=headers)
    res = c.getresponse()
    data = res.read()
    json_data = json.loads(data)
    return json_data

def home(request):
    context = {'destinos' : gerar_destinos()}
    return render(request, 'cotacao/home.html', context=context)

def opcoes(request):
    data_inicio = request.POST['data_inicio']
    data_fim = request.POST['data_fim']
    destino = request.POST['destinos']

    cotacao = {
      "begin_date": str(data_inicio),
      "end_date": str(data_fim),
      "destination": str(destino),
      "benefits": ["42", "46"]
    }

    response = requests.post('http://staging.segurospromo.com.br/emitir-seguros/v0/quotations',
    data=json.dumps(cotacao),
    auth=requests.auth.HTTPBasicAuth('illager', 'evoker@111'))
    json_data = json.loads(response.text)

    ctx=[]
    for i in json_data:
        preco_adulto = str("%.2f" % float(i['adult']['price']))
        provedor = i['provider_name']
        produto = i['name']
        beneficio1 = i['benefits'][0]['name']
        cobertura1 = i['benefits'][0]['coverage']
        beneficio2 = i['benefits'][1]['name']
        cobertura2 = i['benefits'][1]['coverage']
        codigo = i['code']
        ctx.append({'provedor': provedor,
        'produto': produto,
        'codigo': codigo,
        'preco_adulto': preco_adulto,
        'beneficio1': beneficio1,
        'beneficio2': beneficio2,
        'cobertura1': cobertura1,
        'cobertura2': cobertura2})

    context = {'destinos' : gerar_destinos()}

    return render(request, 'cotacao/opcoes_seguro.html', context={"cotacoes":ctx})

def compra(request):
    dados = request.POST['dados_compra'].split(";")
    compra = Compra(provedor=dados[0], produto=dados[1], preco=float(dados[2]), codigo=dados[3], cliente="2xt")
    compra.save()

    ctx={'produto': dados[1],
    'provedor': dados[0],
    'preco': dados[2]}

    return render(request, 'cotacao/dados_compra.html', context=ctx)
