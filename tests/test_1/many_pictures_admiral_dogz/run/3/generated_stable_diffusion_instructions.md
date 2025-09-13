## InvokeAI Prompt Breakdown for Composite Image

Here's a breakdown designed to recreate the described image in InvokeAI, aiming for high fidelity.

**1. Positive Prompt:**

```
a breathtaking panoramic view from inside a futuristic circular observation deck, a lone astronaut stands with back to viewer overlooking a vibrant cloud-covered planet and the expanse of space, detailed control panels with glowing blue and white indicators, dark matte-black interior, highly detailed, photorealistic, cinematic lighting,  intricate details, vastness, isolation, control, a sense of wonder,  deep blues,  saturated colors, planetary vista, ethereal glow, subtle reflections, dynamic cloud formations,  perfect composition, 8k resolution, dramatic perspective, volumetric lighting,  art by Greg Rutkowski and Beeple, trending on ArtStation
```

**2. Negative Prompt:**

This is *crucial* for controlling the output and avoiding unwanted elements. Be exhaustive!

```
blurry, distortion, low resolution, low quality, artifacts, noise, grain, oversaturated, cartoon, anime, painting, illustration, sketch, drawing, bad anatomy, deformed limbs, extra limbs, missing limbs, ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, mutation, mutated, watermark, signature, text, logo, jpeg artifacts,  oversimplified, flat colors,  bright daylight, harsh lighting, reflections, lens flare, people, multiple astronauts, cluttered, busy, unrealistic, CGI, 3D render,  poorly lit, visible seams, plastic texture,  grainy,  disfigured, asymmetrical,  bad proportions,  amateurish, out of focus,  duplicate, cropped, duplicate objects
```

**3. Step Count:**

*   **50-75 steps:**  This provides a good balance between detail and rendering time. Start with 50 and increase if needed.

**4. CFG Scale:**

*   **7-10:**  This controls how closely the image adheres to the prompt. A higher value means more adherence, but can lead to less creative results. Start at 7 and experiment.

**5. Suggested Image Dimensions:**

*   **1024x768 or 1280x960:** This provides a good cinematic aspect ratio for the panoramic view. You can go larger if your hardware allows, but this is a good starting point.  Consider a wider aspect ratio like 16:9.

**6. Stable Diffusion Model & Scheduler:**

*   **Model:** **Realistic Vision v5.1** or **Deliberate v2**. These models excel at photorealism and detail.  Avoid anything too stylized.
*   **Scheduler:** **DPM++ 2M Karras**.  This scheduler is generally considered excellent for realistic images, offering a good balance of speed and quality.  Experiment with DPM++ SDE Karras for slightly different results.


**Additional Tips for InvokeAI:**

*   **Seed:**  Use a fixed seed initially to allow for consistent iterations and parameter tuning. Once you get a good result, experiment with random seeds to generate variations.
*   **Inpainting:** Use inpainting to refine specific areas of the image, such as the astronaut's suit or the planet's details.
*   **Regional Prompting (If available in your InvokeAI version):** This is *extremely* useful.  You could define regions for the astronaut, the control panels, and the planet to apply specific prompts to each.
*   **Experiment!**  AI image generation is iterative. Don't be afraid to try different prompts, settings, and models to achieve the desired result.
*   **Prompt Weighting (if supported):** Use `()` to emphasize parts of the prompt and `[]` to de-emphasize.  For example: `(vibrant cloud-covered planet:1.2) [harsh lighting:0.5]`



This detailed breakdown should provide a solid foundation for recreating the described image in InvokeAI.  Remember to be patient, experiment, and refine your prompts and settings to achieve the best possible results.  Good luck!

