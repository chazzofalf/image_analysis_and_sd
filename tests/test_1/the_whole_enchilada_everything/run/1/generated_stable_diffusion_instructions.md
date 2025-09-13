Okay, this is a fantastic brief! We're aiming for a powerful, epic fantasy image evoking a strong female leader connected to the sea and cosmos. Here's a breakdown of settings for InvokeAI, geared towards achieving a high-fidelity result.

**Core Aesthetic:**  Epic Fantasy, Cosmic/Oceanic blend, Strong Female Protagonist, Detailed Armor, a hint of Introspection.

---

**1. Positive Prompt:**

```
masterpiece, best quality, extremely detailed, 1girl, Zethana, strong female leader, standing on rocky coastline, windswept hair, turquoise and gold filigree armor, ocean wave crests etched into armor, flowing silk garments, cosmic background, swirling nebulae, distant galaxies, vast ocean, dramatic lighting, volumetric light, highly detailed face, serene expression, thoughtful gaze, long hair, cinematic composition, epic scale, mystical aura, depth of field,  intricate details,  fantasy art, inspired by Greg Rutkowski, Alphonse Mucha, Artgerm, WLOP,  detailed environment, islands in the distance,  powerful, regal, determined, introspective,  a hint of melancholy, [dog looking pensively at her feet:0.5],  soft glow around her, ethereal, magical
```

**Explanation:**

*   **Quality & Detail:**  "masterpiece, best quality, extremely detailed" are essential starting points.
*   **Character Focus:**  Clearly defines the subject ("1girl, Zethana…") and her core attributes.
*   **Armor & Clothing:**  Specifies the armor design crucial to the description.
*   **Environment:** Defines the environment as rocky coastline with islands in the distance and the crucial cosmic background.
*   **Lighting & Composition:**  Requests dramatic lighting, cinematic composition, and depth of field.
*   **Artists:**  Inclusion of known fantasy artists to influence style.
*   **Emphasis/Weighting:** `[dog looking pensively at her feet:0.5]`  uses InvokeAI syntax to add the dog as a subtle element, not overpowering the main subject.  The weighting of `:0.5` reduces its influence.

---

**2. Negative Prompt:**

```
low quality, worst quality, bad anatomy, deformed, disfigured, blurry, cropped, jpeg artifacts, signature, watermark, text, errors, extra limbs, mutated hands, poorly drawn hands, poorly drawn face, ugly, tiling, duplicate, morbid, mutilated, out of frame, mutation, bad proportions, gross proportions, cloned face, poorly rendered, plastic, fake, CGI, cartoon, anime, illustration, oversaturated, unnatural colors, simple background, flat lighting, harsh shadows, low contrast, boring, generic,  distant view, full shot, too much detail,  lack of atmosphere,  unrealistic, dull colors, lowres, duplicate faces, multiple people
```

**Explanation:**

*   **Quality & Anatomy:**  Addresses common AI art issues.
*   **Artifacts & Errors:**  Removes unwanted visual noise and errors.
*   **Style & Rendering:**  Excludes undesirable styles (cartoon, anime) and rendering qualities (plastic, fake).
*   **Compositional Issues:** Prevents overly distant shots and unwanted elements.
*   **Redundancy:** Prevents duplicate elements and faces.

---

**3. Settings:**

*   **Step Count:** 60-80 (Higher step counts yield more detail but take longer)
*   **CFG Scale:** 7-9 (Higher values force the AI to adhere more closely to the prompt, but can introduce artifacts. Experiment!)
*   **Image Dimensions:** 768x1024 or 1024x768 (portrait orientation suits the character)  Consider larger dimensions (e.g., 1536x2048) if you have the resources.
*   **Model:** Deliberate v2 is a great all-rounder for fantasy art.  Alternatively, consider:
    *   **Realistic Vision v5.1**: For hyperrealistic results.
    *   **DreamShaper XL**: Good balance of realism and artistic style.
*   **Scheduler:** DPM++ 2M Karras is generally considered excellent for detail and coherence. Alternatively:
    *   Euler a:  Good for speed and artistic style.
    *   DPM++ SDE Karras:  For stability and quality.

---

**Additional Tips & Considerations:**

*   **Seed:** Use a fixed seed to iterate and refine the image while maintaining consistency.
*   **Refiner:** If using a refiner model (many models have companion refiner models), apply it after the initial generation to enhance detail and sharpness.
*   **Inpainting:** Use inpainting to fix minor issues or refine specific areas of the image.
*   **Iterate!** AI art is about experimentation. Don't be afraid to adjust the prompt and settings to achieve the desired result.  Pay attention to what works and what doesn't.



This should give you a solid starting point for creating a compelling image of Zethana, drawing upon the richness of the provided narrative.  Good luck!  Let me know if you have any other questions.

