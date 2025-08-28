import subprocess
from PIL import Image

def describe_image(image_path, output_file, model_name="gemma3:27b"):
    try:
        # Open the image to validate it
        Image.open(image_path)
        
        # Run Ollama command to generate description
        command = [
            "ollama",
            "run",
            model_name,
            "--",
            "Describe this image in great detail.",
            "-i",
            image_path
        ]

        result = subprocess.run(command, capture_output=True, text=True, check=True)
        description = result.stdout
        
        # Write the description to the output file
        with open(output_file, "w") as f:
            f.write(description)
        
        print(f"Description written to {output_file}")

    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error running Ollama: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python image_describer2.py <image_path> <output_file>")
    else:
        image_path = sys.argv[1]
        output_file = sys.argv[2]
        describe_image(image_path, output_file)
