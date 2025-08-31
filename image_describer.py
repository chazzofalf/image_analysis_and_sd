import subprocess
from PIL import Image
from ollama_ls_parser import get_ollama_models_via_ls
import os
from output_file_pair import OutputFilePair
from pathlib import Path
import ollama
import base64
import requests
def describe_image(image_path, model_name):
    PROMPT="""
You are an AI model with vision capabilities.  
Please open and examine the image located at **FILENAME_PLACEMARKER** and give a **comprehensive, exhaustive, and human‑readable description** 
of everything you see. If you cannot load or see the image. Stop right there and say nothing. (Blank output)

Otherwise,

In your description, be sure to cover at least the following points:

1. **Overall scene & context** – What is the general setting (indoor, outdoor, studio, nature, etc.)? What might be happening?
2. **Primary subjects** – Identify the main objects, people, animals, or structures. Mention their positions, poses, expressions, and any 
notable actions.
3. **Secondary elements** – List background items, props, or details that support the main subjects.
4. **Colors, textures & materials** – Note dominant colors, subtle hues, surface qualities (smooth, rough, glossy, matte, etc.), and any 
patterns.
5. **Lighting & shadows** – Describe the light source(s), direction, intensity, color temperature, and how shadows fall across the scene.
6. **Composition & perspective** – Comment on framing, camera angle, depth of field, focal length, rule‑of‑ thirds, leading lines, 
symmetry, or any artistic choices.
7. **Spatial relationships** – Explain how objects relate to each other in distance, scale, and orientation.
8. **Atmosphere & mood** – Infer the emotional tone, ambiance, or narrative suggested by the image (e.g., calm, chaotic, festive, 
somber).
9. **Potential context clues** – Any text, signage, timestamps, logos, or cultural references that hint at location, time period, 
or purpose.
10. **Any anomalies or notable details** – Highlight unusual features, imperfections, reflections, or hidden elements that a casual 
glance might miss.

Write the description in clear, natural language, using full sentences and organized paragraphs. Aim for a level of detail that would 
allow someone who cannot see the image to form a vivid mental picture of it.
"""
    try:
        # Open the image to validate it
        Image.open(image_path)
        
        # Run Ollama command to generate description
        command = [
            "ollama",
            "run",
            model_name,
            "--",
            PROMPT.replace("FILENAME_PLACEMARKER",os.path.abspath(image_path)),
            "-i",
            image_path
        ]

        result = subprocess.run(command, capture_output=True, text=True, check=True)
        description = result.stdout
        print(f"Model `{model_name}`'s Description of {os.path.abspath(image_path)}: {description}")
        return f"### {model_name}'s take on the image:\n\n{description}"

    except FileNotFoundError:
        return f"Error: Image file not found at {image_path}"
    except subprocess.CalledProcessError as e:
        return f"Error running Ollama: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
def filtered_models():
    return [g for f in get_ollama_models_via_ls() for g in ([f] if is_multimodal(f) else [])]
def good_models():
    return [
        "gemma3:27b",
        "llava:34b",
        "minicpm-v:8b",
        "llama3.2-vision:90b",
        "llava-llama3:8b",
        "llama4:16x17b", # Not the biggest one but this one is at least marginally supported. But if you do have a datacenter in your basement then go ahead and user llama4:128x17b too
        # "llama4:128x17b", # Uncomment this one if you have a server room in your basement and plan on running this on it. :-D
        "qwen2.5vl:72b",
        "granite3.2-vision:2b",
        "moondream:1.8b",
        "mistral-small3.1:24b",
        "bakllava:7b",
        "llava-phi3:3.8b"
    ]
def multiple_describe_image(image_path):
    models = good_models() # Use ALL installed models that self-report themselves to work with images.
    results = []
    for model in models:
        results.append(describe_image(image_path, model))
    return results

def is_multimodal(model_name):
    """Checks if an Ollama model supports multimodal inputs."""
    try:
        url = f"http://localhost:11434/api/show"
        data = {"name": model_name}
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        details = response.json()
        
        # Check if "clip" is present in the model's families
        if 'details' in details and 'families' in details['details']:
            return 'clip' in details['details']['families']
            
    except requests.exceptions.RequestException as e:
        print(f"Error checking model details: {e}")
    return False
def run_image_inference(model_name: str, image_path: str=str(Path(Path(__file__).parent.absolute(),"Scout.jpg")), prompt: str="Describe this image."):
    try:
        with open(image_path, 'rb') as img_file:
            img_data = img_file.read()
            img_base64 = base64.b64encode(img_data).decode('utf-8')

        stream = ollama.chat(
            model=model_name,
            messages=[
                {"role": "user", "content": prompt, "images": [img_base64]}
            ],
            stream=True,
        )

        model_response = ""
        for chunk in stream:
            model_response += chunk["message"]["content"]
            print(chunk["message"]["content"], end="", flush=True)
        
        # Analyze the model's response to confirm image processing
        if "Please provide me with the image!" in model_response or "no image for me to describe" in model_response:
            print("\nOllama model indicated it did not receive or process the image correctly.")
            return False
        else:
            print("\nOllama model appears to have successfully processed the image.")
            return True

    except Exception as e:
        print(f"\nError during Ollama interaction: {e}")
        return False
def check_if_image_model(model):
    PROMPT = """If you can load the image 'FILENAME_PATH' and see what is there just output the word "'"True"'", Otherwise "'"False"'"""
    try:
        command = [
            "ollama",
            "run",
            model,
            "--",
            PROMPT.replace("FILENAME_PATH",os.path.abspath(str(Path(Path(__file__).parent.absolute(),"Scout.jpg"))))
        ]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        
        summary = result.stdout
        print(f"Model `{model}`'s self-reported existance of image reading capability: {summary}")
        return summary.strip().lower() == 'true'        
    except Exception as e:
        return False # If there is error running this model then don't include it.
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
        print(f"Writing image summary: {summary}")
        return summary
    except Exception as e:
        return f"Error summarizing descriptions: {e}"

def stable_diffusion_info(description):
    try:
        command = [
            "ollama",
            "run",
            "gpt-oss:120b",
            "--",
            "Based on the following image description, provide information suitable for recreating it in InvokeAI.  Include the following: Positive Prompt, Negative Prompt, Step Count, CFG Scale, Suggested Image Dimensions, and an idea on the best stable diffusion model to use and the best scheduler:",
            description
        ]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        info = result.stdout
        print(f"Writing image stable diffusion info: {info}")
        return info
    except Exception as e:
        return f"Error generating stable diffusion info: {e}"

def main(image_path):
    pair = OutputFilePair(image_path)
    descriptions = multiple_describe_image(image_path)
    summary = summarize_descriptions(descriptions)
    with open(pair.description_file, "w") as f:
        f.write(summary)

    sd_info = stable_diffusion_info(summary)
    with open(pair.stable_diffusion_file, "w") as f:
        f.write(sd_info)

    print(f"Summary written to {pair.description_file}")
    print(f"Stable Diffusion info written to {pair.stable_diffusion_file}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python image_describer.py <image_path>")
    else:
        main(sys.argv[1])
