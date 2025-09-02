Thinking...
We need to provide information suitable for recreating it in InvokeAI: Positive Prompt, Negative Prompt, Step Count, CFG Scale, Suggested Image Dimensions, best stable diffusion model and best scheduler. Also include the exhaustive description we just made? The user asked: "Based on the following image description, provide information suitable for recreating it in InvokeAI. Include the following: Positive Prompt, Negative Prompt, Step Count, CFG Scale, Suggested Image Dimensions, and an idea on the best stable diffusion model to use and the best scheduler: Thinking... We need to combine descriptions into a single exhaustive description. The previous assistant gave the exhaustive description. Now they ask to provide prompts etc. So output should include the exhaustive description plus the InvokeAI settings. Provide positive prompt detailed, negative prompt to exclude unwanted elements, steps maybe 30-45, CFG 7-9, dimensions maybe 1024x1024 or 768x1024, model suggestion: stable-diffusion-xl-base-1.0 or sd-v2.1, maybe use "Euler a" or "DPM++ 2M Karras". Provide rationale. Let's craft final answer.
...done thinking.

**✅  What you need to type into InvokeAI (or any Stable‑Diffusion front‑end) to reproduce the picture**  

---

## 1️⃣  Positive Prompt (everything you *do* want in the image)  

```
glass Coca‑Cola bottle, classic contour glass design, 355 ml, red and white retro Coca‑Cola label with white script and “Cont. Net 355ml”, glossy label, clear slightly green‑tinged glass, smooth polished surface, slender neck, uncapped, partially filled with dark caramel cola (optional: show liquid with bubbles and subtle surface ripples), suspended droplets of water frozen in mid‑air around the bottle, high‑speed splash effect, dramatic cool‑toned directional lighting from upper‑left, soft rim highlight on glass, subtle shadows on opposite side, dark matte black background with faint specks, slight diagonal tilt, slightly low‑angle perspective looking up, shallow depth of field, ultra‑sharp bottle, bokeh background, cinematic chiaroscuro, nostalgic yet modern product‑shot, clean no fingerprints, premium glossy finish
```

*Tip:* You can copy‑paste the whole line into the **Prompt** field.  
If you want to force the “liquid inside” you can add `, filled with dark cola` at the end; if you prefer it empty, omit that clause.

---

## 2️⃣  Negative Prompt (what you want to keep out)  

```
blur, out‑of‑focus, low‑resolution, grain, noise, JPEG artifacts, watermark, text overlay, people, hands, other objects, extra bottles, metal caps, plastic, reflections of studio equipment, lens flare, overexposed highlights, underexposed shadows, color banding, unrealistic glass distortion, cartoon, illustration, painting, sketch, 3D render, low‑poly, clipping, double exposure, motion blur, lens distortion, vignetting, background patterns, wood grain (unless you specifically want a wooden surface), any logos other than Coca‑Cola, bright colorful background, green screen, studio backdrop with grids
```

---

## 3️⃣  Sampling Settings  

| Parameter | Recommended Value | Why |
|-----------|-------------------|-----|
| **Steps** | **35–45** (≈ 40) | Gives enough diffusion time for fine details (glass curvature, droplets, label texture) without over‑smoothing. |
| **CFG Scale** | **7.5–9** (≈ 8)** | Strong enough to lock the iconic Coca‑Cola branding and glass shape, but still allows the model to generate realistic lighting and droplets. |
| **Sampler / Scheduler** | **Euler‑a** (or **DPM++ 2M Karras**) | Euler‑a is fast and produces crisp edges; DPM++ 2M Karras often yields smoother droplet rendering and more natural glass refractions. |
| **Batch size** | **1** (default) | You only need one high‑quality render. |
| **Seed** | **Leave empty** (or set a specific number if you want reproducibility) | Random seed gives a fresh composition; fixing it lets you reproduce the exact result later. |

---

## 4️⃣  Image Dimensions  

