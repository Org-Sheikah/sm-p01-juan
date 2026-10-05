import os

num1 = 15
num2 = 25
resultado = num1 + num2

# Crear la carpeta public donde estará la página
os.makedirs("public", exist_ok=True)

# Contenido HTML con diseño
html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Resultado de la Suma</title>
    <style>
        body {{ font-family: Arial, sans-serif; background-color: #0d1117; color: #c9d1d9; text-align: center; padding: 50px; }}
        .card {{ background: #161b22; border: 1px solid #30363d; padding: 30px; border-radius: 12px; display: inline-block; }}
        h1 {{ color: #58a6ff; }}
        .result {{ font-size: 2.2em; color: #3fb950; font-weight: bold; margin-top: 15px; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>🧮 Resultado Calculado con Python</h1>
        <p>Número 1: <strong>{num1}</strong></p>
        <p>Número 2: <strong>{num2}</strong></p>
        <div class="result">Suma Total = {resultado}</div>
    </div>
</body>
</html>
"""

with open("public/index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Página web generada correctamente en public/index.html")