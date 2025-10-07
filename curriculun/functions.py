from datetime import datetime, date


def calcula_idade(data_nascimento: str) -> int:
    nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()

    hoje = date.today()
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))

    return idade

