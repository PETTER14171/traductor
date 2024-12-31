import pytesseract
from PIL import ImageGrab, ImageDraw
import keyboard
import tkinter as tk
from tkinter import messagebox
from deep_translator import GoogleTranslator
import threading

# Configuración de Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Variables globales para la selección del rango
start_x, start_y, end_x, end_y = 0, 0, 0, 0
selection_complete = False
translation_window = None
text_widget = None
program_running = True

# Función para traducir texto
def translate_text(text):
    try:
        translated = GoogleTranslator(source='en', target='es').translate(text)
        return translated
    except Exception as e:
        return f"Error en la traducción: {e}"

# Función para capturar el rango seleccionado y extraer texto
def capture_and_translate():
    if not program_running:
        return

    def task():
        global start_x, start_y, end_x, end_y, selection_complete
        selection_complete = False

        # Ventana para seleccionar el área
        root = tk.Tk()
        root.attributes("-fullscreen", True)
        root.attributes("-alpha", 0.3)
        root.configure(bg="gray")

        canvas = tk.Canvas(root, cursor="cross", bg="gray")
        canvas.pack(fill=tk.BOTH, expand=True)

        def on_mouse_down(event):
            global start_x, start_y
            canvas.delete("selection")
            start_x, start_y = event.x, event.y

        def on_mouse_move(event):
            canvas.delete("selection")
            canvas.create_rectangle(start_x, start_y, event.x, event.y, outline="red", width=2, tag="selection")

        def on_mouse_up(event):
            global end_x, end_y, selection_complete
            end_x, end_y = event.x, event.y
            selection_complete = True
            root.destroy()

        canvas.bind("<Button-1>", on_mouse_down)
        canvas.bind("<B1-Motion>", on_mouse_move)
        canvas.bind("<ButtonRelease-1>", on_mouse_up)
        root.mainloop()

        if not selection_complete:
            return

        # Captura la región seleccionada
        bbox = (min(start_x, end_x), min(start_y, end_y), max(start_x, end_x), max(start_y, end_y))
        img = ImageGrab.grab(bbox)

        # Realiza el OCR
        text = pytesseract.image_to_string(img)

        if not text.strip():
            show_message("Traducción", "No se detectó texto para traducir.")
            return

        # Traduce el texto detectado
        translated_text = translate_text(text)

        # Muestra la traducción
        threading.Thread(target=update_translation, args=(translated_text,)).start()

    threading.Thread(target=task).start()

# Función para mostrar o actualizar la traducción
def update_translation(text):
    global translation_window, text_widget

    if translation_window is None or not translation_window.winfo_exists():
        translation_window = tk.Tk()
        translation_window.title("Traducción")

        text_widget = tk.Text(translation_window, wrap=tk.WORD, width=60, height=20)
        text_widget.pack(padx=10, pady=10)

        quit_button = tk.Button(translation_window, text="Salir", command=stop_program)
        quit_button.pack(pady=5)

    text_widget.config(state=tk.NORMAL)
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, text)
    text_widget.config(state=tk.DISABLED)

    translation_window.deiconify()
    translation_window.mainloop()

# Función para mostrar mensajes
def show_message(title, message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(title, message)
    root.destroy()

# Función para detener el programa
def stop_program():
    global program_running, translation_window
    program_running = False
    if translation_window is not None:
        translation_window.destroy()
    keyboard.unhook_all_hotkeys()

# Configuración del atajo de teclado
keyboard.add_hotkey('alt+i', capture_and_translate)
keyboard.add_hotkey('alt+q', stop_program)

# Ventana principal de la aplicación
def main():
    global program_running

    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal

    messagebox.showinfo("Instrucciones", "Presiona Alt+i para seleccionar un área y traducir el texto contenido en ella. Presiona Alt+Q para salir del programa.")

    while program_running:
        try:
            root.update()
        except tk.TclError:
            break

if __name__ == "__main__":
    main()



