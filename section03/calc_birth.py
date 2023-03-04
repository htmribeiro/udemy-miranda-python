"""
No objeto diff teremos a diferença entre as datas. Pelo atributo day e seconds
pegamos esta diferença em relação ao número de dias e segundos,
respectivamente.

Para saber a quantidade de anos, calculamos a divisão inteira entre a
quantidade de dias por 365 e atualizamos o valor de days para descontar a
quantia relativa a esses anos.

Com o mês, calculamos a divisão por 30 e atualizamos novamente a quantidade de
dias.

Para as horas e minutos a lógica é exatamente a mesma, dividindo o número de
segundos por 3600 e 60, respectivamente.

Vale lembrar que esta diferença é aproximada, pois não leva em considerações
ano bissextos dentro do intervalo considerado, nem a quantidade exata de dias
em cada mês.
"""
from datetime import datetime


def date_of_birth(years, months, days):
    birth_year = years
    data1 = datetime(year=years, month=months, day=days)
    data2 = datetime.now()

    diff = data2-data1

    days = diff.days
    years, days = days // 365, days % 365
    months, days = days // 30, days % 30

    seconds = diff.seconds
    hours, seconds = seconds // 3600, seconds % 3600
    minutes, seconds = seconds // 60, seconds % 60

    # print(f"Desde {data1} passaram {years} anos, {months} meses", end=', ')
    # print(f"{days} dias, {hours} horas, {minutes} minutos", end=', ')
    # print(f"e {seconds} segundos")
    # print(birth_year)

    return birth_year, years, months, days


if __name__ == "__main__":
    date_of_birth(1980, 3, 21)
