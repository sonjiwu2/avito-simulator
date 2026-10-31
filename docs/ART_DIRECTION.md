# Art Direction and Pixel Animation Specification

## Visual promise
An inviting, believable contemporary office, viewed from above. Warm oak, cream walls, sage furniture, dark monitors, thoughtful Avito-associated cyan/lime/coral/lilac accents. Ordinary adult colleagues with readable silhouettes. Charming objects tell stories: a carefully labeled cable box, an accumulating whiteboard, a mug moved after an argument, a plant watered after a reconciliation.

The supplied generated images establish mood, composition and UI hierarchy. They are **concept references only**: they are more detailed and less geometrically consistent than production sprites. Never crop them into a claimed tileset or use a screenshot as the whole interactive office.

## Camera and coordinate system
Orthogonal top-down RPG camera with a modest visible front face on furniture; no isometric diamonds, perspective vanishing points or 3D camera. All assets share one projection. Tile size 16×16. Character frame 32×48 with a nominal 24×36 occupied silhouette. Normalized origin (0.5,1), visual foot anchor at pixel (16,44), with a 4-pixel transparent safety band below. For placing a character, its image origin remains bottom-center; store `footOffsetY=-4` so depth/collider use the true foot location. Treat that distinction consistently; do not silently use image bottom as feet in one subsystem and actual feet in another.

World logical viewport 640×360; use integer enlargement where practical and letterboxing. Keep UI in a separate high-resolution DOM overlay or well-tested canvas layer; Cyrillic body text remains readable at a 1366×768 browser. Art at 1× must be readable. Extra details must create object identity rather than noisy texture.

## Palette
See `assets/palette.json`. Base palette is an original production starting point, not an official brand specification. 32 named colors, with up to 24 visible colors per character including skin and outfit. Transparent alpha is 0; solid sprite pixels use 255. Very limited explicit effect layers may have graded alpha and must be declared separately. No anti-aliased sprite edges. Use 3–4 tonal clusters per material; reserve darkest outline for silhouette/overlap and strongest saturation for focal accents. Skin-tone variants need distinct full ramps, not a global tint.

## Character specification
Hero: adult dark-haired intern, lavender hoodie, navy trousers, white shoes, cyan badge; name and pronouns selected at new game without changing mechanics. Offer 3 appearance presets through coherent layer swaps after the core set is proven. Twelve named NPCs have distinct hair, silhouette, posture and at least one prop; do not produce twelve palette-swapped clones. Use source layers or reusable hand-authored parts to control identity.

Animation tags per fully supported character:
| Tag family | Directions | Frames | Timing | Loop |
|---|---:|---:|---|---|
| idle | south, west, east, north | 4 each | 240,160,240,360 ms | yes |
| walk | south, west, east, north | 6 each | 100 ms/frame | yes |
| talk | south, west, east, north | 4 each | 140,120,140,240 ms | yes |
| sit-type | north, south | 6 each | 120 ms/frame | yes |
| drink | south | 6 | 140,100,180,220,120,180 ms | no |
| interact | south | 4 | 100,160,160,140 ms | no |
| react | south | 4 | 90,140,220,160 ms | no |

That is 82 frame entries per full set: 16 idle + 24 walk + 16 talk + 12 typing + 6 drink + 4 interact + 4 react. Reuse identical visual cels where a held pose is intentional, but timings and metadata must still represent all entries. Core pack requires the complete hero and 7 core NPC sets; support pack completes the other 5. Do not claim a universal 82-frame NPC set if only walking exists. Other sit directions are explicitly unsupported in v1; map chair orientation must respect it.

Walk poses: contact-left, down-left, passing-left, contact-right, down-right, passing-right. Alternate the planted foot; keep ground contact and natural arm counter-swing; small hip/shoulder changes preserve head volume. A lateral shift of an unchanged standing picture is not a walk cycle. Do not rotate south to obtain north. Mirror east/west only when outfit and prop asymmetry permit; badge and dominant hand must remain correct. Seated typing needs a changed pelvis/leg pose and desk occlusion, not a standing sprite behind a desk.

