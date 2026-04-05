# Awesome Skills

A curated collection of Claude Code skills by [Shahar Polak](https://github.com/shaharpolak) and the community.

**Claude Code skills** are markdown files that teach Claude how to approach specific tasks — like a reusable prompt template that gets invoked automatically based on context.

## Skills

| Skill | Description |
|-------|-------------|
| [nano-banana-prompt-creator](skills/nano-banana-prompt-creator/) | Create high-quality image generation prompts optimized for Nano Banana Pro (Google Gemini image generation) |

## Install as a Plugin

```bash
claude plugin install https://github.com/shaharpolak/awesome-skills
```

## Use a Single Skill

Copy any `SKILL.md` directly into your project's `.claude/skills/` directory, or into `~/.claude/skills/` for global access.

## Contributing

1. Fork this repo
2. Add your skill under `skills/<skill-name>/SKILL.md`
3. Run `./validate.sh <skill-name>` to verify it passes validation
4. Open a pull request

Skills follow the standard Claude Code skill format with a frontmatter block:

```markdown
---
name: my-skill-name
description: When to trigger this skill...
---

# Skill content here
```

Skills can also include a `references/` folder alongside `SKILL.md` for supporting files (templates, patterns, examples) that the skill reads at runtime.

## License

MIT — see [LICENSE](LICENSE)
