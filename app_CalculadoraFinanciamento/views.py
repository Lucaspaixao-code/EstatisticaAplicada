from django.shortcuts import render
from app_CalculadoraFinanciamento.models import Veiculo
from datetime import datetime, timedelta

# Create your views here.

def home(request):
    return render(request, 'home.html')

def veiculo(request):
    try:
        veiculo = Veiculo(int(request.GET.get('ValorEmprestimo')), int(request.GET.get('ValorEntrada')), int(request.GET.get('Parcelas')),int(request.GET.get('TaxaJuros')))
        return render(request, 'veiculos.html',{'valorParcela': "{:.2f}".format(veiculo.calcular_valor_parcela()), 
                                                'ValorTotal': veiculo.valor,
                                                'ValorJuros': "{:.2f}".format((veiculo.calcular_valor_parcela()*veiculo.qtde_parcela) - veiculo.valor),
                                                'DataFinal': (datetime.now() + timedelta(days=veiculo.qtde_parcela)).strftime("%m/%Y")})
    except:
        return render(request, 'veiculos.html')
