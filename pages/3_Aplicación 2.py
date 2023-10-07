import streamlit as st
import matplotlib.pyplot as plt

def main():
    # Datos ficticios: Categorías y valores
    categorias = ['Categoría A', 'Categoría B', 'Categoría C', 'Categoría D']
    valores = [15, 24, 30, 8]
    
    # Crear un gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(categorias, valores, color='skyblue')
    
    # Personalizar el gráfico
    ax.set_title('Gráfico de Barras')
    ax.set_xlabel('Categorías')
    ax.set_ylabel('Valores')
    
    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

if __name__ == "__main__":
    main()
