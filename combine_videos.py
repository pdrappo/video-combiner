import os
from moviepy.editor import VideoFileClip, concatenate_videoclips
from pathlib import Path

INPUT_DIR = Path("input")
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

def combine_videos_in_folder(folder_path: Path):
    """Combina todos los .mp4 dentro de una carpeta en un solo video"""
    mp4_files = sorted(folder_path.glob("*.mp4"))  # ordenados alfabéticamente

    if not mp4_files:
        print(f"⚠️ No se encontraron videos en {folder_path}")
        return

    print(f"📂 Procesando carpeta: {folder_path}")
    print(f"🎬 Archivos: {[f.name for f in mp4_files]}")

    # Cargar videos
    clips = [VideoFileClip(str(f)) for f in mp4_files]

    # Concatenar
    final = concatenate_videoclips(clips, method="compose")

    # Nombre de salida
    output_file = OUTPUT_DIR / f"{folder_path.name}_combined.mp4"

    # Exportar
    final.write_videofile(
        str(output_file),
        codec="libx264",
        audio_codec="aac",
        temp_audiofile="temp-audio.m4a",
        remove_temp=True
    )

    print(f"✅ Video exportado en {output_file}")


def main():
    # Buscar todas las subcarpetas dentro de input/
    for folder in INPUT_DIR.iterdir():
        if folder.is_dir():
            combine_videos_in_folder(folder)


if __name__ == "__main__":
    main()
