from django.shortcuts import render
from app_CalculadoraFinanciamento.models import Veiculo, Imovel
import datetime 
import calendar 


# Create your views here.

def home(request):
    return render(request,'home.html')


def relatorio(request):
    tipo = int(request.GET.get('gridRadios'))
    
    if tipo == 1:   
        imovel = Imovel(int(request.GET.get('divida')), int(request.GET.get('parcelas')), float(request.GET.get('taxa')), int(request.GET.get('entrada')))
        return render(request, 'imoveis.html',{ 'ValorParcelaSemJurosFixa': "{:.2f}".format(imovel.ValorParcelaSemJurosFixa()),
                                                'ValorParcelaFixa': "{:.2f}".format(imovel.CalcularValorParcelaFixa()),
                                                'valorParcelas': imovel.calcular_valor_parcela(), 
                                                'ValorJurosParcela': imovel.juros_por_parcela(),
                                                'ValorTotal': "{:.2f}".format(sum(imovel.calcular_valor_parcela())),
                                                'ValorTotalFixa': "{:.2f}".format(imovel.CalcularValorParcelaFixa() * imovel.periodo),
                                                'ValorTotalJurosFixa': "{:.2f}".format((imovel.CalcularValorParcelaFixa() * imovel.periodo) - imovel.calcular_valor_financiado()),
                                                'ValorJuros': "{:.2f}".format(sum(imovel.calcular_valor_parcela()) - float(imovel.calcular_valor_financiado())),
                                                'DataFinal': (add_months(datetime.date.today(), imovel.periodo)).strftime("%m/%Y"),
                                                'qtdeParcelas': int(request.GET.get('parcelas')),
                                                'Taxa': imovel.taxa,
                                                'Divida': "{:.2f}".format(imovel.divida - imovel.entrada),
                                                'valorCompra': "{:.2f}".format(imovel.divida),
                                                'Entrada': 'R$ '+str("{:.2f}".format(imovel.entrada)) if imovel.entrada > 0 else 'Sem Entrada'})
    else:
        veiculo = Veiculo(int(request.GET.get('divida')), int(request.GET.get('entrada')), int(request.GET.get('parcelas')),float(request.GET.get('taxa')))

        return render(request, 'veiculos.html',{'valorParcela': "{:.2f}".format(veiculo.calcular_valor_parcela()), 
                                                'ValorParcelaSemJuros': veiculo.ValorParcelaSemJuros(),
                                                'ValorTotal': "{:.2f}".format(veiculo.calcular_valor_parcela()*veiculo.qtde_parcela),
                                                'ValorTotalSemJuros': veiculo.calcular_valor_financiado(),
                                                'ValorJuros': "{:.2f}".format((veiculo.calcular_valor_parcela()*veiculo.qtde_parcela) - veiculo.calcular_valor_financiado()),
                                                'DataFinal': (add_months(datetime.date.today(), veiculo.qtde_parcela)).strftime("%m/%Y"),
                                                'Taxa': veiculo.taxa_juros,
                                                'Divida': veiculo.valor - veiculo.valor_entrada,
                                                'Entrada': 'R$ '+str(veiculo.valor_entrada) if veiculo.valor_entrada > 0 else 'Sem Entrada',
                                                'qtdeParcelas': int(request.GET.get('parcelas')),
                                                'valorCompra': veiculo.valor})
    
def add_months(base_date=None, months_to_add=1):
    if months_to_add == 0:
        raise ValueError("months_to_add cannot be zero")
    if base_date is None:
        base_date = datetime.now
    years_to_add = months_to_add // 12
    remaining_months = months_to_add % 12
    new_year = base_date.year + years_to_add
    new_month = (base_date.month + remaining_months) % 12  # Wrap around to next year if necessary
    # Handle cases where the new month might have fewer days than the base date's day
    if new_month == base_date.month:
        new_day = min(base_date.day, calendar.monthrange(new_year, new_month)[1])
    else:
        new_day = calendar.monthrange(new_year, new_month)[1]  # Use the last day of the new month

    return datetime.date(new_year, new_month, new_day)

