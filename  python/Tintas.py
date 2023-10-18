#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 14:01:36 2023

@author: ranieusousa
"""

# Entrada do tamanho da área
tamanho_area = float(input("Informe o tamanho da área a ser pintada em metros quadrados: "))

# Cálculo com latas de 18 litros
preco_lata = 80.00
litros_necessarios_latas = (tamanho_area / 6) * 1.1  # Adicionando 10% de folga
latas_necessarias_latas = -(-litros_necessarios_latas // 18)  # Arredonda para cima
preco_total_latas = latas_necessarias_latas * preco_lata

print(f"Comprar {latas_necessarias_latas} latas de 18 litros custará R${preco_total_latas:.2f}")

# Cálculo com galões de 3.6 litros
preco_galao = 25.00
litros_necessarios_galoes = (tamanho_area / 6) * 1.1  # Adicionando 10% de folga
galoes_necessarios_galoes = -(-litros_necessarios_galoes // 3.6)  # Arredonda para cima
preco_total_galoes = galoes_necessarios_galoes * preco_galao

print(f"Comprar {galoes_necessarios_galoes} galões de 3.6 litros custará R${preco_total_galoes:.2f}")

# Cálculo misturando latas e galões
litros_necessarios_misturado = (tamanho_area / 6) * 1.1  # Adicionando 10% de folga
latas_necessarias_misturado = int(litros_necessarios_misturado / 18)  # Latas inteiras
litros_resto = litros_necessarios_misturado % 18  # Litros restantes
galoes_necessarios_misturado = -(-litros_resto // 3.6)  # Galões necessários para o resto
preco_total_misturado = (latas_necessarias_misturado * preco_lata) + (galoes_necessarios_misturado * preco_galao)

print(f"Misturando {latas_necessarias_misturado} latas e {galoes_necessarios_misturado} galões, o custo total será R${preco_total_misturado:.2f}")
