Okay, here's a breakdown of InvokeAI settings tailored to recreate imagery inspired by the "Life of Zethana" description, focusing on the iconic image of Zethana as a young adult (around 15-16 years old).  I'll aim for a fantastical, painterly style.

**Core Concept:**  We're aiming for a beautiful, strong, and slightly ethereal image of Zethana – a young woman deeply connected to the ocean, with a hint of power and sadness in her eyes. The environment is crucial – rugged cliffs, tempestuous sea, and a sense of ancient magic.



**1. Positive Prompt:**

```
a beautiful young woman, 16 years old, standing on a black sand beach, dramatic lighting, cinematic, shimmering turquoise armor, intricate gold filigree, ocean wave crest details, flowing gown mimicking ocean currents, ornate headpiece shaped like sea creature horns, long flowing dark hair, strikingly blue eyes, powerful and serene expression, tempestuous sea, rugged obsidian cliffs, ancient ruins in the background,  fantasy art, digital painting, art by Artgerm and Alphonse Mucha, detailed, photorealistic, 8k, volumetric lighting, dynamic composition,  sense of magic, ethereal glow
```

**Breakdown of Prompt Elements:**

*   **Subject & Age:**  Clearly defines the primary subject and her age for consistency.
*   **Armor & Clothing:**  Specific details about her attire – the colors, materials, and ornamentation are vital to the imagery.
*   **Expression:** Crucial. We want a blend of strength and vulnerability.
*   **Environment:**  Sets the scene - black sand beach, cliffs, ruins (suggesting an ancient civilization).
*   **Art Style:**  "Fantasy art, digital painting" provides a foundation.
*   **Artist References:** "Artgerm and Alphonse Mucha" – Both artists have a beautiful style and attention to detail.
*   **Technical Details:** "Detailed, photorealistic, 8k, volumetric lighting, dynamic composition" – Increases the rendering quality and visual impact.




**2. Negative Prompt:**

```
ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, extra limbs, disfigured, deformed, body out of frame, blurry, bad anatomy, watermark, signature, text, close up, cropped, jpeg artifacts, low resolution, overexposed, underexposed,  realistic, photorealistic, mundane, boring, simple background, cartoon, anime, illustration, greyscale, monochrome, bad eyes, mutated hands, plastic skin, smooth skin, doll-like, nsfw, cleavage, overly sexualized
```

**Explanation:**

*   **Common Artifacts:**  "Tiling, poorly drawn hands/feet/face" –  Addresses common issues with AI image generation.
*   **Disfigurement:** "Disfigured, deformed, extra limbs" - Removes problematic results.
*   **Quality Issues:** "Blurry, low resolution, jpeg artifacts" - Ensures a high-quality image.
*   **Style Rejection:**  "Cartoon, anime, illustration" – We want a realistic/painterly style, not stylized.
*   **Unwanted Content:** "nsfw, cleavage, overly sexualized" – Keeps the image appropriate.
*   **Details to Avoid:** "smooth skin, doll-like"  We don't want an unrealistic, plastic look.




**3. Settings:**

*   **Step Count:** 60-80.  More steps generally lead to finer details.
*   **CFG Scale:** 7-10. Higher values enforce the prompt more strongly, but can lead to artifacts.  Experiment within this range.
*   **Image Dimensions:** 768x1024 or 1024x768 (portrait orientation is a good fit for the subject).  Higher resolutions (e.g. 1024x1024) are possible, but require more VRAM.
*   **Sampler:** DPM++ 2M Karras is a good all-around sampler known for quality and speed.  Euler a is another option that works well with detailed prompts.
*   **Model:**  Realistic Vision v5.1 or Deliberate are excellent choices for achieving a realistic and detailed look.  DreamShaper is a good option if you want a slightly more painterly style.
*   **VAE:**  Use a VAE appropriate for your chosen model.  Most models will specify a recommended VAE.  This helps with color accuracy and overall image quality.



**Tips for Success:**

*   **Seed:**  Use a fixed seed to reproduce results and iterate on variations.
*   **Prompt Weighting:** Experiment with weighting different parts of the prompt using parentheses (e.g., `(shimmering turquoise armor:1.2)` to emphasize the armor).
*   **Image Upscaling:** Once you have a good base image, use an upscaler (like Real-ESRGAN) to increase the resolution further without significant quality loss.
*   **Inpainting:**  If specific parts of the image need refinement (e.g., hands or face), use inpainting to correct them.
*   **Iterate:**  AI image generation is an iterative process. Don't be afraid to experiment with different settings and prompts until you achieve the desired result.




I've tried to be as comprehensive as possible.  Let me know if you'd like any further clarification or modifications to these settings!

