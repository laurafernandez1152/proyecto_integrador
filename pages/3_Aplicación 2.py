import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def main():
    # Datos ficticios: Categorías y valores
    categorias = ['Categoría A', 'Categoría B', 'Categoría C', 'Categoría D']
    valores = [15, 24, 30, 8]
    
    # Crear un DataFrame para facilitar el uso con st.bar_chart
    df = pd.DataFrame({'Categorías': categorias, 'Valores': valores})
    
    # Mostrar el gráfico de barras en Streamlit
    st.bar_chart(df.set_index('Categorías'))

    # Personalizar el gráfico (esto no es necesario en Streamlit)
    plt.title('Gráfico de Barras')
    plt.xlabel('Categorías')
    plt.ylabel('Valores')
    
if __name__ == "__main__":
    main()
