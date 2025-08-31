import subprocess
from PIL import Image
from ollama_ls_parser import get_ollama_models_via_ls
import os
from output_file_pair import OutputFilePair
def describe_image(image_path, model_name):
    PROMPT="""
You are an AI model with vision capabilities.  
Please open and examine the image located at **FILENAME_PLACEMARKER** and give a **comprehensive, exhaustive, and human‑readable description** 
of everything you see. If you cannot load or see the image. Stop Right There.

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
        
        return f"### {model_name}'s take on the image:\n\n{description}"

    except FileNotFoundError:
        return f"Error: Image file not found at {image_path}"
    except subprocess.CalledProcessError as e:
        return f"Error running Ollama: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def multiple_describe_image(image_path):
    models = get_ollama_models_via_ls() # Use ALL installed models (Some may not work. But THAT is what will make it more interesting!)!
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
