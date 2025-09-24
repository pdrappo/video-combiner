# Video Combiner 🎬

Proyecto en Python para combinar múltiples videos `.mp4` en uno solo.  
Cada subcarpeta dentro de `input/` se combina en un único archivo dentro de `output/`.

---

## 🚀 Uso

1. Clonar el repositorio y entrar en la carpeta:

```bash
   cd video-combiner
```

2. Crear entorno virtual (opcional pero recomendado):

```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate      # Windows
```

3. Instalar dependencias:

```bash
   pip install -r requirements.txt
```   

4. Ejecutar
```bash
   python combine_videos.py
``` 

## Notas

- Los videos se concatenan en orden alfabético.

- Si los videos tienen diferentes resoluciones, se ajustan automáticamente.

- El códec usado es libx264 con audio aac (compatibles en la mayoría de reproductores).