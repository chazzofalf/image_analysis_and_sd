Okay, here's a breakdown of settings for InvokeAI, aiming to recreate an image that *feels* like the narrative described. This is going to be geared toward a dramatic, painterly, and fantastical style, with a focus on atmospheric detail and strong character portrayal.  Since the narrative mentions colors aligning with a nebula, we'll lean into that visually.

**Understanding the Core Aesthetic:**

The narrative leans toward a high-fantasy aesthetic, but *not* overly gritty or grimdark. It's majestic, slightly mystical, and emphasizes the connection to nature (specifically the ocean). We want something that feels *epic* but also *compassionate*.



**1. Positive Prompt:**

This is the core of what we want to see.  I'm breaking it down into sections for clarity, layering details.  Weighting (using `( )` and `[ ]`) is used to emphasize specific aspects.

```
a breathtaking portrait of Zethana, a young woman with flowing dark hair and piercing turquoise eyes, wearing ornate turquoise and silver armor reminiscent of ocean waves and coral, [highly detailed intricate armor:1.3], standing on a windswept cliff overlooking a vast turbulent ocean, dramatic lighting, nebula background with swirling blues, purples, and greens, [glowing bioluminescent details:0.8] on armor and surrounding environment,  a sense of power and compassion, [flowing robes:0.7] beneath armor,  detailed facial features, [realistic skin texture:0.9], wind-swept hair, [intricate jewelry:0.7] crafted from shells and pearls, epic fantasy, painterly, art by Artgerm and Alphonse Mucha,  [masterpiece:1.2], best quality, 8k, photorealistic
```

* **Key Elements:** Zethana's description, armor details, environment, lighting, artistic influences.
* **Weighting:** Increases the emphasis on certain features.
* **Artistic Style:**  Artgerm (known for detailed portraits) and Alphonse Mucha (known for flowing lines, Art Nouveau) help define the aesthetic.

**2. Negative Prompt:**

This is *crucial* for controlling the outcome. We want to avoid common pitfalls and unwanted elements.  Be *exhaustive* here.

```
lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, artist name, monochrome, grayscale, oversaturated, unnatural colors, cartoon, anime, 3d render, plastic, doll-like, ugly, tiling, deformed, disfigured, mutation, mutated, extra limbs, floating limbs, poorly drawn hands, poorly drawn feet, bad art, beginner, amateur, poorly drawn face, duplicate, cloned, simple background, flat lighting, harsh shadows, unrealistic, unnatural, overly bright, overly dark, noisy, grain, sketch, draft, illustration, painting, (worst face:1.2), (bad eyes:1.2), (disproportionate body:1.2), (bad anatomy:1.2)
```

* **Common Issues:** Addresses common image generation problems (bad anatomy, hands, etc.).
* **Unwanted Styles:** Excludes styles that don’t fit the desired aesthetic (cartoon, 3D render).
* **Quality Control:**  Emphasis on avoiding low-quality results.




**3. Step Count:**

* **50-75 steps:**  This provides a good balance between detail and generation time. More steps *can* improve quality, but the gains diminish after a certain point.  Experiment!

**4. CFG Scale:**

* **7-10:** This controls how strongly the image adheres to the prompt.  Lower values give more creative freedom, higher values force the image to match the prompt more closely.  I suggest starting at 7.5 and adjusting.

**5. Suggested Image Dimensions:**

* **768x1024 or 1024x768:** These dimensions provide a good aspect ratio for a character portrait.  Higher resolutions are possible but require more VRAM.

**6. Stable Diffusion Model:**

* **Deliberate:**  Excellent for realistic and painterly images, with strong character portrayal.
* **Realistic Vision V5.1:** Another strong choice for realism and detail.
* **Dreamshaper:** Good for fantasy and artistic images.

**7. Scheduler:**

* **DPM++ 2M Karras:**  Considered one of the best schedulers for detail and quality.  Offers a good balance between speed and performance.
* **Euler a:** Can produce more creative results, but may require more fine-tuning.

**Additional Tips:**

* **Seed:** Use a fixed seed to reproduce results and iterate on them.
* **Variations:**  Experiment with different seeds and minor prompt changes to generate variations of the image.
* **Img2Img:** If you have a base image you like, use img2img to refine it and add details.
* **Inpainting:** Use inpainting to fix specific areas of the image.




**Important Note:** This is a starting point. Image generation is an iterative process. You'll need to experiment with different settings and prompts to achieve the exact result you're looking for. Be patient and have fun!  The key is to refine the prompt and negative prompt based on the images you're getting.  Don't be afraid to add more specific details, and pay attention to what works and what doesn't.

