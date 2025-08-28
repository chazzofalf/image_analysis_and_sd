import subprocess
from PIL import Image

def describe_image(image_path, model_name):
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
        
        return description

    except FileNotFoundError:
        return f"Error: Image file not found at {image_path}"
    except subprocess.CalledProcessError as e:
        return f"Error running Ollama: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def multiple_describe_image(image_path):
    models = ["gemma3:27b", "llava:latest", "llama4:scout", "mistral-small3.2:24b", "Moondream:latest", "llama3.2-vision:latest"]
    results = []
    for model in models:
        results.append(describe_image(image_path, model))
    return results

def summarize_descriptions(descriptions):
    try:
        command = [
            "ollama",
            "run",
            "gpt-oss:120b",
            "--",
            "Combine the following descriptions into a single, very long and detailed exhaustive description:",
            "\n".join(descriptions)
        ]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        summary = result.stdout
        return summary
    except Exception as e:
        return f"Error summarizing descriptions: {e}"

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python image_describer2.py <image_path> <output_file>")
    else:
        image_path = sys.argv[1]
        output_file = sys.argv[2]
        descriptions = multiple_describe_image(image_path)
        summary = summarize_descriptions(descriptions)
        with open(output_file, "w") as f:
            f.write(summary)
        print(f"Summary written to {output_file}")
