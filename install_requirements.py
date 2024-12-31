import os

def install_requirements():
    libraries = [
        "pytesseract",
        "Pillow",
        "keyboard",
        "tkinter",  # tkinter viene preinstalado en la mayoría de las distribuciones de Python.
        "deep-translator",
        "pywin32"
    ]

    for lib in libraries:
        try:
            os.system(f"pip install {lib}")
        except Exception as e:
            print(f"Error instalando {lib}: {e}")

    # Mensaje final
    print("\nInstalación completa. Si hubo errores, revísalos para solucionarlos.")

if __name__ == "__main__":
    install_requirements()
