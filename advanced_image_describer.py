import subprocess
import sys
from ollama_ls_parser import get_ollama_models_via_ls
def generate_description(model, image_path):
    try:
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()

        process = subprocess.Popen(
            ['ollama', 'run', model],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        stdout, stderr = process.communicate(input=image_data)

        if process.returncode != 0:
            error_message = f"!!!ERROR!!!: {stderr.decode('utf-8')}"
            return error_message
        else:
            return stdout.decode('utf-8')

    except Exception as e:
        return f"!!!ERROR!!!: {str(e)}"

def consolidate_descriptions(descriptions):
    return "\n".join(descriptions)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python advanced_image_describer.py <image_path> <output_file>")
        sys.exit(1)

    image_path = sys.argv[1]
    output_file = sys.argv[2]

    models = get_ollama_models_via_ls() # Gets Descriptions from ALL Models installed!

    descriptions = []
    for model in models:
        description = generate_description(model, image_path)
        descriptions.append(description)

    consolidated_description = consolidate_descriptions(descriptions)

    with open(output_file, "w") as f:
        f.write(consolidated_description)

    print(f"Consolidated description written to {output_file}")
