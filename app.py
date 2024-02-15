import pandas as pd
import plotly.express as px
import streamlit as st

# Carga de datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Anuncios de venta de coches')

# Crear una casilla de verificación para construir un histograma
build_histogram = st.checkbox('Construir un histograma')

# Crear una casilla de verificación para construir un gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

# Función para construir el histograma cuando se selecciona la casilla de verificación
if build_histogram:
    # Mensaje
    st.write('Construir un histograma para la columna odómetro')
    
    # Crear el histograma
    fig_histogram = px.histogram(car_data, x="odometer")
    
    # Mostrar el histograma
    st.plotly_chart(fig_histogram, use_container_width=True)

# Función para construir el gráfico de dispersión cuando se selecciona la casilla de verificación
if build_scatter:
    # Mensaje
    st.write('Construir un gráfico de dispersión para las columnas odómetro y precio')
    
    # Crear el gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    
    # Mostrar el gráfico de dispersión
    st.plotly_chart(fig_scatter, use_container_width=True)