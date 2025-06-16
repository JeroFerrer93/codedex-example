# transcriptor_de_audios.py

import os
import whisper # type: ignore
import tkinter as tk
from tkinter import filedialog, messagebox

def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    file_path = filedialog.askopenfilename(
        title="Selecciona un archivo de audio",
        filetypes=[("Archivos de audio", "*.mp3 *.wav *.m4a *.ogg *.flac")]
    )
    return file_path

def transcribir_audio(audio_file_path):
    if not os.path.exists(audio_file_path):
        raise FileNotFoundError("Archivo no encontrado.")

    print(f"Archivo seleccionado: {audio_file_path}")

    print("Cargando modelo de Whisper...")
    model = whisper.load_model("small")  # Cambiar a "medium" o "large" si querés mayor precisión

    print("Transcribiendo el audio...")
    result = model.transcribe(audio_file_path, language="es")

    transcripcion = result["text"]
    print("\n--- TRANSCRIPCIÓN ---\n")
    print(transcripcion)

    # Guardar resultado
    output_path = "transcripcion.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(transcripcion)

    print(f"\n✅ Transcripción guardada en: {output_path}")

if __name__ == "__main__":
    try:
        audio_path = seleccionar_archivo()
        if audio_path:
            transcribir_audio(audio_path)
        else:
            print("No se seleccionó ningún archivo.")
    except Exception as e:
        messagebox.showerror("Error", str(e))
