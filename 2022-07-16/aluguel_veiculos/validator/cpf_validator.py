import re


def valida_cpf(cpf):
    return not re.match(r'^([\s\d]+)$', cpf)
