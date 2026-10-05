import os

num1 = 15
num2 = 25
resultado = num1 + num2

# 1. Imprimir en la consola (Logs)
print("----------------------------------------")
print(f"El resultado de sumar {num1} + {num2} en Python es: {resultado}")
print("----------------------------------------")

# 2. Generar la página visual en GitHub Actions (Job Summary)
summary_file = os.environ.get('GITHUB_STEP_SUMMARY')

if summary_file:
    with open(summary_file, 'a', encoding='utf-8') as f:
        f.write(f"""
# 🧮 Reporte de Ejecución - Calculadora Python

| Operación | Valor |
| :--- | :--- |
| **Número 1** | `{num1}` |
| **Número 2** | `{num2}` |
| **Resultado final** | **`{resultado}`** |

> ✅ **Estado:** Cálculo ejecutado correctamente desde la carpeta `src/suma.py`.
""")