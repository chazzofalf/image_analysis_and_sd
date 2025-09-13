## InvokeAI Recreation Parameters

Here's a breakdown of parameters for recreating the described image in InvokeAI, geared towards achieving a high level of fidelity and matching the described aesthetic:

**1. Positive Prompt:**

```
a small dark-furred terrier dog seated on light concrete, rustic wooden fence background, green vegetation visible, direct gaze, soft lighting, detailed fur texture, wiry coat, slight mane, natural wood grain, weathered wood, shallow depth of field, peaceful scene, domestic setting, high detail, 8k, photorealistic
```

**2. Negative Prompt (Detailed - very important for quality):**

```
cartoon, illustration, painting, drawing, sketch, anime, 3d render, digital art, CGI, unrealistic, blurry, low resolution, bad anatomy, deformed, disfigured, cropped, watermark, signature, text, logo, jpeg artifacts, oversaturated, overexposed, underexposed, noise, grain, bad proportions, extra limbs, missing limbs, mutated hands, poorly drawn hands, unnatural colors, plastic texture, fake, artificial, smooth skin, perfect skin, glossy, simple background, flat lighting, bright colors, abstract, fantasy, magical, long neck, long body, close-up, wide angle, fish eye,  duplicate, cloned, multiple dogs
```

**3. Step Count:**

* **40-60 steps:**  This range offers a good balance between detail and rendering time.  Higher steps *can* increase detail, but diminishing returns are common.

**4. CFG Scale:**

* **7-9:** This range typically provides a good balance between adhering to the prompt and allowing for some creative freedom.  Lower values (closer to 7) can feel more natural, while higher values (closer to 9) will force the image to adhere more strictly to the prompt.

**5. Suggested Image Dimensions:**

* **768x1024 or 512x768:**  Vertical orientation to match the described composition.  These dimensions offer a good compromise between detail and processing time.  You can experiment with higher resolutions if your hardware allows.

**6. Stable Diffusion Model Recommendation:**

* **Realistic Vision V6.0:** This model is excellent for photorealistic images, especially with animals and outdoor scenes. It's known for its natural lighting and detailed textures.
* **Deliberate v2:** Another strong contender for photorealism, particularly adept at rendering fur and wood textures.
* **DreamShaper 7.0:**  Good overall realism and creative freedom.

**7. Scheduler Recommendation:**

* **DPM++ 2M Karras:**  This scheduler generally produces high-quality, detailed images with good color accuracy. It's a good all-around choice.
* **Euler a:** Can provide a more artistic, painterly look if you want a slightly softer aesthetic.
* **UniPC:** This scheduler is known for its speed and generally produces good results.

**Additional Tips & Considerations:**

* **Seed:**  Use a seed to reproduce results and iterate on variations.
* **Emphasis:** Use parentheses `()` to emphasize certain keywords in the positive prompt (e.g., `(detailed fur texture)`) and square brackets `[]` to de-emphasize.
* **Inpainting/Outpainting:**  Consider using inpainting/outpainting tools to refine specific areas of the image after the initial generation.  For example, you could inpaint to sharpen the dog's eyes or add more detail to the wooden fence.
* **Variations:** Experiment with slightly altering the prompts and parameters to explore different variations of the image.  Don't be afraid to try different models and schedulers to find what works best for you.
* **Img2Img:** If you have a starting image that's close to the desired result, use img2img to refine it and add more detail.



By carefully adjusting these parameters and experimenting with different options, you should be able to create a compelling and faithful recreation of the described image in InvokeAI.  The detailed negative prompt is *crucial* for preventing unwanted artifacts and ensuring a high level of quality. Remember to monitor your VRAM usage and adjust image dimensions accordingly.

