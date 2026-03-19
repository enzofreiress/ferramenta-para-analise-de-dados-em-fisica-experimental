import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import io
import pandas as pd
from scipy.stats import chi2

def f(a,b,x):

    #definindo a função de ajuste

    y=a*x+b

    return y


def main():

    fig=plt.figure(figsize=(6,6))

    #carregar arquivo

    x,y = np.loadtxt('ajuste_linearH.txt',unpack=True)

    popt,pcov = curve_fit(f,x,y,p0=None,sigma=None,absolute_sigma=False)    

    a,b = popt
    a_incerteza = np.sqrt(pcov[0,0])
    b_incerteza=np.sqrt(pcov[1,1])


    x_ajuste=np.linspace(min(x),max(x))
    y_ajuste=f(x_ajuste,a,b)


    ax1 =fig.add_axes([0,0.25,1,0.75])
    
    
        #APENAS SE TIVERMOS INCERTEZAS ASSOCIADAS 
    #ax1.errorbar(x,y,xerr=x,yerr=y,fmt='o',color='red',ecolor='black',ms=0.1,capsize=0.2, label=  "Dados")

    ax1.plot(x,y,'o',color='green',label='Dados')
    ax1.plot(x_ajuste,y_ajuste,color='red',label=f'Ajuste: $y={a:.2f}x + {b:.2f}$', linewidth=0.5)
    ax1.legend()
    ax1.set_ylabel('Eixo Y')
    ax1.set_title('Titulo')
    ax1.grid(True,linestyle='-',alpha=0.7)
    

    y_ajuste=f(x,a,b)
    distancias=y-y_ajuste

    # Segundo subplot
    ax2 = fig.add_axes([0, 0, 1, 0.25])
    ax2.axhline(0, color='red', linestyle='-', linewidth=1.5)


    # ax2.errorbar(x, distancias, yerr=iy, fmt='o', color='black', ecolor='red', capsize=3)
    
    
    ax2.set_xlabel('EIXO X')     #legenda eixo x
    ax2.legend()
    ax2.grid(True, linestyle='-', alpha=0.7)

    #chi^2
    #chi2_valor = np.sum(((distancias) / iy) ** 2)
    # Graus de liberdade
    n_dados = len(y)
    n_parametros = 2  #********substitua número de parâmetros
    graus_de_liberdade = n_dados - n_parametros
    # Valor crítico
    alfa = 0.01
    valor_critico = chi2.ppf(1 - alfa, graus_de_liberdade)

    #print(f"Valor do χ²: {chi2_valor:.2f}")
    print(f"Graus de liberdade: {graus_de_liberdade}")
    print(f"Valor crítico (alfa={alfa}): {valor_critico:.2f}")
    #if chi2_valor > valor_critico:
    #    print("os dados diferem significativamente do modelo.")
    #else:
    #    print("os dados não diferem significativamente do modelo.")

    plt.show()



main()