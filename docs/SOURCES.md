# Primary Sources and Design Decisions
Checked 2026-10-31. Specifications are original design; sources ground the tools and integration conventions.

| Official source | What to verify / why it matters |
|---|---|
| https://docs.phaser.io/api-documentation/3.90.0/constant/core | Pinned Phaser 3 config, pixelArt/roundPixels; read source/examples when prose is ambiguous |
| https://docs.phaser.io/phaser/concepts/cameras | Camera follow and pixel rounding; explicitly retain roundPixels after follow |
| https://docs.phaser.io/phaser/concepts/animations | Frame-based animation, animation keys and per-frame timing |
| https://docs.phaser.io/phaser/concepts/loader | Spritesheet/atlas loading contracts and caching |
| https://docs.phaser.io/api-documentation/3.90.0/constant/scale | FIT preserves aspect ratio, does not promise integer enlargement |
| https://www.aseprite.org/docs/cli/ | Batch export, sheets, tags, JSON formats and padding |
| https://www.aseprite.org/docs/sprite-sheet/ | Frame export/import conventions |
| https://doc.mapeditor.org/en/stable/manual/objects/ | Spawn points, collision rectangles, interaction objects and stable properties |
| https://doc.mapeditor.org/en/stable/manual/custom-properties/ | Data-driven map annotations |
| https://learn.chatgpt.com/docs/build-skills | Codex local skills and progressive disclosure; project .agents/skills |
| https://code.claude.com/docs/en/skills | Claude Code skills; project .claude/skills and personal scope |

Phaser has newer major-generation documentation too; the chosen baseline is intentionally3.90.0. Consult version-matched API pages. The generated references are original concept images; they are not borrowed game assets or evidence of working animation. The 30-day story, event catalog and pacing are design proposals that need playtesting. Aseprite is optional and its executable/license is not bundled or installed by a text skill. AI image-generation access is host-specific; the production prompt requires explicit capability detection.
