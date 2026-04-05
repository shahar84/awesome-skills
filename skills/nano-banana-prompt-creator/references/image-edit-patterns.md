# Image Edit Patterns

Use the right pattern based on the type of change the user requested.

---

## Style Transformation
*(watercolor, ukiyo-e, oil painting, origami, chalkboard, etc.)*

```
[Key: Maintain precise facial features, retain original face structure — use uploaded image as reference. Do not alter face.]

Transform this image into [style]. Preserve the subject's identity, pose, and composition exactly.
Every surface is rendered in [style-specific texture details].
[Style-specific aesthetic rules — e.g. for ukiyo-e: bold ink outlines, flat perspective, mineral pigments, wood grain texture, color misalignment (版ズレ)]
Photorealistic studio render quality.

Aspect ratio: [X]
Negative prompts: photorealistic rendering, digital gradients, AI face
```

---

## Background / Environment Swap
*(new location, different setting, different context)*

```
[Key: Maintain precise facial features, retain original face structure — use uploaded image as reference. Do not alter face.]

Keep the subject exactly as in the reference image — same face, same pose, same clothing, same lighting on subject.

Replace the background entirely with:
[Detailed new environment — location, time of day, key elements, atmosphere, color palette]

Match the lighting on the subject to the new environment's light source.
Seamless composite feel — subject belongs there, not a cutout.

Aspect ratio: [X]
Negative prompts: studio background bleed, hard cutout edges, mismatched lighting, logos
```

---

## Lighting Change
*(golden hour, dramatic, soft, moody, etc.)*

```
[Key: Maintain precise facial features, retain original face structure — use uploaded image as reference.]

Same subject, same pose, same clothing as reference image.

Change the lighting to:
[New lighting — type (hard/soft/directional), source direction, color temperature in K, shadow quality, mood effect]

Adjust skin tones and color grading to match new light.
[If outdoors: specify sun angle, time of day]

Aspect ratio: [X]
Negative prompts: original lighting bleed, mismatched shadows, AI look
```

---

## Outfit / Clothing Change

```
[Key: Maintain precise facial features, retain original face structure — use uploaded image as reference.]

Same subject (face, hair, body proportions) as reference.
Same pose and background.

Change clothing to:
[Detailed new outfit — each garment: color, fabric type, cut/fit, details, how it drapes/fits]

Fabric physics should look realistic — describe expected wrinkles, drape, tension where relevant.

Aspect ratio: [X]
Negative prompts: AI look, plastic skin, unnatural fabric, logos
```

---

## Face Swap (Multi-Image Reference)
*(replacing a face in an existing image with a face from a reference photo)*

### How it works in Nano Banana:
- **Image 1** = the face you want to USE (the reference face)
- **Image 2** = the target scene / body (the image you want to place the face INTO)
- **Order is critical** — getting it backwards confuses the model

### Standard prompt (opposite genders, or clear visual distinction):
```
Insert the face of the person from Image 1 into the body of the person in Image 2.

[Face descriptor — paste the confirmed analysis here, e.g.:]
The person in Image 1 is a bald man in his mid-40s, square jaw, dark brown deep-set eyes,
clean-shaven, light olive skin, neutral expression, prominent brow.

Preserve the exact facial features, bone structure, skin tone, and eye color from Image 1.
Adapt the lighting on the face to match the environment and light direction in Image 2.
Seamless, natural blend. No visible composite artifacts.

Aspect ratio: [match Image 2's ratio]
Negative prompts: AI look, visible seam, mismatched lighting, wrong identity, plastic skin
```

### Same-gender challenge:
When both images show the same gender, Nano Banana success rate drops from ~85% to ~5%.
**Fix: Gender-swap the target scene first:**

**Step 1 prompt (send Image 2 only):**
```
Convert the person in this image to the opposite gender.
Maintain exact same pose, background, clothing style, and composition.
Only change the person's gender appearance — nothing else.
```

**Step 2 prompt (send Step 1 result as Image 2, original face photo as Image 1):**
```
Insert the face of the [man/woman] from Image 1 into the [woman/man] in Image 2.
Preserve the exact facial features, skin tone, and bone structure from Image 1.
Adapt lighting on the face to match Image 2's environment.
[Describe both people to help AI identify: e.g. "bald man from Image 1" / "blonde woman in Image 2"]
Seamless, photorealistic composite.

Aspect ratio: [match Image 2]
Negative prompts: wrong face, AI look, mismatched lighting, visible seam
```

### Pro tips:
- Add physical descriptors to the prompt to reduce confusion (bald, beard, age, etc.)
- High-res, front-facing, well-lit reference photos → much better results
- If result is wrong on first try — tweak the description and regenerate (not a 100% success rate tool)
- Glasses, extreme angles, heavy occlusion → reduce quality significantly

---

## Mood / Color Grade Change
*(darker, warmer, more cinematic, desaturated, etc.)*

```
[Key: Maintain precise facial features, retain original face structure — use uploaded image as reference.]

Same scene, same subject, same composition as reference.

Change the mood and color grading to:
[Describe: contrast level, saturation, color temperature shift, shadow depth, highlight rolloff]
[Describe the emotional feel: e.g. "melancholic and cold", "warm and golden", "high-contrast noir"]

Do not change the composition, subject, or lighting direction — only the grade.

Aspect ratio: [X]
Negative prompts: overexposed, washed out, AI look
```
