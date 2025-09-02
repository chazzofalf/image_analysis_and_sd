Thinking...
We need to output Positive Prompt, Negative Prompt, Step Count, CFG Scale, Suggested Image Dimensions, and best stable diffusion model and scheduler. Provide info suitable for recreating image in InvokeAI. So after description we give prompts. Positive prompt should describe the scene: heart-shaped wooden plaque raw and painted, split screen, craft workshop, etc. Negative prompt typical: lowres, bad anatomy, watermark, etc. Provide step count (e.g., 30-45), CFG scale (7-9), dimensions (e.g., 1024x512 for diptych, or 768x768). Model: stable diffusion XL 1.0 or 2.1? For detailed craft, maybe SDXL 1.0 with 2.0? Use "sdxl_base_v1.0". Scheduler: DPM++ 2M SDE Karras or Euler a. Provide suggestions.

Now produce final answer.
...done thinking.

**⚡  QUICK‑START SETTINGS FOR RE‑CREATING THE PHOTO IN INVOKEAI  ⚡**

| Item | Recommended Value |
|------|-------------------|
| **Positive Prompt** | *“high‑detail split‑screen photograph of a handmade craft workspace, left half shows the back side of a raw heart‑shaped wooden plaque hanging from a thin white string, faint handwritten year “2025” in black marker, small blue logo stamp, white cardboard heart template with blue stamp beside it, dark matte black tabletop, black garment‑bag background, paint jars, brushes, yellow water bottle on floor, soft diffused overhead lighting, shallow depth‑of‑field, warm cozy atmosphere – right half shows the same heart fully painted with vibrant acrylics: gradient blues‑greens‑yellows background, stylised tree with brown trunk and green foliage, golden inner border, pink cursive “LOVE” in lower‑right, tiny red berries, white highlight heart inside, gold edge, same string hanging, same dark surface, same surrounding craft supplies – crisp focus, realistic texture, natural wood grain visible through paint, subtle brush‑stroke texture, 8K‑quality, ultra‑realistic, photo‑realistic, studio lighting, slight vignette.”* |
| **Negative Prompt** | *“low‑resolution, blurry, pixelated, jpeg artifacts, watermark, text overlay, signature, lens flare, over‑exposed highlights, under‑exposed shadows, cartoon, anime, illustration, 3D render, unrealistic colors, oversaturation, grainy film, motion blur, duplicate, out‑of‑focus background, plastic‑looking wood, glossy plastic finish, unrealistic metal, wrong perspective, missing string, missing year, missing brush strokes, oversimplified, flat shading.”* |
| **Steps** | **35 – 45** (35 is a good balance; bump to 45 if you want extra fine‑detail on the wood grain and brush texture) |
| **CFG Scale** | **7.5 – 8.5** (8 is a solid middle‑ground for faithful composition while still allowing the model’s creativity for subtle texture) |
| **Image Size** | **1024 × 512 px** (wide “diptych” format) – if you prefer a square canvas for later cropping, use **768 × 768 px** and then split in post‑processing. |
| **Best Stable Diffusion Model** | **Stable Diffusion XL 1.0 (sdxl_base_1.0)** – it handles complex textures (wood grain, acrylic gloss, fabric bags) and realistic lighting very well. If you have the newer **SDXL 1.0‑Turbo** you can also try it for faster iterations. |
| **Recommended Scheduler** | **DPM++ 2M SDE Karras** (excellent for preserving fine detail and smooth gradients) – **Euler‑a** works fine as an alternative if you prefer a slightly sharper edge. |
| **Seed (optional)** | Any integer you like; set a fixed seed (e.g., **123456789**) if you need reproducibility. |
| **Batch size** | 1 (single image, then you can manually split the canvas into left/right panels if you want perfect symmetry). |
| **Additional Tips** | • Use **high‑quality LoRA** or **style‑adapter** for “craft‑workshop” or “photographic‑studio” if you have one – it will reinforce the realistic lighting and material feel. <br>• After generation, **crop** the left‑half and right‑half and optionally apply a tiny **Gaussian blur** (radius 0.3) to the background bags to increase depth separation. <br>• If the year number is ambiguous, you can **in‑paint** a clean “2025” after the first pass using the In‑paint tool. |

--- 

### How to Apply These Settings in InvokeAI (Step‑by‑Step)

1. **Open the UI** → go to the *Text‑2‑Image* tab.  
2. **Model**: select `sdxl_base_1.0` (or `sdxl_base_1.0-turbo`).  
3. **Prompt**: paste the **Positive Prompt** above.  
4. **Negative Prompt**: paste the **Negative Prompt**.  
5. **Steps**: set to `35` (or `45` for extra detail).  
6. **CFG Scale**: set to `8`.  
7. **Sampler**: choose **DPM++ 2M SDE Karras** (or Euler‑a).  
8. **Size**: type `1024` × `512`.  
9. **Seed**: optional – enter `123456789` for reproducibility.  
10. **Generate** → wait for the image.  
11. **Post‑Processing (optional)**:  
    - Use the *Crop* tool to separate the left (raw) and right (finished) halves.  
    - If the year looks fuzzy, run a quick **in‑paint** pass with a clean “2025” mask.  
    - Add a subtle vignette if you want to mimic the soft studio light.  

You should now have a faithful, photorealistic recreation of the original split‑screen craft‑workshop photograph, ready for further editing or sharing. Happy generating! 🚀