Animate for performance: idle eyes/blink as held cels, breathing mostly in torso; no perpetual bobbing feet. Walk 10fps, world rendering target 60fps; these are different rates. Do not draw 60 unique frames per second. One-shot callbacks fire once even if the player exits the action early. Smoothly change facing at rest without interpolated blur.

## Environment kit
Produce original modular tile textures, prop sprites and separate occlusion pieces:
- Floors: oak, light tile, sage carpet, lilac team carpet, terrace deck; seamless 3×3 repeat previews.
- Walls: straight, inner/outer corners, doorway, window, glass partition, skirting; compatible seams.
- Desks: 4 variants, occupied/unoccupied, monitors with readable abstract content; monitors separate for blinking/status.
- Chairs: 4 facings, unoccupied; north/south seated alignment documented.
- Shared props: coffee machine (idle/steam), printer (idle/print/jam), doors (closed/opening/open), plant variants, lockers, sofas, beansbags, whiteboards, bins, coat rack, mugs, cables, cards, food boxes, water station, signage.
- Lighting: day/evening window tint, lamp pools, restrained monitor highlights. Keep light overlays separate from base pixel material.
- Interaction feedback: focus outline, talk marker, notebook discovery, task update and gentle success/error pulse. Shapes as well as color communicate status.

Separate prop collision footprint from art bounds. A desk may occupy a 48×32 collision footprint while its monitor extends upward. Separate foreground or `depthAnchor` makes the player render correctly in front/behind. Glass should remain legible without making collision invisible. Do not collide with the entire sprite rectangle if it includes an overhanging screen.

## UI and illustration
Pixel-framed cream dialogue panels; charcoal workstation chrome; restrained cyan primary action; consistent 9-slice corner sizes. Legible Cyrillic UI font with checked license and full glyph coverage. Render all real text in the game, never bake generated pseudo-Russian into an image. Portraits 96×96, cropped within fixed bounds; 4 emotions for hero and core cast. Icons 16×16 and 24×24, matching stroke weight. Scene illustrations optional and loaded on demand.

## Production workflow
1. Inventory actual available tools, permissions and model/image-generation capabilities. A skill does not install an image model or an Aseprite license. Record tool versions privately.
2. Produce one hero master, one desk/plant/chair vignette and a 6-frame walk proof. Compare at native scale to references. Resolve style drift before bulk production.
3. Use image generation for original concept and identity exploration where available. Prefer a controlled editable pixel source for final animation. Generated multi-frame sheets often have inconsistent scale, grids and anatomy; they require real cleanup and cannot pass by appearance alone.
4. Draw or clean actual low-resolution cels in Aseprite or an equivalent controllable raster tool. Keep source layers for limbs/outfit/face. Use automation for export/packing/validation, not as a substitute for character drawing quality.
5. Export transparent PNG plus the explicit project manifest. Aseprite JSON is an intermediate; convert and validate before engine ingestion. Do not assume different atlas formats are interchangeable.
6. Review native-size contact sheets and loop previews on light, dark and checkerboard backgrounds. Check feet, silhouette volume, changing limbs, blink cadence, clipping, alpha and readability.
7. Load a golden test room: walk behind/in front of desks, sit, turn, talk, drink and move through doors. Capture real engine previews. A standalone GIF is necessary but not sufficient evidence.
8. Compare the whole cast and all props together. Rework inconsistent camera angles, outlines, saturation or pixel density.

Never solve a quality problem by increasing resolution, adding blur or a glow. Never label a skeleton PNG sequence, a reference board, a recolored clone or a contact sheet as a finished animated character pack.

## Delivery gates
**Reference gate:** concepts, palette and specifications; not sufficient to start final art integration.
**Core art gate:** hero + 7 NPCs complete, main-floor modular kit, interaction icons, UI panels, 8 portraits, all declared metadata and engine proof; 3-day slice may start after the user commands Claude.
**Full art gate:** remaining cast, annex/operations/terrace kit, 12 portraits, full effects, decorated states and optional cosmetics; full campaign integration.

Core assets should achieve at least 4/5 on readability, identity consistency, pose clarity, palette coherence and motion quality, with no critical technical defect. A score is an internal review tool, not an objective quality guarantee. If image generation is unavailable, state the limitation; do not invent access or silently substitute low-quality procedural main characters.
