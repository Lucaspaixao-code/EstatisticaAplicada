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
        return render(request, 'imoveis.html',{ 'ValorParcelaSemJurosFixa': formatar_monetario(imovel.ValorParcelaSemJurosFixa()),
                                                'ValorParcelaFixa': formatar_monetario(imovel.CalcularValorParcelaFixa()),
                                                'valorParcelas': imovel.calcular_valor_parcela(), 
                                                'ValorJurosParcela': imovel.juros_por_parcela(),
                                                'ValorTotal': formatar_monetario(sum(imovel.calcular_valor_parcela())),
                                                'ValorTotalFixa': formatar_monetario(imovel.CalcularValorParcelaFixa() * imovel.periodo),
                                                'ValorTotalJurosFixa': formatar_monetario((imovel.CalcularValorParcelaFixa() * imovel.periodo) - imovel.calcular_valor_financiado()),
                                                'ValorJuros': formatar_monetario(sum(imovel.calcular_valor_parcela()) - float(imovel.calcular_valor_financiado())),
                                                'DataFinal': (add_months(datetime.date.today(), imovel.periodo)).strftime("%m/%Y"),
                                                'qtdeParcelas': int(request.GET.get('parcelas')),
                                                'Taxa': imovel.taxa,
                                                'Divida': formatar_monetario(float(imovel.divida - imovel.entrada)),
                                                'valorCompra': formatar_monetario(imovel.divida),
                                                'Entrada': formatar_monetario(imovel.entrada) if imovel.entrada > 0 else 'Sem Entrada'})
    else:
        veiculo = Veiculo(int(request.GET.get('divida')), int(request.GET.get('entrada')), int(request.GET.get('parcelas')),float(request.GET.get('taxa')))

        return render(request, 'veiculos.html',{'valorParcela': formatar_monetario(veiculo.calcular_valor_parcela()), 
                                                'ValorParcelaSemJuros': veiculo.ValorParcelaSemJuros(),
                                                'ValorTotal': formatar_monetario(veiculo.calcular_valor_parcela()*veiculo.qtde_parcela),
                                                'ValorTotalSemJuros': veiculo.calcular_valor_financiado(),
                                                'ValorJuros': formatar_monetario((veiculo.calcular_valor_parcela()*veiculo.qtde_parcela) - veiculo.calcular_valor_financiado()),
                                                'DataFinal': (add_months(datetime.date.today(), veiculo.qtde_parcela)).strftime("%m/%Y"),
                                                'Taxa': veiculo.taxa_juros,
                                                'Divida': formatar_monetario(veiculo.valor - veiculo.valor_entrada),
                                                'Entrada': formatar_monetario(veiculo.valor_entrada) if veiculo.valor_entrada > 0 else 'Sem Entrada',
                                                'qtdeParcelas': int(request.GET.get('parcelas')),
                                                'valorCompra': formatar_monetario(veiculo.valor)})
    
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

def formatar_monetario(numero):
    partes = str(numero).split('.')
    inteiro = partes[0]
    decimal = partes[1] if len(partes) > 1 else '00'

    # Formatar parte inteira
    parte_inteira_formatada = ''
    contador = 0
    for digito in inteiro[::-1]:
        if contador == 3:
            parte_inteira_formatada = '.' + parte_inteira_formatada
            contador = 0
        parte_inteira_formatada = digito + parte_inteira_formatada
        contador += 1

    # Formatar parte decimal
    parte_decimal_formatada = decimal[:2].ljust(2, '0')
    
    return f'R$ {parte_inteira_formatada},{parte_decimal_formatada}'
