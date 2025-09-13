## InvokeAI Prompt Breakdown: Dark Spire Confrontation

Here's a breakdown designed to recreate the scene in InvokeAI, covering all requested elements. This is a *long* prompt, and will require a good model/scheduler pairing and likely some initial experimentation.  I'm aiming for a high-quality, detailed image.

**Key Considerations:**

*   **Model:**  Deliberate v2, Realistic Vision v5.1, or Protogen x5.8 are excellent choices for detailed scenes and character rendering.  Avoid simpler anime-style models.
*   **Scheduler:** DPM++ 2M Karras or DPM++ SDE Karras are generally good for detail and coherence.
*   **CFG Scale:** Start at 7-9, adjust as needed.  Higher values can introduce artifacts.
*   **Step Count:**  At least 40-60 steps are recommended for this level of detail.  Higher step counts (80+) may yield further refinement, but can be slow.
*   **Resolution:**  768x1024 or 1024x1536 is a good starting point for vertical compositions.  You can upscale later.

---

### **Positive Prompt:**

```
(masterpiece, best quality, ultra detailed, 8k), cinematic lighting, dramatic composition, imposing architecture,  cylindrical chamber constructed from polished obsidian, swirling iridescent blue and green patterns in obsidian, diffuse otherworldly glow, phosphorescent lavender energy lines on obsidian floor, complex energy vortex,  Favored One, the Witch Queen, towering figure, (indigo skin with shifting constellation patterns), flowing gown of woven shadows and starlight, ornate crown of dark metal and gems, piercing silver eyes, striking angular face,  Starfighter, advanced spacesuit, matte grey with blue and orange highlights, aerodynamic design, dynamic pose, off-balance, reaching out, (hands almost touching:1.2), flashback sequence, fragmented memories, swirling colors, past lives, mountain vista, warm golden hue,  intimate connection,  (powerful energy:0.8), detailed textures, volumetric lighting, depth of field, dynamic angle,  highly detailed background, complex details, intricate designs,  
```

**Prompt Breakdown Notes:**

*   **(keyword: weight)** is used to emphasize important elements.  Experiment with weights to adjust the emphasis on specific aspects.
*   `masterpiece, best quality, ultra detailed, 8k` are standard quality boosters.
*   Detailed descriptions of materials, colors, and textures are key.
*   I've specified poses and actions to guide the composition.
*   The `(hands almost touching:1.2)` is critical to get the right moment of contact.




### **Negative Prompt:**

```
(worst quality, low quality:1.4), (monochrome, greyscale:1.2), blurry, text, watermark, signature, logo, ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, extra limbs, disfigured, deformed, body out of frame, bad anatomy, blurred, grainy, noisy, artifacts, oversaturated, underexposed,  simple background, flat lighting, cartoon, anime, illustration, 3d render, plastic texture, doll-like,  duplicate, cloned, repetitive patterns, oversmooth,  long neck, mutated hands and fingers,  bad proportions,  lowres, jpeg artifacts, bad art, beginner, amateur, distorted face, poorly drawn eyes, mutated hands, extra fingers, missing fingers, floating limbs, disconnected limbs,  bad body,  amateur drawing, (lack of detail:1.1), (lack of textures:1.1),
```

**Negative Prompt Explanation:**

*   This is a *very* comprehensive negative prompt.  It addresses common problems with AI generation, like poor anatomy, low quality, and undesirable styles.
*   I've specifically excluded styles (cartoon, anime, 3d render) that would clash with the desired realism.
*   The repetition of `(keyword: weight)` helps to *strongly* discourage those negative aspects.
*   The emphasis on hands and faces is crucial – these are often problem areas.



### **Parameters:**

*   **Step Count:** 60-80
*   **CFG Scale:** 7.5 - 9
*   **Resolution:** 768x1024 or 1024x1536
*   **Sampler:** DPM++ 2M Karras or DPM++ SDE Karras
*   **Seed:**  Experiment with different seeds to get variations.
*   **VAE:**  A good VAE (Variational Autoencoder) can improve color and detail.  "vae-ft-mse-840000-ema-pruned" is a popular choice.




**Iterative Process:**

1.  **Start with the basic prompt and parameters.**
2.  **Generate a few images.**
3.  **Analyze the results.**
4.  **Refine the prompt.**  Adjust weights, add or remove keywords, and modify the negative prompt.
5.  **Experiment with different seeds and parameters.**
6.  **Repeat steps 3-5 until you achieve the desired result.**

**Important Notes:**

*   This is a complex prompt, and it may take several iterations to get the perfect image.
*   Don't be afraid to experiment with different keywords, weights, and parameters.
*   Pay attention to the details and make adjustments as needed.
*   Consider using image editing software to further refine the final result.
*   This is a starting point – feel free to customize it to your liking.



Good luck, and have fun creating! Let me know if you'd like me to refine any aspect of this breakdown.