| Desired Output | Width × Height (px) | Reason |
|----------------|--------------------|--------|
| **Square** | **1024 × 1024** | Classic product‑shot aspect; fits most UI previews and keeps detail balanced. |
| **Portrait** | **768 × 1024** | If you want a slightly taller composition that emphasizes the bottle’s height. |
| **Landscape** | **1024 × 768** | If you prefer a wider view that can show more of the surrounding droplets. |

Start with **1024 × 1024**; you can always re‑run with a different aspect ratio later.

---

## 5️⃣  Recommended Stable‑Diffusion Model  

| Model | Version | Why it works best for this scene |
|-------|---------|-----------------------------------|
| **Stable Diffusion XL (sdxl_base_1.0)** | v1.0 | XL’s higher‑resolution training data captures fine glass refraction, subtle label gloss, and realistic water droplets far better than older 1.5 models. |
| **Stable Diffusion 2.1 (sd_v2_1_fp16.ckpt)** | 2.1 | If you don’t have XL hardware, SD‑2.1 still offers a strong improvement in detail over 1.5, especially with the `--highres_fix` option. |
| **Alternative – “Cinematic‑Style” LoRA** | Any base + LoRA | Adding a LoRA trained on product photography or glass objects (e.g., `glass_reflection_lora`) can further sharpen the bottle’s specular highlights. |

*Bottom line:* Use **SD‑XL** if your GPU has ≥ 12 GB VRAM; otherwise fall back to **SD‑2.1** with a high‑res fix.

---

## 6️⃣  Quick “One‑Click” Command (for InvokeAI CLI)  

```bash
invokeai \
  --prompt "glass Coca-Cola bottle, classic contour glass design, 355 ml, red and white retro Coca-Cola label with white script and “Cont. Net 355ml”, glossy label, clear slightly green‑tinged glass, smooth polished surface, slender neck, uncapped, partially filled with dark caramel cola, suspended droplets of water frozen in mid‑air around the bottle, high‑speed splash effect, dramatic cool‑toned directional lighting from upper‑left, soft rim highlight on glass, subtle shadows on opposite side, dark matte black background with faint specks, slight diagonal tilt, slightly low‑angle perspective looking up, shallow depth of field, ultra‑sharp bottle, bokeh background, cinematic chiaroscuro, nostalgic yet modern product‑shot, clean no fingerprints, premium glossy finish" \
  --negative_prompt "blur, low‑resolution, grain, watermark, people, hands, extra bottles, metal caps, plastic, studio equipment reflection, lens flare, overexposed, underexposed, cartoon, illustration, 3D render, low‑poly, clipping, double exposure, motion blur, lens distortion, vignetting, background patterns, wood grain, bright background, green screen, any other logos" \
  --steps 40 \
  --cfg 8 \
  --sampler euler_a \
  --width 1024 --height 1024 \
  --model sdxl_base_1.0 \
  --seed -1
```

*(Replace `sdxl_base_1.0` with `sd_v2_1_fp16.ckpt` if you’re using SD‑2.1.)*

---

## 7️⃣  Recap – How the Prompt Captures the Exhaustive Description  

- **Bottle & Label** – All wording about the classic contour glass, red‑white label, “Cont. Net 355 ml”, glossy finish.  
- **Liquid vs. Empty** – The clause “partially filled with dark caramel cola” is optional; you can drop it if you prefer an empty bottle.  
- **Droplets & Splash** – “Suspended droplets of water frozen in mid‑air” + “high‑speed splash effect” reproduces the frozen‑in‑time droplets.  
- **Lighting & Mood** – “dramatic cool‑toned directional lighting from upper‑left”, “soft rim highlight”, “cinematic chiaroscuro” give the cool artificial studio light and subtle shadows.  
- **Background & Surface** – “dark matte black background with faint specks” matches the plain dark surface with specks.  
- **Composition** – “slight diagonal tilt”, “slightly low‑angle perspective looking up”, “shallow depth of field”, “bokeh background” encode the tilt, perspective and focus choices.  
- **Atmosphere** – “nostalgic yet modern product‑shot”, “clean no fingerprints”, “premium glossy finish” convey the mood and cleanliness observed.  

With the settings above you should obtain an image that mirrors the highly detailed, cinematic product photograph described in the exhaustive analysis. Happy rendering!

