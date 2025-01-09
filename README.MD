# Eliminar Fondo de Imágenes con Python 🚀

Este proyecto permite a los usuarios subir imágenes y eliminar automáticamente el fondo usando el paquete Python `rembg`. Los usuarios pueden cargar hasta 3 imágenes a la vez y recibir los resultados como archivos procesados para descargar.

## Resultado final

![](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/refs/heads/master/eliminar-fondo-de-imagenes-con-python.png)


## Características

- **Subida de imágenes**: Los usuarios pueden seleccionar y cargar imágenes en formato `.jpg`, `.jpeg`, o `.png`.
- **Eliminación de fondo**: Utiliza el paquete `rembg` para eliminar el fondo de las imágenes cargadas.
- **Procesamiento de múltiples imágenes**: Permite cargar hasta 3 imágenes y las procesará simultáneamente.
- **Descarga de imágenes procesadas**: Si solo se procesa una imagen, se descarga directamente. Si son varias, las imágenes procesadas se envían como un archivo ZIP.
- **Mensajes Flash**: El proyecto muestra mensajes flash para informar al usuario sobre el estado de la carga y el procesamiento de las imágenes.

## Tecnologías

- **Flask**: Framework web de Python para crear el servidor y manejar las rutas.
- **PIL (Pillow)**: Para manejar imágenes en Python.
- **rembg**: Herramienta para eliminar el fondo de las imágenes.
- **Bootstrap 5**: Para el diseño y las alertas interactivas en la interfaz de usuario.

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/urian121/eliminar-fondo-de-imagenes-con-Python
   ```

2. Instala las dependencias:
   ```bash
    pip install -r requirements.txt
   ```

3. Crea las carpetas necesarias para almacenar las imágenes cargadas y procesadas:
```bash
    mkdir uploads processed
   ```

4. Ejecuta el servidor:
   ```bash
    python app.py
   ```

5. Accede al proyecto en tu navegador en http://127.0.0.1:5000


### Expresiones de Gratitud 🎁

    Comenta a otros sobre este proyecto 📢
    Invita una cerveza 🍺 o un café ☕
    Paypal iamdeveloper86@gmail.com
    Da las gracias públicamente 🤓.
   Y no olvides dejar tu estrella ⭐ en el repositorio, ¡dicen que trae buena suerte! 🍀  

## No olvides SUSCRIBIRTE 👍
