# Traductor de Texto por Captura de Pantalla

Este proyecto es una herramienta que permite capturar texto directamente desde la pantalla, realizar el reconocimiento óptico de caracteres (OCR) y traducir el texto detectado de inglés a español de forma automática. Es especialmente útil para traducir rápidamente contenido visual sin necesidad de copiar y pegar manualmente.

## Características

- **Captura de texto desde la pantalla:** Selecciona un área en la pantalla para realizar el OCR.
- **Reconocimiento de texto:** Utiliza Tesseract OCR para extraer el texto de las imágenes capturadas.
- **Traducción automática:** Traduce el texto detectado del inglés al español usando la API de Google Translator.
- **Interfaz intuitiva:** Ventana emergente para seleccionar áreas y mostrar la traducción.
- **Atajos de teclado:** Controla las funciones del programa con combinaciones de teclas.

## Requisitos

- Python 3.8 o superior.
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) instalado en el sistema.
- Las siguientes bibliotecas de Python:
  - `pytesseract`
  - `Pillow`
  - `keyboard`
  - `tkinter` (incluido en la instalación estándar de Python)
  - `deep-translator`

## Instalación

1. **Instalar Tesseract OCR:**
   - Descarga e instala [Tesseract OCR](https://github.com/tesseract-ocr/tesseract).
   - Asegúrate de anotar la ruta de instalación (usualmente `C:\Program Files\Tesseract-OCR\tesseract.exe`).

2. **Instalar dependencias de Python:**
   ```bash
   Python install_requirements.py
