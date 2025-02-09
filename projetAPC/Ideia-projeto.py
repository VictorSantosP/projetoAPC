import tkinter as tk
from tkinter import ttk, messagebox

def tipoEmissao(codigo):
    prodCO2 = ''
    if codigo == "Automotores":
        prodCO2 = 'Automotores'
    elif codigo == "Indústria":
        prodCO2 = 'Industria'
    elif codigo == "Energia":
        prodCO2 = 'Energia'
    elif codigo == "Resíduos":
        prodCO2 = 'Residuos'
    elif codigo == "Agricultura":
        prodCO2 = 'Agricultura'
    elif codigo == "Desmatamento":
        prodCO2 = 'Desmatamento'
    elif codigo == "Produtos Químicos":
        prodCO2 = 'Produtos Químicos'
    else:
        prodCO2 = 'Código inválido'
    return prodCO2

def calcEmissao(prodCO2):
    codigoloc = tipoEmissao(prodCO2)
    resultado = 0
    if codigoloc == 'Automotores':
        resultado = 15000 * (23.1 / 100) / 1000
    elif codigoloc == 'Industria':
        resultado = 100000 * (10 / 1000)
    elif codigoloc == 'Energia':
        carvao_consumido = 350000
        fator_emissao = 2.2
        resultado = (carvao_consumido * 1000 * fator_emissao) / 1000
    elif codigoloc == 'Residuos':
        residuos_gerados = 500000
        fator_emissao = 1.5
        resultado = residuos_gerados * fator_emissao / 1000
    elif codigoloc == 'Agricultura':
        gado = 20000
        emissao_por_gado = 2.5
        fertilizantes = 10000
        fator_emissao_fertilizantes = 1.6
        resultado = (gado * emissao_por_gado + fertilizantes * fator_emissao_fertilizantes) / 1000
    elif codigoloc == 'Desmatamento':
        area_desmatada = 10000  # em hectares
        fator_emissao = 0.3  # toneladas de CO2 por hectare
        resultado = area_desmatada * fator_emissao
    elif codigoloc == 'Produtos Químicos':
        producao_quimica = 50000  # toneladas
        fator_emissao = 2.8  # toneladas de CO2 por tonelada de produto químico
        resultado = producao_quimica * fator_emissao / 1000
    return resultado

def replanto(prodCO2):
    tipo = tipoEmissao(prodCO2)
    resultado = 22 * 100
    qnt = 0
    if tipo == 'Automotores':
        qnt = int((3460 / resultado) + 1)
    elif tipo == 'Industria':
        qnt = int((1000000 / resultado) + 1)
    elif tipo == 'Energia':
        qnt = int((7700000 / resultado) + 1)
    elif tipo == 'Residuos':
        qnt = int((750000 / resultado) + 1)
    elif tipo == 'Agricultura':
        qnt = int((950000 / resultado) + 1)
    elif tipo == 'Desmatamento':
        qnt = int((3000000 / resultado) + 1)
    elif tipo == 'Produtos Químicos':
        qnt = int((1400000 / resultado) + 1)
    return qnt

def calcular_resultado():
    try:
        entrada = tipo_emissor_var.get()
        tipo = tipoEmissao(entrada)

        if tipo == 'Código inválido':
            messagebox.showerror("Erro", "Por favor, escolha uma opção válida!")
            return

        resultado = calcEmissao(entrada)
        qnt = replanto(entrada)

        resultado_label.config(text=f"Emissão calculada: {resultado:.2f} toneladas de CO2 por ano")
        replantar_label.config(text=f"Você precisaria replantar {qnt} árvores para que em 100 anos roubassem a quantidade de CO2 produzida em 1 ano.\nSe for em 1 ano, precisaria de: {qnt * 100} árvores.")
    except ValueError:
        messagebox.showerror("Erro", "Ocorreu um erro inesperado. Tente novamente!")

# Função para popular a aba de informações educativas
def popular_informacoes():
    info_text = (
        "Dicas para Reduzir Emissões de CO2:\n\n"
        "1. Substitua fontes de energia por renováveis (solar, eólica).\n"
        "2. Use transporte público, bicicletas ou caminhe sempre que possível.\n"
        "3. Recicle e reduza o desperdício em casa e no trabalho.\n"
        "4. Invista em eletrodomésticos e veículos eficientes em energia.\n"
        "5. Plante árvores e apoie iniciativas de reflorestamento.\n"
        "6. Apoie políticas públicas que promovam a redução de emissões.\n"
        "7. Utilize lâmpadas LED e desligue aparelhos quando não estiverem em uso.\n\n"
        "Cuide do meio ambiente, pois ele é essencial para a sobrevivência de todos os seres vivos. Proteger os recursos naturais não é apenas um dever, mas também a garantia de um futuro sustentável para as próximas gerações.\n\nCada pequena ação conta e pode fazer a diferença para combater as mudanças climáticas.\n "
    )
    info_label.config(text=info_text)

# Criação da interface gráfica com Tkinter
root = tk.Tk()
root.title("Calculadora de Emissões de CO2")
root.geometry("825x450")
root.resizable(False, False)

# Configuração do Notebook (abas)
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# Frame da aba de cálculo
frame_calculo = ttk.Frame(notebook, width=700, height=500)
frame_calculo.pack(fill="both", expand=True)

# Frame da aba de informações
frame_informacoes = ttk.Frame(notebook, width=700, height=500)
frame_informacoes.pack(fill="both", expand=True)

# Adicionando as abas
notebook.add(frame_calculo, text="Cálculo de Emissões")
notebook.add(frame_informacoes, text="Informações Educativas")

# Aba de Cálculo
tipo_emissor_var = tk.StringVar(value="Escolha uma opção")

# Widgets para cálculo
title_label = ttk.Label(frame_calculo, text="Calculadora de Emissões de CO2", font=("Helvetica", 16))
title_label.pack(pady=20)

tipo_label = ttk.Label(frame_calculo, text="Escolha o tipo de emissor de CO2:")
tipo_label.pack(pady=10)

# Menu suspenso para seleção do tipo de emissor
tipo_opcoes = ttk.OptionMenu(frame_calculo, tipo_emissor_var, "Escolha uma opção", "Automotores", "Indústria", "Energia", "Resíduos", "Agricultura", "Desmatamento", "Produtos Químicos")
tipo_opcoes.pack(pady=10)

calcular_button = ttk.Button(frame_calculo, text="Calcular Emissão", command=calcular_resultado)
calcular_button.pack(pady=20)

resultado_label = ttk.Label(frame_calculo, text="Emissão calculada: ", font=("Helvetica", 12))
resultado_label.pack(pady=10)

replantar_label = ttk.Label(frame_calculo, text="Replantio necessário: ", font=("Helvetica", 12))
replantar_label.pack(pady=10)

# Aba de Informações
info_label = ttk.Label(frame_informacoes, text="", font=("Helvetica", 12), justify="left", wraplength=650)
info_label.pack(pady=20)
popular_informacoes()

# Iniciar a interface gráfica
root.mainloop()
