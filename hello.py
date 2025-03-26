import io
import time
from datetime import datetime

import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.sidebar.success("Select a demo above.")

# 1. Títulos e Texto
titulo = "Aula Introdutória ao Streamlit"
st.title(titulo)  # Exibe o título da aplicação

cabecalho = "Aprendendo os Principais Métodos"
st.header(cabecalho)  # Exibe um cabeçalho

# Exibição de Texto
subcabecalho_texto = "Métodos de Exibição de Texto"
st.subheader(subcabecalho_texto)  # Exibe um subcabeçalho

# Exibe um texto simples
texto_simples = (
    "Streamlit facilita a criação de aplicações web interativas com Python."
)
st.text(texto_simples)  # Exibe um texto simples

# Exibe um texto em markdown
texto_markdown = "### Este é um texto em **markdown**!"
st.markdown(texto_markdown)  # Exibe texto formatado usando Markdown

# Exibe uma fórmula em LaTeX
formula_latex = r""" e^{i\pi} + 1 = 0 """
st.latex(formula_latex)  # Exibe uma fórmula matemática usando LaTeX

# Exibe um código
codigo_exemplo = "x = 42"
st.code(
    codigo_exemplo, language="python"
)  # Exibe um trecho de código com destaque de sintaxe

# 2. Exibição de Dados
subcabecalho_dados = "Exibição de Dados"
st.subheader(subcabecalho_dados)  # Exibe um subcabeçalho

# Cria um DataFrame e exibe-o de várias formas
data = {"A": [1, 2, 3, 4], "B": [10, 20, 30, 40]}
df = pd.DataFrame(data)

# Exibe o DataFrame usando o método write
st.write(
    "Aqui está um dataframe:", df
)  # Exibe o DataFrame com formatação padrão

# Exibe o DataFrame usando o método dataframe
st.dataframe(df)  # Exibe o DataFrame com opções de redimensionamento

# Exibe o DataFrame usando o método table
st.table(df)  # Exibe o DataFrame como uma tabela estática

# Exibe um JSON
json_exemplo = {"name": "Streamlit", "type": "Web Framework"}
st.json(json_exemplo)  # Exibe um objeto JSON

# Exibe um CSV como string
csv_exemplo = df.to_csv(index=False)
st.write("Exibindo CSV:", csv_exemplo)  # Exibe o DataFrame como CSV

# Exibe uma lista
lista_exemplo = [1, 2, 3, 4, 5]
st.write("Lista de números:", lista_exemplo)  # Exibe uma lista

# 3. Métricas
subcabecalho_metricas = "Métricas"
st.subheader(subcabecalho_metricas)  # Exibe um subcabeçalho

#------------------------------------------------
#Exibindo visual de Cards na Horizontal
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
# Exibe uma métrica com delta (diferença)
    st.metric(label="Temperatura", value="70 °F", delta="1.2 °F")  # Exibe uma métrica com delta (mudança)

with col2:
# Exibe mais métricas com diferentes valores e deltas
    st.metric(label="Umidade", value="60%", delta="-5%")

with col3:    
    st.metric(label="Velocidade do Vento", value="15 km/h", delta="2 km/h")

with col4:
    st.metric(label="Nível de Ruído", value="40 dB", delta="1.5 dB")

with col5:
    st.metric(label="Pressão Atmosférica", value="1013 hPa", delta="2 hPa")

#------------------------------------------------
#Exibindo visual de Cards na Vertical

# st.metric(label="Umidade", value="60%", delta="-5%")
# st.metric(label="Velocidade do Vento", value="15 km/h", delta="2 km/h")
# st.metric(label="Nível de Ruído", value="40 dB", delta="1.5 dB")
# st.metric(label="Pressão Atmosférica", value="1013 hPa", delta="2 hPa")



# Exibe uma métrica sem delta
st.metric(label="População", value="8 bilhões")

# 4. Gráficos
subcabecalho_graficos = "Gráficos"
st.subheader(subcabecalho_graficos)  # Exibe um subcabeçalho

# Cria e exibe gráficos de linha, área e barra
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)  # Exibe um gráfico de linha
st.area_chart(chart_data)  # Exibe um gráfico de área
st.bar_chart(chart_data)  # Exibe um gráfico de barra

# Mais exemplos de gráficos
mais_graficos = "Mais Exemplos de Gráficos"
st.subheader(mais_graficos)  # Exibe um subcabeçalho

# Gráfico de dispersão
scatter_data = pd.DataFrame(np.random.randn(100, 2), columns=["x", "y"])
st.plotly_chart(
    {
        "data": [
            {
                "x": scatter_data["x"],
                "y": scatter_data["y"],
                "type": "scatter",
                "mode": "markers",
            }
        ],
        "layout": {"title": "Gráfico de Dispersão"},
    }
)  # Exibe um gráfico de dispersão

# Histograma
hist_data = np.random.randn(1000)
st.plotly_chart(
    {
        "data": [{"x": hist_data, "type": "histogram"}],
        "layout": {"title": "Histograma"},
    }
)  # Exibe um histograma

