
# 🧠 Chatbot Modular de Razonamiento Avanzado (TP3 - LLMs y Agentes)

Este proyecto implementa un **sistema de respuesta inteligente y razonamiento complejo** basado en un flujo modular de **6 agentes especializados**.  
Cada agente cumple una función distinta en el procesamiento de la pregunta, generando una respuesta robusta y revisada.

---

## 📋 Descripción general

- **Recepción de preguntas complejas:** El sistema recibe consultas que requieren búsqueda, análisis, soluciones y referencias.
- **Agentes especializados:** Se activan 6 agentes consecutivos para explorar, planificar, resolver, buscar información, sintetizar y revisar.
- **Estimación de tokens:** Mide el uso de tokens de entrada, salida, razonamiento y total (de forma estimada si no hay reporte real).
- **Resultados estructurados:** Muestra tanto la respuesta final como el detalle intermedio de cada etapa del razonamiento.

---

## 🏗️ Estructura del proyecto

| Archivo                  | Descripción |
|:--------------------------|:------------|
| `agent_module.py`         | Lógica de los 6 agentes y orquestación del flujo. |
| `razonamiento_app.py`     | Aplicación Streamlit para interactuar con el chatbot. |
| `requirements.txt`        | Dependencias necesarias para ejecutar el proyecto. |
| `README.md`               | Este archivo. |

---

## 🤖 Flujo de agentes

El sistema sigue el siguiente flujo modular:

1. **Explorador:** Analiza el contexto general de la pregunta.
2. **Estratega:** Propone métodos o enfoques de solución.
3. **Solucionador:** Busca soluciones concretas basadas en los enfoques.
4. **Investigador Web:** Nombra artículos, autores y referencias relevantes.
5. **Arquitecto:** Sintetiza toda la información en una respuesta estructurada.
6. **Revisor:** Revisa, refina y sugiere mejoras a la respuesta final.

---

## 🔧 Requisitos

### Software
- **Python 3.9 o superior**
- **Streamlit** para la interfaz gráfica.
- **LangChain** como framework de orquestación de agentes.
- **Groq API** como proveedor de LLMs (Llama 3 70B 8192).

### Instalación de bibliotecas

Instalar todas las dependencias ejecutando:

```bash
pip install -r requirements.txt
```

### Variables de entorno

Debes configurar las siguientes variables de entorno:

```bash
GROQ_API_KEY = "tu_api_key_de_groq"
GROQ_MODEL = "llama3-70b-8192"  # opcional
```

---

## 🚀 Ejecución

1. Ejecutar la aplicación Streamlit:

```bash
streamlit run razonamiento_app.py
```

2. Escribir preguntas como:
   - "¿Cuánta energía consumen los grandes modelos LLM y qué impacto ambiental tendrán en el futuro?"
   - "¿Qué superficie sería necesaria para abastecer el mundo con energía solar?"

El sistema responderá utilizando el razonamiento de los 6 agentes.

---

## 📚 Tecnologías utilizadas

- [Streamlit](https://streamlit.io/)
- [LangChain](https://python.langchain.com/)
- [Groq API](https://groq.com/)

---

## 👨‍💻 Autor

Trabajo realizado por **Omar López Cabrera** 

---
