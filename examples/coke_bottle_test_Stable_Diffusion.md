Thinking...
We need to output info suitable for recreating it in InvokeAI: Positive Prompt, Negative Prompt, Step Count, CFG Scale, Suggested Image Dimensions, best model and scheduler. Use the description above. Provide concise prompts. Positive prompt describing bottle, label, lighting, background. Negative prompt: avoid watermarks, text, distortion, low quality, etc. Steps maybe 30-50. CFG 7-8. Dimensions 768x1024 or 512x768. Model: stable diffusion 2.1 or 2.1-base? Maybe "Deliberate" for photorealistic? Or "sdxl" for higher quality. Scheduler: DPM++ 2M Karras. Provide.

Now craft final answer.
...done thinking.

**✅ Quick‑reference for recreating the “Coca‑Cola glass‑bottle” image in InvokeAI**

| Item | Recommendation |
|------|----------------|
| **Stable‑Diffusion model** | **SDXL‑Base 1.0** (or **Stable Diffusion 2.1‑Base** if you need a lighter model).  SDXL gives the richest colour fidelity for glass, reflections and the deep amber cola. |
| **Scheduler** | **DPM++ 2M Karras** – produces smooth, high‑detail results with clean bokeh. |
| **Steps** | **45 steps** (30 – 50 works; 45 is a safe middle‑ground). |
| **CFG scale** | **7.5** (balances prompt adherence with a natural‑looking photographic look). |
| **Image size** | **768 × 1024 px** (portrait‑oriented, good for the bottle’s tall silhouette).  If you prefer a square crop, use **1024 × 1024 px** and add a slight “crop‑to‑portrait” after generation. |
| **Seed** | Set to **‑1** (random) or lock a seed you like after the first run. |

---

## 🎨 Positive Prompt  
*(All essential visual cues are listed; you can copy‑paste the whole line or cherry‑pick the most important parts.)*

```
photorealistic close‑up of a classic Coca‑Cola glass bottle, iconic contoured shape, clear soda‑glass with subtle dark amber cola inside, bright red circular logo with white outline and white Spencerian script, crisp white label border, bottle resting on a smooth matte‑black surface, shallow depth of field with creamy bokeh background, soft diffused studio lighting, specular highlights tracing the glass curvature, gentle shadow on the surface, optional ice cubes floating in the cola, optional industrial hydraulic press plate lightly pressing the neck (demonstrating durability), cool neutral background tones, high‑resolution, ultra‑sharp label details, realistic reflections, subtle vignette, 8K‑quality, award‑winning product photography
```

**Tip:** If you want the “press‑test” version, add `, hydraulic press plate pressing the neck, slight glass deformation` at the end of the prompt. If you want the “refrigerator‑door” version, replace that part with `, bottle perched on a white refrigerator door, soft indoor lighting`.

---

## ❌ Negative Prompt  
*(Filters out common artefacts and unwanted styles.)*

```
low‑resolution, blurry, jpeg artifacts, watermark, text overlay, logo glitch, cartoon, illustration, painting, sketch, anime, 3d render, low‑contrast, oversaturated, banding, chromatic aberration, lens flare, dust, scratches, fingerprints on glass, missing label, mis‑aligned logo, double exposure, distorted perspective, unrealistic glass thickness, over‑exposed highlights, under‑exposed shadows, grain, noise, vignetting that cuts off bottle, unrealistic reflections, background clutter, people, hands, other objects, text in background, neon, hologram, glitch, surreal, fantasy, oil painting, pastel, watercolor
```

---

### How to use it in InvokeAI (CLI example)

```bash
invokeai \
  --model sd_xl_base_1.0.safetensors \
  --prompt "photorealistic close‑up of a classic Coca‑Cola glass bottle, iconic contoured shape, clear soda‑glass with subtle dark amber cola inside, bright red circular logo with white outline and white Spencerian script, crisp white label border, bottle resting on a smooth matte‑black surface, shallow depth of field with creamy bokeh background, soft diffused studio lighting, specular highlights tracing the glass curvature, gentle shadow on the surface, optional ice cubes floating in the cola, optional hydraulic press plate lightly pressing the neck (demonstrating durability), cool neutral background tones, high‑resolution, ultra‑sharp label details, realistic reflections, subtle vignette, 8K‑quality, award‑winning product photography" \
  --negative_prompt "low‑resolution, blurry, jpeg artifacts, watermark, text overlay, cartoon, illustration, sketch, anime, 3d render, low‑contrast, oversaturated, banding, chromatic aberration, lens flare, dust, scratches, fingerprints on glass, missing label, mis‑aligned logo, double exposure, distorted perspective, unrealistic glass thickness, over‑exposed highlights, under‑exposed shadows, grain, noise, vignetting that cuts off bottle, unrealistic reflections, background clutter, people, hands, other objects, text in background, neon, hologram, glitch, surreal, fantasy, oil painting, pastel, watercolor" \
  --steps 45 \
  --cfg 7.5 \
  --width 768 \
  --height 1024 \
  --scheduler dpmpp_2m_karras \
  --seed -1 \
  --output ./coke_bottle_test.png
```

Adjust `--width`/`--height` or add `--sampler ddim` if you prefer a different sampler, but the combo above (SDXL‑Base + DPM++ 2M Karras) consistently yields the cleanest, most photographic result. Happy generating! 🚀

