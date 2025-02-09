n= int(input())
m_nota = 0.0
m_nome = ''
for i in range(n):

    nome, nota = input().split()
    nota = float(nota)
    if nota > m_nota:
        m_nota = nota
        m_nome = nome
    
print(m_nome)