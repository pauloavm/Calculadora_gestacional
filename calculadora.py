# -*- coding: utf-8 -*-
from tkinter import Tk, Label, Entry, Button, Frame, StringVar
from datetime import date, timedelta

# Funções de cálculo
def calculate_age():
    """
    Função principal para calcular a idade cronológica e corrigida.
    """
    try:
        # Pega os valores dos campos
        birthdate_str = birthdate_entry.get()
        gestational_age_weeks = int(gestational_age_entry.get())
        gestational_age_days = int(gestational_age_days_entry.get())

        # Converte a string da data para um objeto date
        birthdate = date.fromisoformat(birthdate_str)

        # Chama as funções de cálculo
        chronological_age = calculate_chronological_age(birthdate)
        corrected_age = calculate_corrected_age(chronological_age, gestational_age_weeks, gestational_age_days)

        # Exibe os resultados
        display_results(chronological_age, corrected_age)

    except ValueError:
        # Lida com erros de entrada de dados
        result_var.set("Por favor, preencha todos os campos corretamente. Use o formato YYYY-MM-DD para a data.")

def calculate_chronological_age(birthdate):
    """
    Calcula a idade cronológica em semanas e meses.
    """
    today = date.today()
    delta = today - birthdate
    total_days = delta.days

    age_in_weeks = total_days // 7
    age_in_months = total_days // 30 # Aproximação

    return {'weeks': age_in_weeks, 'months': age_in_months}

def calculate_corrected_age(chronological_age, gestational_age_weeks, gestational_age_days):
    """
    Calcula a idade corrigida em semanas, meses e dias.
    A lógica é a mesma do código JS original.
    """
    corrected_weeks = chronological_age['weeks'] - (40 - gestational_age_weeks)
    
    # O código JavaScript original faz o cálculo de uma forma que o resultado final em dias
    # não é um resto de semanas, então vamos manter essa mesma lógica.
    total_corrected_days = corrected_weeks * 7 + gestational_age_days
    
    final_weeks = total_corrected_days // 7
    final_days = total_corrected_days % 7
    
    corrected_months = total_corrected_days // 30 # Aproximação

    return {'weeks': final_weeks, 'months': corrected_months, 'days': final_days}

def display_results(chronological_age, corrected_age):
    """
    Exibe os resultados na interface.
    """
    result_text = (
        f"Idade Cronológica: {chronological_age['weeks']} semanas ({chronological_age['months']} meses)\n"
        f"Idade Corrigida: {corrected_age['weeks']} semanas ({corrected_age['months']} meses) e {corrected_age['days']} dias"
    )
    result_var.set(result_text)

def clear_fields():
    """
    Limpa os campos de entrada e o resultado.
    """
    birthdate_entry.delete(0, 'end')
    gestational_age_entry.delete(0, 'end')
    gestational_age_days_entry.delete(0, 'end')
    result_var.set("")

# Configuração da janela principal
root = Tk()
root.title("Calculadora de Idade do Bebê")
root.geometry("450x350")
root.resizable(False, False)

# Configuração dos widgets (elementos da interface)
main_frame = Frame(root, padx=20, pady=20)
main_frame.pack(expand=True)

title_label = Label(main_frame, text="Calculadora de Idade do Bebê", font=("Verdana", 16, "bold"))
title_label.pack(pady=10)

# Campo Data de Nascimento
birthdate_label = Label(main_frame, text="Data de Nascimento (YYYY-MM-DD):", font=("Verdana", 10))
birthdate_label.pack()
birthdate_entry = Entry(main_frame, width=30)
birthdate_entry.pack(pady=5)

# Campo Idade Gestacional (Semanas)
gestational_age_label = Label(main_frame, text="Idade Gestacional (semanas):", font=("Verdana", 10))
gestational_age_label.pack()
gestational_age_entry = Entry(main_frame, width=30)
gestational_age_entry.pack(pady=5)

# Campo Dias na Semana
gestational_age_days_label = Label(main_frame, text="Dias na Semana de Nascimento:", font=("Verdana", 10))
gestational_age_days_label.pack()
gestational_age_days_entry = Entry(main_frame, width=30)
gestational_age_days_entry.pack(pady=5)

# Contêiner para os botões
button_frame = Frame(main_frame)
button_frame.pack(pady=10)

# Botões
calculate_button = Button(button_frame, text="Calcular", command=calculate_age, width=15, bg="#0000ff", fg="#f8f7f4")
calculate_button.pack(side="left", padx=5)

clear_button = Button(button_frame, text="Limpar", command=clear_fields, width=15, bg="#0000ff", fg="#f8f7f4")
clear_button.pack(side="left", padx=5)

# Área de resultado
result_var = StringVar()
result_label = Label(main_frame, textvariable=result_var, font=("Verdana", 10), justify="center")
result_label.pack(pady=10)

# Iniciar o loop principal da interface
root.mainloop()