Okay, here's a breakdown of settings for InvokeAI to attempt to recreate the essence of Zethana and the world described, aiming for a visually compelling and atmospheric result.  This is a complex scene with a lot of nuanced detail, so expect to refine these settings through experimentation.

**Core Aesthetic Goal:**  A blend of fantasy, realism, and environmental beauty.  Think "epic fantasy illustration" but with believable lighting and texture.  We want a sense of power, connection to the ocean, and a hint of ancient mystery.



**1. Positive Prompt:**

```
a beautiful, strong woman, Zethana, the Tide Weaver, standing on a black sand beach, overlooking a turquoise ocean, shimmering turquoise armor with intricate coral filigree, long flowing gown mimicking ocean currents, ornate headpiece shaped like sea creature horns, long flowing dark hair with seafoam highlights, determined expression, powerful stance, dramatic lighting, bioluminescent details, ancient ruins in the background, crashing waves, stormy sky with shafts of sunlight, hyperdetailed, realistic textures, fantasy illustration, art by Artgerm and Alphonse Mucha, cinematic composition,  high resolution, 8k,  detailed face,  intricate detail
```

**Key Elements in the Prompt:**

*   **Character Focus:**  Clearly defines Zethana, emphasizing key details of her appearance.
*   **Setting:** Specifically calls for the black sand beach, turquoise ocean, and ancient ruins.
*   **Art Style References:**  "Artgerm and Alphonse Mucha" aims for a blend of modern digital painting polish and classical art nouveau grace.
*   **Technical Details:** "8k, high resolution, detailed face, intricate detail" tells the AI to prioritize quality.
*   **Atmospheric elements** stormy sky, crashing waves, bioluminescent details




**2. Negative Prompt:** (This is *critical* for quality)

```
cartoon, anime, 3d render, CGI, illustration, painting, drawing, sketch, low quality, blurry, pixelated, jpeg artifacts,  deformed face, bad anatomy, extra limbs, missing limbs, poorly drawn hands, poorly drawn feet, mutated, disfigured, ugly, tiling, out of frame, watermark, signature, text, logo, bad proportions, plastic skin, smooth skin, flat lighting, oversaturated, monochrome, greyscale, simple background,  fantasy, unreal engine, children,  excessive makeup,  duplicate features,  unnatural colors,  close-up, cropped, 
```

**Explanation of Negative Prompt Choices:**

*   **Style Rejection:**  Specifically excludes styles we *don't* want.  (e.g., cartoon, anime).
*   **Quality Control:**  Eliminates common AI image generation flaws (blurry, low quality, artifacts).
*   **Anatomy & Detail:** Prevents common anatomical errors (extra/missing limbs, bad hands/feet).
*   **Aesthetic Control:**  Prevents unwanted visual elements (watermarks, text).



**3. Step Count:** 

*   **50-75 steps:** This provides a good balance between detail and generation time.  Higher step counts (up to 100) *may* yield slightly better results, but the improvement will be diminishing.



**4. CFG Scale:**

*   **7-9:** This range encourages the AI to adhere to the prompt while still allowing for some creative interpretation.  Experiment within this range to find the sweet spot for your desired level of prompt adherence.



**5. Suggested Image Dimensions:**

*   **768x1024 or 1024x1536:** These vertical aspect ratios are well-suited for a character-focused image with a dramatic landscape.  You can experiment with wider aspect ratios if you prefer a more cinematic composition.




**6. Stable Diffusion Model:**

*   **Deliberate V2:**  This model is known for its realistic and detailed outputs, making it a good choice for this fantasy scene.  It handles faces and armor particularly well.
*   **Realistic Vision V5.1:** Another strong contender known for its realism and ability to render intricate details.

**7. Scheduler:**

*   **Euler a:** This scheduler often produces more artistic and dynamic results, which would suit the fantasy aesthetic.
*   **DPM++ 2M Karras:**  A good all-around scheduler that balances speed and quality.



**Additional Tips & Experimentation:**

*   **Seed:** Use a specific seed to reproduce results and iterate on variations.
*   **Vary Prompt Weighting:** Experiment with using parentheses to emphasize certain keywords in the prompt (e.g., `(Zethana:1.2)` to give her more prominence).
*   **Regional Prompting/Inpainting:**  Use regional prompting or inpainting features to refine specific areas of the image (e.g., to add more detail to the armor or the ocean).
*   **Image Upscaling:** After generating a good base image, use an image upscaling tool (e.g., Real-ESRGAN) to increase the resolution and sharpness.

**Important Note:** AI image generation is an iterative process.  You'll need to experiment with these settings and refine them based on your own preferences and the results you're getting.  Don't be afraid to try different combinations of models, schedulers, and settings to achieve the look you're aiming for.  Good luck!

