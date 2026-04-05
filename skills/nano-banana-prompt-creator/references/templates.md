# Prompt Templates

## When to use which

- **Markdown sections** → artistic styles, illustrated, infographics, scene-based covers
- **JSON** → photorealistic portraits, fashion editorial, product photography, anything needing camera specs

---

## Markdown Sections Template

```
**Aspect Ratio:** [value]

### Scene
[Overall scene description, color tone, mood]

### Subject
* Gender / age / ethnicity (if person)
* Body type / pose / expression
* Clothing details (fabric, color, fit)
* Accessories

### Environment
* Setting (indoor/outdoor/studio)
* Key background elements
* Color palette / atmosphere

### Lighting
* Source and quality (soft/hard, directional/flat)
* Color temperature (K value for precise control)
* Shadows: minimal / dramatic / soft

### Camera
* Device or lens (iPhone 16 Pro / Hasselblad / 85mm f/1.8)
* Aspect ratio
* Aperture, ISO, shutter speed (for photorealism)
* Composition notes

### Negative Prompts
* [Things to exclude: AI look, plastic skin, blur artifacts, logos, etc.]
```

---

## JSON Template

```json
{
  "meta": {
    "quality": "ultra_photorealistic, raw style, 8k",
    "camera": "iPhone 16 Pro Max",
    "aspect_ratio": "4:5",
    "style": "[e.g. editorial, candid, fashion, street]"
  },
  "scene": {
    "location": "[Setting description]",
    "atmosphere": "[Mood / energy]"
  },
  "subject": {
    "gender": "female/male/non-binary",
    "age": "[range]",
    "ethnicity": "[if relevant]",
    "pose": "[detailed pose description]",
    "expression": "[mood of expression]",
    "clothing": {
      "top": {"color": "", "type": "", "fabric": "", "details": ""},
      "bottom": {"color": "", "type": "", "fabric": "", "details": ""},
      "shoes": {"color": "", "type": ""}
    },
    "hair": {"color": "", "style": "", "length": ""},
    "skin_texture": "Natural matte finish with visible pores, realistic micro-texture"
  },
  "lighting": {
    "type": "[soft cinematic / hard sunlight / beauty dish / ambient]",
    "temperature": "[Kelvin value]",
    "effects": ["[effect 1]", "[effect 2]"]
  },
  "camera_settings": {
    "focal_length": "[mm equivalent]",
    "aperture": "f/[value]",
    "iso": "[value]",
    "shutter_speed": "1/[value]s",
    "depth_of_field": "[deep / shallow]"
  },
  "composition": {
    "shot_type": "[close-up / medium / full body]",
    "angle": "[eye-level / high angle / low angle]",
    "framing": "[rule of thirds / centered / etc.]"
  },
  "post_processing": {
    "editing": "minimal",
    "grain": "[none / light / natural]",
    "color_grading": "[warm / cool / natural]"
  },
  "avoid": ["AI look", "plastic skin", "heavy filters", "unnatural poses"]
}
```
