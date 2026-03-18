import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd

def ajuste(x, a, b):
    
    #INSIRA O AJUSTE AQUI
    
    y=a*x+b
    
    
    return y




def main():

    #insira abaixo, o diretório onde o arquivo está localizado na sua máquina, certifique-se que ele contém uma coluna para o eixo x e outro para o eixo y 
    eixo_x, eixo_y = np.loadtxt('Medida_4 H Melhor', unpack=True)
   
    # INCERTEZAS

    incerteza_y = np.array([0])
    incerteza_x = np.array([0])

    #A função que faz toda a mágica do programa

    #!lembre-se de adicionar o sigma = incerteza_y ao curve_fit para obtermos os valores corretos da incerteza
    
    popt, pcov = curve_fit(ajuste, eixo_x, eixo_y, absolute_sigma=True, p0=[0.4, 0.3])

    a, b = popt
    
    # CÁLCULO DAS INCERTEZAS DOS PARÂMETROS
    # A incerteza é a raiz quadrada da diagonal da matriz de covariância (pcov)
    perr = np.sqrt(np.diag(pcov))
    sigma_a, sigma_b = perr

    # RESIDUOS E CALCULOS FINAIS
    # Curva teórica
    y_model = ajuste(eixo_x, a, b)
    
    # Resíduos
    residuos = eixo_y - y_model

    # Chi-Quadrado
    chi2 = np.sum((residuos / incerteza_y)**2)
    ngl = len(eixo_y) - 3 # 3 parametros (a,b)
    chi2_red = chi2 / ngl

    # Printar resultados bonitinhos no terminal
    print("-" * 30)
    print("RESULTADOS DO AJUSTE")
    print("-" * 30)
    print(f"a = {a:.5f} +/- {sigma_a:.5f}")
    print(f"b = {b:.5f} +/- {sigma_b:.5f}")
    print("-" * 30)
    print(f"Chi² Reduzido: {chi2_red:.4f}")
    print("-" * 30)

    # PLOTAGEM (Gráfico Principal + Resíduos)
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(10, 8), gridspec_kw={'height_ratios': [3, 1]})
    
    # Curva suave para o desenho ficar bonito
    x_smooth_graus = np.linspace(min(eixo_x), max(eixo_x), 300)
    x_smooth_rad = np.deg2rad(x_smooth_graus)
    y_smooth = ajuste(x_smooth_rad, a, b)

    # GRÁFICO DO AJUSTE
    ax1.errorbar(eixo_x, eixo_y, yerr=incerteza_y, xerr=incerteza_x, fmt='o', 
                 color='black', ecolor='red', capsize=3, markersize=4, label='Dados Experimentais')
    ax1.plot(x_smooth_graus, y_smooth, 'b-', label='Ajuste Teórico')
    ax1.set_ylabel('Tensão (V)')
    ax1.set_title(f'Ajuste: a={a:.3f}, b={b:.3f}')
    ax1.legend()
    ax1.grid(True, linestyle='--', alpha=0.6)


    # GRÁFICO DE RESIDUOS
    ax2.errorbar(eixo_x, residuos, yerr=incerteza_y, fmt='o', color='black', ecolor='red', capsize=3, markersize=4)
    ax2.axhline(0, color='blue', linestyle='--') # Linha do zero
    ax2.set_xlabel('Ângulo (Graus)')
    ax2.set_ylabel('Resíduos (V)')
    ax2.grid(True, linestyle='--', alpha=0.6)

    #AJUSTE DE LAYOUT
    plt.tight_layout()
    plt.subplots_adjust(hspace=0.05) # Diminui espaço entre os gráficos
    plt.show()


main()