# 5. Mapas
subcabecalho_mapas = "Mapas"
st.subheader(subcabecalho_mapas)  # Exibe um subcabeçalho

# Cria e exibe um mapa
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"],
)
st.map(map_data)  # Exibe um mapa com pontos aleatórios

# 6. Mídia
subcabecalho_midia = "Mídia"
st.subheader(subcabecalho_midia)  # Exibe um subcabeçalho

# Exibe uma imagem
imagem_url = "https://www.streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png"
imagem_legenda = "Streamlit Logo"
st.image(imagem_url, caption=imagem_legenda)  # Exibe uma imagem com legenda

# Exibe um áudio
audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
st.audio(audio_url)  # Exibe um reprodutor de áudio

# Exibe um vídeo
video_url = "https://www.youtube.com/watch?v=B2iAodr0fOo"
st.video(video_url)  # Exibe um reprodutor de vídeo

# 7. Widgets
subcabecalho_widgets = "Widgets"
st.subheader(subcabecalho_widgets)  # Exibe um subcabeçalho

# Botão - Exibe um botão que, ao ser clicado, mostra uma mensagem
if st.button("Clique aqui"):
    st.write("Botão clicado!")  # Mensagem exibida ao clicar no botão

# Checkbox - Exibe uma caixa de seleção
aceita_termos = st.checkbox("Eu aceito os termos e condições")
st.write("Aceita os termos:", aceita_termos)  # Exibe o valor selecionado

# Radio - Exibe opções de escolha única
opcao_radio = st.radio("Escolha uma opção", ("Opção 1", "Opção 2", "Opção 3"))
st.write("Opção escolhida:", opcao_radio)  # Exibe a opção selecionada

# Selectbox - Exibe um menu suspenso para selecionar uma opção
opcao_selectbox = st.selectbox(
    "Selecione uma opção", ["Opção A", "Opção B", "Opção C"]
)
st.write("Opção selecionada:", opcao_selectbox)  # Exibe a opção selecionada

# Multiselect - Exibe um menu suspenso para selecionar várias opções
opcoes_multiselect = st.multiselect(
    "Selecione múltiplas opções", ["Opção 1", "Opção 2", "Opção 3"]
)
st.write(
    "Opções selecionadas:", opcoes_multiselect
)  # Exibe as opções selecionadas

# Slider - Exibe uma barra deslizante para selecionar um valor
valor_slider = st.slider("Selecione um valor", 0, 100, 50)
st.write("Valor selecionado:", valor_slider)  # Exibe o valor selecionado

# Select Slider - Exibe uma barra deslizante com opções de texto
intervalo_slider = st.select_slider(
    "Selecione um intervalo", options=["a", "b", "c", "d"], value=("b", "c")
)
st.write(
    "Intervalo selecionado:", intervalo_slider
)  # Exibe o intervalo selecionado

# Text Input - Exibe uma caixa de entrada de texto
nome = st.text_input("Digite seu nome")
st.write("Nome digitado:", nome)  # Exibe o texto digitado

# Number Input - Exibe uma caixa de entrada de número
numero = st.number_input("Selecione um número", 0, 100)
st.write("Número selecionado:", numero)  # Exibe o número selecionado

# Text Area - Exibe uma área de texto
texto = st.text_area("Escreva um texto")
st.write("Texto digitado:", texto)  # Exibe o texto digitado

# Date Input - Exibe um seletor de data
data = st.date_input("Selecione uma data", datetime.now())
st.write("Data selecionada:", data)  # Exibe a data selecionada

# Sidebar
st.sidebar.title("Barra Lateral")  # Exibe o título da barra lateral
botao_sidebar = st.sidebar.button("Botão na Barra Lateral")
if botao_sidebar:
    st.sidebar.write(
        "Botão na barra lateral clicado!"
    )  # Mensagem exibida ao clicar no botão da barra lateral

# Carregar CSV
subcabecalho_csv = "Carregar CSV"
st.subheader(subcabecalho_csv)  # Exibe um subcabeçalho
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

if uploaded_file is not None:
    # Barra de progresso durante o upload
    progress_bar = st.progress(0)

    # Simulação do progresso de carregamento
    for i in range(100):
        time.sleep(0.01)
        progress_bar.progress(i + 1)

    # Lê o CSV
    csv_data = pd.read_csv(uploaded_file)
    st.write("Dados do CSV:")
    st.dataframe(csv_data)  # Exibe o conteúdo do arquivo CSV

    # Soltar balões após o upload
    st.balloons()

    # Função para converter DataFrame para Parquet
    @st.cache_data
    def convert_df_to_parquet(df):
        output = io.BytesIO()
        df.to_parquet(output, index=False)
        return output.getvalue()

    st.download_button(
        label="Baixar dados como Parquet",
        data=convert_df_to_parquet(csv_data),
        file_name="dados.parquet",
        mime="application/octet-stream",
    )