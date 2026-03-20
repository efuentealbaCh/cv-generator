import json
from jinja2 import Environment, FileSystemLoader

def main():
    # 1. Cargar los datos desde el archivo JSON
    with open('cv_data.json', 'r', encoding='utf-8') as f:
        cv_data = json.load(f)

    # 2. Configurar Jinja2 para buscar plantillas en el directorio actual
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')

    # 3. Generar el HTML final inyectando el JSON
    html_output = template.render(cv_data)

    # 4. Guardar el resultado en un nuevo archivo
    output_filename = 'CV_Generado.html'
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(html_output)

    print(f"¡Éxito! El currículum se ha generado en '{output_filename}'.")
    print("Ábrelo en tu navegador y usa la opción 'Imprimir -> Guardar como PDF'.")

if __name__ == "__main__":
    main()