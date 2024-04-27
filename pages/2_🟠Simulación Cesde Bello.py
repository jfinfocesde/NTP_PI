import numpy as np
import streamlit as st
import pandas as pd
import plotly.figure_factory as ff

import plotly.graph_objects as go

# Set the page title and header
st.title("Simulador CESDE Bello")
st.header("Esta aplicación simula la gestión de notas y horarios para todos los grupos de la sede Bello del CESDE.")

df = pd.read_csv('datasets\cesde.csv')

gruposU = sorted(df['GRUPO'].unique())
nivelesU = sorted(df['NIVEL'].unique())
jornadasU = df['JORNADA'].unique()
horarioU = df['HORARIO'].unique()
submodulosU = df['SUBMODULO'].unique()
docentesU = df['DOCENTE'].unique()
momentosU = df['MOMENTO'].unique()


tab1, tab2 = st.tabs(["Notas", "Docentes"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        gruposU.insert(0,"Todos")
        optionGrupo = st.selectbox('Grupo', (gruposU))
    with col2:       
        optionMomento = st.selectbox('Momento', (momentosU))
    notas_conocimiento = None
    if optionGrupo != 'Todos':
        notas_conocimiento = df[(df['GRUPO']==optionGrupo)&(df['MOMENTO']==optionMomento)]
    else :
        notas_conocimiento = df[df['MOMENTO']==optionMomento]

     # Create the bar chart
    if notas_conocimiento is not None:
        # Select the relevant column for the bar chart (e.g., 'CONOCIMIENTO')
        chart_data = pd.DataFrame(notas_conocimiento, columns=["CONOCIMIENTO", "DESEMPEÑO", "PRODUCTO"])
        # chart_data = notas_conocimiento['CONOCIMIENTO'].value_counts()
        st.line_chart(chart_data)


        # Group data together
        hist_data = [notas_conocimiento['CONOCIMIENTO'], notas_conocimiento['DESEMPEÑO'], notas_conocimiento['PRODUCTO']]

        group_labels = ['CONOCIMIENTO', 'DESEMPEÑO', 'PRODUCTO']

        # # Add histogram data
        # x1 = np.random.randn(200) - 2
        # x2 = np.random.randn(200)
        # x3 = np.random.randn(200) + 2

        # # Group data together
        # hist_data = [x1, x2, x3]

        # group_labels = ['Group 1', 'Group 2', 'Group 3']

        # Create distplot with custom bin_size
        fig = ff.create_distplot(
                hist_data, group_labels, bin_size=[5, 5, 5])

        # Plot!
        st.plotly_chart(fig, use_container_width=True)


        NOTAS=notas_conocimiento['NOMBRE']
        # NOTAS
        # notas_conocimiento['CONOCIMIENTO']

        fig = go.Figure(data=[
            go.Bar(name='CONOCIMIENTO', x=NOTAS, y=notas_conocimiento['CONOCIMIENTO']),
            go.Bar(name='DESEMPEÑO', x=NOTAS, y=notas_conocimiento['DESEMPEÑO']),
            go.Bar(name='PRODUCTO', x=NOTAS, y=notas_conocimiento['PRODUCTO'])
        ])
        # Change the bar mode
        fig.update_layout(barmode='group')
        st.plotly_chart(fig, use_container_width=True)


    else:
        st.write("No hay datos disponibles para el grupo y momento seleccionados.")

    st.table(notas_conocimiento[['NOMBRE','CONOCIMIENTO','DESEMPEÑO','PRODUCTO']])

with tab2:
    nivelesU.insert(0,"Todos")
    option = st.selectbox('Nivel', (nivelesU))







