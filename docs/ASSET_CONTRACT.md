# Art-to-Engine Handoff Contract v1

## Ownership and sequencing
Codex owns original art, editable sources, validated exports and a small art-preview harness. Claude Code owns the playable game, world simulation, UI integration, campaign, tests and user documentation. Codex may author a technical preview room to verify assets; it must not start building the campaign. Claude must not silently redraw core characters or reinterpret approved frame coordinates.

The user launches Codex first and explicitly launches Claude only after the core art handoff has been committed and pushed. Reference images alone do not satisfy this gate. In the initial repository `assets/production-status.json` says `reference-only`, `coreReady: false`, `fullReady: false`; this is intentional and truthful.

## File locations
- `assets/source/characters/<id>/...`: editable layered sources and original frame sequence, with provenance.
- `assets/source/environment/...`: modular environment sources.
- `public/assets/characters/<id>.png`: fixed-grid runtime sheet.
- `public/assets/props/`, `tilesets/`, `portraits/`, `ui/`, `effects/`: runtime images.
- `public/assets/manifest.json`: canonical metadata contract consumed by the engine adapter.
- `assets/ART_HANDOFF.json`: version, gate, validation evidence and hashes of reviewed outputs.
- `docs/art-previews/`: curated actual loop previews and test-room captures, not all working iterations.
- `docs/reference-images/`: supplied concepts, explicitly non-runtime.

Use lowercase kebab-case ASCII paths and stable IDs. Do not store absolute machine paths, local file URLs or expiring signed URLs. Asset paths in the runtime manifest are relative to `public/assets`. Source paths are relative to repository root. References remain outside runtime loading.

## Canonical manifest
Top-level fields: `schemaVersion:1`, `contractVersion:"1.0.0"`, `gate:"core"|"full"`, `assets:[...]`.

Each asset has `id`, `kind`, `status:"approved"`, `path`, `sha256`, `width`, `height`, `sourcePath`, `provenance:{method,rightsNote}`. Kinds: character, prop, tileset, portrait, ui, effect. Use only PNG in the image manifest. Fonts/audio use their own typed manifests and credits. `method` truthfully identifies generated-and-cleaned, original-hand-authored or licensed-source; `rightsNote` records actual provenance and any dependency. A note is not a legal warranty.

Character assets additionally contain:
```
"sheet": {"frameWidth":32,"frameHeight":48,"columns":8,"rows":11},
"origin": {"x":0.5,"y":1},
"footAnchor": {"x":16,"y":44},
"collider": {"width":12,"height":8,"anchor":"foot"},
"animations": [
  {"key":"idle-south","frames":[0,1,2,3],
   "durationsMs":[240,160,240,360],"loop":true}
]
```

Complete exact keys: idle/walk/talk each south, west, east, north; sit-type north and south; drink-south, interact-south, react-south. Frame counts: idle4, walk6, talk4, sit-type6, drink6, interact4, react4; total 82 entries. Use exactly 8 columns ×11 rows for the first contract; trailing6 cells unused and transparent. Frame indices row-major. A frame can be referenced twice for held animation, but walk must have 6 visually distinct cels. Durations positive integers >=40ms. No rotated or trimmed frames; source pivot must stay fixed. Props with animation use their own declared fixed grid and keys. Tilesets declare tile size16, spacing0, margin0. UI assets may declare 9-slice borders; portraits are96×96.

Why fixed grids: straightforward deterministic slicing, no per-frame trim jitter, less adapter ambiguity. Aseprite `--format json-array`/`json-hash` exports are intermediates. Build a conversion step that produces this contract; never call raw Aseprite JSON the runtime manifest.

## Required core bundle
Characters hero, vera, max, anya, lev, polina, artem, denis, all 17 tag keys and 82 entries each. Core world IDs: floor-oak, floor-tile, floor-carpet, wall-office, desk-main, chair-north, chair-south, meeting-glass, door-office, coffee-machine, printer, locker, sofa, plant-small, plant-large, whiteboard, interaction-icons, dialogue-panel, workstation-panel. Include corresponding 8 portraits as `portrait-<character-id>`. Core callback scenes must only use these characters until support art arrives.

The exact number of tile images and prop sheets is flexible; unique asset IDs map logical use to physical files. Reusing one physical PNG for several declared logical entries is allowed only if metadata is explicit and all views are real. No invisible placeholder PNGs or conceptual furniture boards.

Full adds sonya, timur, oleg, nika, irina complete sets and portraits, product-annex/operations/terrace modular kit, all final day variants and campaign effects. Optional cosmetics can follow later and must not block story completion.

## Validation and evidence
Run the delivered validator using repository root and manifest. It verifies image dimensions, PNG decoding, file hash, fixed-grid agreement, bounds, durations, tag coverage, binary alpha, nonempty referenced character cels, 6 distinct walk cels, source existence, required asset IDs and provenance fields. It rejects path traversal and unapproved status. Machine checks cannot judge artistic quality, semantic pose correctness or whether a source is genuinely editable; visually inspect those.

For each core character export native-scale contact sheet and annotated4× nearest-neighbor loop previews; watch at least 3 loops in all walk directions. Check real timing, foot sliding, head-volume drift, repeated frames and awkward seam. Test world occlusion, seated alignment and actual foot depth in the art preview room. Keep a compact evidence list with paths, reviewed tag families, result and known limitations.

`assets/ART_HANDOFF.json` fields: schemaVersion 1; contractVersion; gate; generatedAt; manifestSha256; validationCommand; validationPassed; reviewEvidence[]; requiredAssets[]; knownLimitations[]; coreReady; fullReady. Set readiness true only after both machine validation and visual review. The commit containing the handoff is the immutable integration input; report its SHA after pushing. Do not embed a commit’s own SHA in that same commit (self-reference is impossible). Claude records the reviewed source commit in its integration notes after checkout.

If a quality or tool limit prevents completion, keep the gate false, publish honest partial progress on an art branch and list missing IDs. Do not manufacture a PASS file. Breaking changes require a contract version bump and explicit adapter migration, not silent renaming.
