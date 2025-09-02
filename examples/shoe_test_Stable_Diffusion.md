Thinking...
We need to output: Positive Prompt, Negative Prompt, Step Count, CFG Scale, Suggested Image Dimensions, best stable diffusion model, best scheduler, plus exhaustive description combined. Probably separate sections. Provide in plain text. Let's craft.
...done thinking.

**Exhaustive Prompt Description (one continuous, highly‑detailed paragraph)**  

A studio‑style product photograph of a brand‑new white New Balance athletic sneaker, shown slightly off‑center and rotated diagonally so the toe points toward the lower‑right corner of the frame and the heel angles toward the opposite side. The upper is a pristine, matte‑white blend of breathable mesh, smooth synthetic leather‑like panels and lightweight TPU overlays. White laces run through chrome‑tone eyelets; the laces are loosely untied, hanging gently from the top and spilling over the tongue, with clean white tips extending outward to the right. Subtle dark‑gray/black sidewall panels and a small black mark/patch near the heel provide contrast, while deep navy‑blue accents appear on the interior tongue padding, heel overlay and the thin edge of the outsole. The iconic “N” logo, rendered in dark gray, is prominently displayed on the lateral side. The midsole is a flawless white rubber; the outsole is a contrasting navy‑blue tread with fine rubber grooves that catch the light. The shoe rests on a warm, medium‑dark brown wooden floor that fills the background; the wood shows a natural horizontal grain and a polished matte sheen. A faint white electrical cord runs across the floor in one version, adding a subtle domestic hint. Soft, diffused studio lighting from a large softbox placed slightly above and to the left creates gentle, feathered shadows that fall to the right and rear, modelling the shoe’s contours without harsh highlights. The camera is positioned slightly above the plane of the shoe, angled downwards enough to capture the side profile, the lace eyelets, the “N” logo and a glimpse of the toe box, with a shallow depth of field that keeps the sneaker razor‑sharp while the wooden floor recedes into a gentle blur. The overall mood is clean, minimalist and professional – ideal for e‑commerce, catalogue or brand‑identity use – with no extraneous props, only the warm wood and subtle lighting to ground the product.  

---

### InvokeAI Settings

| Setting | Value |
|---------|-------|
| **Positive Prompt** | `white New Balance sneaker, clean white upper, mesh and synthetic leather, navy blue accents on tongue and heel, dark gray side panels, black heel patch, iconic "N" logo, white laces loosely untied, white rubber midsole, navy blue tread outsole, warm polished wooden floor, subtle white cord, soft diffused studio lighting, gentle feathered shadows, slight diagonal rotation, off‑center composition, shallow depth of field, high‑detail, product photography, minimalist, professional` |
| **Negative Prompt** | `blur, low‑resolution, distortion, watermark, text, people, hands, background clutter, glossy reflections, harsh shadows, overexposed, underexposed, lens flare, grainy, noisy, motion blur, double exposure, unrealistic colors, cartoon, painting, illustration, abstract` |
| **Steps** | **30** (gives enough refinement for fine texture on mesh, wood grain and outsole tread) |
| **CFG Scale** | **7.5** (balances adherence to prompt with creative detail) |
| **Suggested Image Dimensions** | **1024 × 1024** (square works well for e‑commerce thumbnails; keep high enough resolution for detail) |
| **Best Stable Diffusion Model** | **Stable Diffusion XL 1.0 (SDXL‑base‑1.0)** – excellent at rendering realistic materials, fine textures and accurate lighting. |
| **Best Scheduler** | **Euler‑a (Euler ancestral)** – provides smooth, high‑quality convergence for detailed product shots. |

**Quick usage tip:**  
If you need a rectangular “banner” version for a website header, simply change the dimensions to **1152 × 640** (or any 16:9 ratio) while keeping the same prompts and settings; the model will preserve the composition and keep the sneaker centered within the new aspect ratio.

