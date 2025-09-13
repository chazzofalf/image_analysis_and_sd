# Tests Overview

This **README** documents the structure and contents of the `tests` directory for the **image_analysis_and_sd** project.  
Each top‑level folder under `tests` represents a **testing session** (e.g., `test_1`).  
Inside a session are **named test cases** (e.g., `test_1/life_of_zethana_the_favored_one_multistories_test`).  
Each test case contains:

* **Input data** – markdown narrative files, source images, etc.  
* A **`run/`** directory with numbered runs (`1`, `2`, `3`, …).  
  * Each run has a `description.md`, a `generated_stable_diffusion_instructions.md`, and a `stable_diffusion_runs/` folder with the generated images.

Below you will find a concise summary for every test case in the repository, together with links to the most important files and visual previews of the generated images.

---


## Test Session: `test_1`

### 1️⃣ `test_1/life_of_zethana_the_favored_one_multistories_test`

**Input files**

| File | Description |
|------|-------------|
| `tfo_narrative_0.md` … `tfo_narrative_7.md` | Narrative fragments used to build the prompt. |
| `the_favored_one.png` | Original input image. |

**Runs**

| Run | Description | Instructions | Images |
|-----|-------------|--------------|--------|
| `run/1` | `run/1/description.md` | `run/1/generated_stable_diffusion_instructions.md` | ![run1‑0](test_1/life_of_zethana_the_favored_one_multistories_test/run/1/stable_diffusion_runs/1.png) ![run1‑1](test_1/life_of_zethana_the_favored_one_multistories_test/run/1/stable_diffusion_runs/2.png) ![run1‑2](test_1/life_of_zethana_the_favored_one_multistories_test/run/1/stable_diffusion_runs/3.png) |
| `run/2` | `run/2/description.md` | `run/2/generated_stable_diffusion_instructions.md` | ![run2‑0](test_1/life_of_zethana_the_favored_one_multistories_test/run/2/stable_diffusion_runs/0.png) ![run2‑1](test_1/life_of_zethana_the_favored_one_multistories_test/run/2/stable_diffusion_runs/1.png) ![run2‑2](test_1/life_of_zethana_the_favored_one_multistories_test/run/2/stable_diffusion_runs/2.png) |
| `run/3` | `run/3/description.md` | `run/3/generated_stable_diffusion_instructions.md` | ![run3‑0](test_1/life_of_zethana_the_favored_one_multistories_test/run/3/stable_diffusion_runs/1.png) ![run3‑1](test_1/life_of_zethana_the_favored_one_multistories_test/run/3/stable_diffusion_runs/2.png) ![run3‑2](test_1/life_of_zethana_the_favored_one_multistories_test/run/3/stable_diffusion_runs/3.png) |

---

### 2️⃣ `test_1/many_pictures_admiral_dogz`

**Input files**

| File | Description |
|------|-------------|
| `AlienSpaceStation.png` | Background image. |
| `Dog1.jpg` … `Dog4.jpg` | Individual dog pictures. |
| `StarfighterAdmiral1.png` … `StarfighterAdmiral3.png` | Additional assets. |

**Runs**

| Run | Description | Instructions | Images |
|-----|-------------|--------------|--------|
| `run/1` | `run/1/description.md` | `run/1/generated_stable_diffusion_instructions.md` | ![run1‑0](test_1/many_pictures_admiral_dogz/run/1/stable_diffusion_runs/0.png) ![run1‑1](test_1/many_pictures_admiral_dogz/run/1/stable_diffusion_runs/1.png) ![run1‑2](test_1/many_pictures_admiral_dogz/run/1/stable_diffusion_runs/2.png) |
| `run/2` | `run/2/description.md` | `run/2/generated_stable_diffusion_instructions.md` | ![run2‑0](test_1/many_pictures_admiral_dogz/run/2/stable_diffusion_runs/0.png) ![run2‑1](test_1/many_pictures_admiral_dogz/run/2/stable_diffusion_runs/1.png) ![run2‑2](test_1/many_pictures_admiral_dogz/run/2/stable_diffusion_runs/2.png) |
| `run/3` | `run/3/description.md` | `run/3/generated_stable_diffusion_instructions.md` | ![run3‑0](test_1/many_pictures_admiral_dogz/run/3/stable_diffusion_runs/0.png) ![run3‑1](test_1/many_pictures_admiral_dogz/run/3/stable_diffusion_runs/1.png) ![run3‑2](test_1/many_pictures_admiral_dogz/run/3/stable_diffusion_runs/2.png) |

---

### 3️⃣ `test_1/scout_image_test`

**Input files**

| File | Description |
|------|-------------|
| `scout.jpg` | Original image of the scout. |

**Runs**

