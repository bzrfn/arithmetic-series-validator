# Arithmetic Series Project

Proyecto en Python para validar si una lista de números corresponde a una **progresión aritmética** usando **Pandas**.

## Estructura

```text
arithmetic_series_project/
├── main.py
├── series_validator.py
├── requirements.txt
└── README.md
```

## Requisitos

- Python 3.10+
- Pandas

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
python main.py
```

## Salida esperada

```text
Serie: [2, 4, 6, 8, 10]
Es una progresión aritmética
Diferencia común: 2

Serie: [3, 7, 10, 15]
No es una progresión aritmética
```

## Descripción técnica

La clase `ArithmeticProgressionValidator`:

- Usa `pandas.Series`
- Calcula diferencias consecutivas con `diff()`
- Verifica si todas las diferencias son iguales
- Devuelve la diferencia común cuando la serie es válida

## Archivo principal

`main.py` ejecuta dos pruebas:

1. Una serie válida
2. Una serie inválida
