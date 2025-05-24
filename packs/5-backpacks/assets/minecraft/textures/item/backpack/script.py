from PIL import Image
import os

def adjust_opacity_to_max():
    # Obtener el directorio actual del script
    current_dir = os.getcwd()
    
    # Iterar sobre todos los archivos en el directorio actual
    for filename in os.listdir(current_dir):
        if filename.endswith('.png'):  # Verificar que el archivo sea PNG
            filepath = os.path.join(current_dir, filename)
            try:
                # Abrir la imagen
                img = Image.open(filepath).convert("RGBA")
                pixels = img.load()

                # Modificar la opacidad de todos los píxeles a 255
                for y in range(img.height):
                    for x in range(img.width):
                        r, g, b, a = pixels[x, y]
                        pixels[x, y] = (r, g, b, 255)

                # Guardar la imagen modificada (sobrescribiendo la original)
                img.save(filepath)
                print(f"Opacidad ajustada en: {filename}")
            except Exception as e:
                print(f"No se pudo procesar {filename}: {e}")

if __name__ == "__main__":
    adjust_opacity_to_max()
