"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco

Enunciado: 
Faça um programa que responda as seguintes perguntas:

1.	Quantos alunos estão matriculados na escola, no total?
2.	Quantos e quais estão matriculados APENAS em INGLES?
3.	Quantos e quais estão matriculados APENAS em FRANCES?
4.	Quantos e quais estão matriculados EM AMBOS os cursos?
5.	Quantos alunos estão matriculados somente em francês ou somente em inglês, mas não em ambos os cursos?

"""

alunos_ingles = {
    "João Alves dos Santos",
    "Maria Magalhães",
    "Antônio da Silva Ferreira",
    "José Júnior Jarbas",
    "Henrique da Silva Sauro",
    "Joaquina Ferreira da Silva",
    "Fabiana Aparecida Bianco",
    "Marrone Gutierres",
    "Carlos Magno Farad",
    "Antônio da Silva Júnior Amaral",
}

alunos_frances = {
    "João Alves dos Santos",
    "Antônio da Silva Ferreira",
    "Fernanda Abdala Mohamed",
    "Abner Mignon Alib",
    "Alisson Figueiredo",
    "Henrique da Silva Sauro",
    "Maria Magalhães",
    "Marrone Gutierres",
    "Joaquina Ferreira da Silva",
}

print(f"Resp 1) - {len(alunos_ingles.union(alunos_frances))}", end="\n\n")

print(f"Resp 2) - {len(alunos_ingles)}. Os alunos são: {alunos_ingles}", end="\n\n")

print(f"Resp 3) - {len(alunos_frances)}. Os alunos são: {alunos_frances}", end="\n\n")

print(
    f"Resp 4) - {len(alunos_ingles.intersection(alunos_frances))}. Os alunos são: {alunos_ingles.intersection(alunos_frances)}",
    end="\n\n",
)

print(f"Resp 5) - {len(alunos_ingles.symmetric_difference(alunos_frances))}")
