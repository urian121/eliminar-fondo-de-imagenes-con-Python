from flask import Flask, flash, render_template, request, send_file, jsonify, redirect, url_for
from PIL import Image
from rembg import remove
import os

app = Flask(__name__)
app.secret_key = '454ghgghfg8h9fghjnrjtr'

# Carpeta para guardar las imágenes cargadas y procesadas
UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

# Crear carpetas si no existen
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_image():
    if 'image' not in request.files or not request.files.getlist('image'):
        flash('No se seleccionó ninguna imagen', 'error')
        return redirect(url_for('index'))

    # Obtener las imágenes cargadas
    files = request.files.getlist('image')
    
    # Validar que no sean más de 3 imágenes
    if len(files) > 3:
        flash('Máximo puedes subir 3 imágenes.', 'error')
        return redirect(url_for('index'))

    processed_files = []
    for file in files:
        if file.filename == '':
            continue

        input_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        output_path = os.path.join(app.config['PROCESSED_FOLDER'], f"processed_{file.filename}")

        # Guardar la imagen cargada
        file.save(input_path)

        # Eliminar el fondo de la imagen
        with open(input_path, 'rb') as inp_file:
            input_data = inp_file.read()
            output_data = remove(input_data)

        # Guardar la imagen procesada
        with open(output_path, 'wb') as out_file:
            out_file.write(output_data)

        processed_files.append(output_path)

    # Retornar las imágenes procesadas como archivos descargables
    if len(processed_files) == 1:
        return send_file(processed_files[0], as_attachment=True)
    else:
        # Crear un zip si hay múltiples archivos
        zip_path = os.path.join(app.config['PROCESSED_FOLDER'], 'processed_images.zip')
        from zipfile import ZipFile
        with ZipFile(zip_path, 'w') as zipf:
            for file_path in processed_files:
                zipf.write(file_path, os.path.basename(file_path))
        return send_file(zip_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
