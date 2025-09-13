## InvokeAI Prompt Breakdown for Composite Image

Here's a breakdown to recreate the described image in InvokeAI, aimed for high fidelity and a realistic look.

**1. Positive Prompt:**

```
a small dark-furred dog, seated, alert expression, slightly tilted head, wiry coat, subtle graying around muzzle, pale beige collar with bright green pendant, rustic wooden structures in background, archway of weathered wood, staggered wooden fence, rough-hewn wood, packed earth foreground transitioning to vibrant green lawn, diffused lighting, low angle light, detailed texture, high resolution, natural scene, serene, tranquil, well-cared-for environment, photographic, 8k, realistic
```

**2. Negative Prompt (Detailed - Crucial for Fidelity):**

```
blurry, low resolution, cartoon, illustration, painting, drawing, anime, sketch, unrealistic, oversaturated, deformed, disfigured, poorly drawn hands, bad anatomy, extra limbs, mutated, watermark, signature, text, logo, jpeg artifacts, compression artifacts, bright harsh light, direct sunlight, flat lighting, plastic texture, smooth skin, plastic fur, shiny, metallic, glowing, bokeh, depth of field,  abstract, fantasy, sci-fi,  artificial, fake, CGI, 3D render, digital art, out of focus, vignette
```

**3. Step Count:**

*   **50-75 steps:**  This range provides a good balance between detail and generation time.  Higher steps can refine details further, but diminishing returns apply.  Start with 50 and increase if needed.

**4. CFG Scale:**

*   **7-10:** A moderate CFG scale will encourage adherence to the prompt without overly constraining the creative freedom of the AI. Start with 7.5.  Higher values will stick more rigidly to the prompt, but can lead to less natural results.

**5. Suggested Image Dimensions:**

*   **768x512 or 832x608:** These are good starting points for portrait-oriented images that still provide detail. You could experiment with wider ratios as well (e.g. 1024x683) but this might require some adjustment to the prompt to ensure the key elements are framed correctly.

**6. Model & Scheduler:**

*   **Best Model:** **Realistic Vision V5.1** is an excellent choice for photorealistic results. **Deliberate V2** is another very solid option.
*   **Best Scheduler:** **DPM++ 2M Karras** or **DPM++ SDE Karras** both generally provide excellent detail and quality with good stability.  Experiment with both to see which works best for this particular prompt.

**Important Notes & Tips:**

*   **Seed:** Use a fixed seed for consistent results during experimentation.  Once you find a result you like, you can then randomize the seed to explore variations.
*   **Prompt Weighting:** If certain elements are more important than others, you can use prompt weighting (e.g., `(dog:1.2)` to emphasize the dog).
*   **Regional Prompting (If Using InvokeAI's Inpainting):**  If you need to refine specific areas, consider using InvokeAI's inpainting features with a targeted prompt.
*   **Iterative Refinement:**  This is key. Generate an image, analyze the results, and then adjust the prompts, steps, CFG scale, or seed to improve the image.  Pay attention to areas that are consistently problematic.
*   **Experiment with Variations:**  Don't be afraid to try different combinations of prompts, settings, and models.



This detailed breakdown should provide a solid foundation for recreating the described image in InvokeAI with a high level of detail and realism.  Good luck!

