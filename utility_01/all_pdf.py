from pathlib import Path
from datetime import datetime

def list_pdf(directory, output_file):
    """Liste tous les fichiers et répertoires dans un chemin donné et écrit les résultats dans un fichier texte."""
    with open(output_file, 'w') as f:
        for path in Path(directory).rglob('*.pdf'):
            f.write(str(path) + '\n')

# main exec
if __name__ == "__main__":
    directory_to_list = Path.home()  # Vous pouvez changer ceci pour n'importe quel chemin
    current_time = datetime.now().strftime("%d-%m-%Y_%H%M%S")
    output_file = f'list_pdf_files{current_time}.txt'  # Nom du fichier avec la date et l'heure
    list_pdf(directory_to_list, output_file)
    print(f"Liste des fichiers: {output_file}")