| Run | Description | Instructions | Images |
|-----|-------------|--------------|--------|
| `run/1` | `run/1/description.md` | `run/1/generated_stable_diffusion_instructions.md` | ![run1‑0](test_1/scout_image_test/run/1/stable_diffusion_runs/1.png) ![run1‑1](test_1/scout_image_test/run/1/stable_diffusion_runs/2.png) ![run1‑2](test_1/scout_image_test/run/1/stable_diffusion_runs/3.png) |
| `run/2` | `run/2/description.md` | `run/2/generated_stable_diffusion_instructions.md` | ![run2‑0](test_1/scout_image_test/run/2/stable_diffusion_runs/0.png) ![run2‑1](test_1/scout_image_test/run/2/stable_diffusion_runs/1.png) ![run2‑2](test_1/scout_image_test/run/2/stable_diffusion_runs/2.png) |
| `run/3` | `run/3/description.md` | `run/3/generated_stable_diffusion_instructions.md` | ![run3‑0](test_1/scout_image_test/run/3/stable_diffusion_runs/1.png) ![run3‑1](test_1/scout_image_test/run/3/stable_diffusion_runs/2.png) ![run3‑2](test_1/scout_image_test/run/3/stable_diffusion_runs/3.png) |

---

### 4️⃣ `test_1/starfighter_fighter_generations`

**Input files**

| File | Description |
|------|-------------|
| `test_1/starfighter_fight.md` | Prompt describing the star‑fighter scenario. |

**Runs**

| Run | Description | Instructions | Images |
|-----|-------------|--------------|--------|
| `run/1` | `run/1/description.md` | `run/1/generated_stable_diffusion_instructions.md` | ![run1‑0](test_1/starfighter_fighter_generations/run/1/stable_diffusion_runs/0.png) ![run1‑1](test_1/starfighter_fighter_generations/run/1/stable_diffusion_runs/1.png) ![run1‑2](test_1/starfighter_fighter_generations/run/1/stable_diffusion_runs/2.png) |
| `run/2` | `run/2/description.md` | `run/2/generated_stable_diffusion_instructions.md` | ![run2‑0](test_1/starfighter_fighter_generations/run/2/stable_diffusion_runs/0.png) ![run2‑1](test_1/starfighter_fighter_generations/run/2/stable_diffusion_runs/1.png) ![run2‑2](test_1/starfighter_fighter_generations/run/2/stable_diffusion_runs/2.png) |
| `run/3` | `run/3/description.md` | `run/3/generated_stable_diffusion_instructions.md` | ![run3‑0](test_1/starfighter_fighter_generations/run/3/stable_diffusion_runs/0.png) ![run3‑1](test_1/starfighter_fighter_generations/run/3/stable_diffusion_runs/1.png) ![run3‑2](test_1/starfighter_fighter_generations/run/3/stable_diffusion_runs/2.png) |

---

### 5️⃣ `test_1/the_whole_enchilada_everything`

**Input files**

| File | Description |
|------|-------------|
| `AlienSpaceStation.png` | Background asset. |
| `Dog1.jpg` … `Dog4.jpg` | Supporting images. |
| `tfo_narrative_0.md` … `tfo_narrative_7.md` | Narrative prompts. |

**Runs**

| Run | Description | Instructions | Images |
|-----|-------------|--------------|--------|
| `run/1` | `run/1/description.md` | `run/1/generated_stable_diffusion_instructions.md` | ![run1‑0](test_1/the_whole_enchilada_everything/run/1/stable_diffusion_runs/1.png) ![run1‑1](test_1/the_whole_enchilada_everything/run/1/stable_diffusion_runs/2.png) ![run1‑2](test_1/the_whole_enchilada_everything/run/1/stable_diffusion_runs/3.png) |
| `run/2` | `run/2/description.md` | `run/2/generated_stable_diffusion_instructions.md` | ![run2‑0](test_1/the_whole_enchilada_everything/run/2/stable_diffusion_runs/0.png) ![run2‑1](test_1/the_whole_enchilada_everything/run/2/stable_diffusion_runs/1.png) ![run2‑2](test_1/the_whole_enchilada_everything/run/2/stable_diffusion_runs/2.png) |
| `run/3` | `run/3/description.md` | `run/3/generated_stable_diffusion_instructions.md` | ![run3‑0](test_1/the_whole_enchilada_everything/run/3/stable_diffusion_runs/0.png) ![run3‑1](test_1/the_whole_enchilada_everything/run/3/stable_diffusion_runs/1.png) ![run3‑2](test_1/the_whole_enchilada_everything/run/3/stable_diffusion_runs/2.png) |

---


## How to use this README

* Open any markdown file (e.g., `run/1/description.md`) to see the textual description of the generated image.  
* Open any `generated_stable_diffusion_instructions.md` to view the exact prompt that was fed to Stable Diffusion.  
* Click on the embedded images to view the generated results directly from the repository.

---

*Generated automatically to give a quick, visual overview of every test case and its runs.*
