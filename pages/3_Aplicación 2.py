import matplotlib.pyplot as plt

def main():
    # Datos ficticios: Categorías y valores
    categorias = ['Categoría A', 'Categoría B', 'Categoría C', 'Categoría D']
    valores = [15, 24, 30, 8]
    
    # Crear un gráfico de barras
    plt.bar(categorias, valores, color='skyblue')
    
    # Personalizar el gráfico
    plt.title('Gráfico de Barras')
    plt.xlabel('Categorías')
    plt.ylabel('Valores')
    
    # Mostrar el gráfico
    plt.show()

if __name__ == "__main__":
    main()
