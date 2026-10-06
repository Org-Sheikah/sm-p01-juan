import os

# Crear la carpeta public donde se guardará la página
os.makedirs("public", exist_ok=True)

# Código HTML interactivo con campos de texto, botón y JavaScript
html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora Interactiva</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #0d1117;
            color: #c9d1d9;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
        }
        .card {
            background: #161b22;
            border: 1px solid #30363d;
            padding: 30px;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.5);
            width: 320px;
        }
        h1 {
            color: #58a6ff;
            font-size: 1.4rem;
            margin-bottom: 20px;
        }
        .input-group {
            margin-bottom: 15px;
            text-align: left;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-size: 0.9rem;
            color: #8b949e;
        }
        input[type="number"] {
            width: 100%;
            padding: 10px;
            border-radius: 6px;
            border: 1px solid #30363d;
            background-color: #0d1117;
            color: #c9d1d9;
            font-size: 1rem;
            box-sizing: border-box;
        }
        button {
            width: 100%;
            padding: 10px;
            background-color: #238636;
            color: white;
            border: none;
            border-radius: 6px;
            font-size: 1rem;
            font-weight: bold;
            cursor: pointer;
            margin-top: 10px;
        }
        button:hover {
            background-color: #2ea043;
        }
        .result {
            font-size: 1.4rem;
            color: #3fb950;
            font-weight: bold;
            margin-top: 20px;
            padding: 12px;
            background: #0d1117;
            border-radius: 6px;
            border: 1px solid #30363d;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>🧮 Calculadora de Suma</h1>
        <div class="input-group">
            <label for="num1">Primer Número:</label>
            <input type="number" id="num1" placeholder="Ej. 10" value="0">
        </div>
        <div class="input-group">
            <label for="num2">Segundo Número:</label>
            <input type="number" id="num2" placeholder="Ej. 25" value="0">
        </div>
        <button onclick="calcularSuma()">Sumar Números</button>
        <div class="result" id="resultado">Resultado: 0</div>
    </div>

    <script>
        function calcularSuma() {
            const val1 = parseFloat(document.getElementById('num1').value) || 0;
            const val2 = parseFloat(document.getElementById('num2').value) || 0;
            const suma = val1 + val2;
            document.getElementById('resultado').innerText = 'Resultado: ' + suma;
        }
    </script>
</body>
</html>
"""

with open("public/index.html", "w", encoding="utf-8") as f:
    f.write(html_content)
print("Página interactiva generada con éxito en public/index.html")