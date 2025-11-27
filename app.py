from dash import Dash, html

# Inicializa o app
app = Dash(__name__)

# Define o layout com a mensagem
app.layout = html.Div(
    children=[
        html.H1("Hello Time Tech&Inovação")
    ]
)

# Roda o servidor
if __name__ == "__main__":
    app.run_server(debug=True, port=8080)


