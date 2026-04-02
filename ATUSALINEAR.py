import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import io
import pandas as pd
from scipy.stats import chi2
from scipy.signal import find_peaks
def f(x,a,b):

    #definindo a função de ajuste

    y=a*x+b

    return y

def main():

    fig=plt.figure(figsize=(6,6))

    #carregar arquivo

    x,y = np.loadtxt('Medida_4 H Melhor',unpack=True)

    popt,pcov = curve_fit(f,x,y,p0=None,sigma=None,absolute_sigma=False)    

    a,b = popt
    a_incerteza = np.sqrt(pcov[0,0])
    b_incerteza=np.sqrt(pcov[1,1])


    x_ajuste=np.linspace(min(x),max(x))
    y_ajuste=f(x_ajuste,a,b)

    
    
        #APENAS SE TIVERMOS INCERTEZAS ASSOCIADAS 
    #ax1.errorbar(x,y,xerr=x,yerr=y,fmt='o',color='red',ecolor='black',ms=0.1,capsize=0.2, label=  "Dados")

    y_ajuste=f(x,a,b)
    distancias=y-y_ajuste

    '''  # Segundo subplot
    ax2 = fig.add_axes([0, 0, 1, 0.25])
    ax2.axhline(0, color='red', linestyle='-', linewidth=1.5)

    #ax2.errorbar(x, distancias, yerr=iy, fmt='o', color='black', ecolor='red', capsize=3)
    
    
    ax2.set_xlabel('EIXO X')     #legenda eixo x
    ax2.legend()
    ax2.grid(True, linestyle='-', alpha=0.7)
    '''
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



    #gráfico com os picos da função

    picos, propriedades = find_peaks(y,
    height=2500,          
    distance=5,         
    prominence=0.05,    
    width=35,              
    rel_height=0.5   )
    

    
    
    plt.plot(x,y,'-',color='blue')
    plt.plot(x[picos], y[picos], "x", color='red', markersize=10)
    plt.legend()
    plt.ylabel('Intensidade')
    plt.xlabel('Pixels')
    plt.title('Intensidade x Pixels')
    plt.grid(True,linestyle='-',alpha=0.7)
    plt.show()
    


    x_picos=x[picos]
    y_picos=y[picos]

    y_pajuste=y_picos
    x_pajuste=x_picos
    


    popt,pcov = curve_fit(f,x_pajuste,y_pajuste,p0=None,sigma=None,absolute_sigma=False)

    a1,b1=popt
    
    y_ajustepicos=f(x_pajuste,a1,b1)

  
    plt.plot(x_pajuste,y_ajustepicos,'-',color='blue',label=(f'Dados: \n a={a1} \n b={b1}'))

    plt.plot(x_pajuste,y_pajuste,'o',color ='red')
    plt.legend()
    plt.grid(True,linestyle='-',alpha=0.7)
    plt.show()

    


main()