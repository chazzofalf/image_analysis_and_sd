# Image Description Tool

This tool leverages Ollama models to describe images and generate stable diffusion parameters for recreation in InvokeAI.

## Functionality

- **Image Description:** Uses multiple Ollama models (gemma3:27b, llava:latest, llama4:scout, mistral-small3.2:24b, Moondream:latest, llama3.2-vision:latest) to generate descriptions of an input image.
- **Summarization:** Combines the individual descriptions into a single, comprehensive summary using `gpt-oss:120b`.
- **Stable Diffusion Parameter Generation:** Extracts parameters (positive prompt, negative prompt, step count, CFG scale, image dimensions, and suggested model/scheduler) suitable for recreating the image in InvokeAI, using `gpt-oss:120b`.

## Usage

1.  Ensure you have Ollama installed and configured.
2.  Run the `image_describer2.py` script with the following arguments:

    ```bash
    python image_describer2.py <image_path> <output_file>
    ```

    *   `<image_path>`: Path to the input image.
    *   `<output_file>`: Path to the output file (summary will be written to this file, and stable diffusion parameters will be written to `<output_file>.sd.txt`).

## Dependencies

-   Ollama
-   Python 3

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
