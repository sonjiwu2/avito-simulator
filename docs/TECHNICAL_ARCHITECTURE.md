# Browser Game Architecture

## Engine choice and version policy
Default baseline: **Phaser 3.90.0 + TypeScript + Vite**, with Phaser pinned exactly to 3.90.0. This is a deliberate mature baseline, not a claim that 3.90.0 is the newest release. Official docs also expose newer engine generations; do not mix Phaser 4 examples, render filters or import patterns into the pinned v3 project. Before initialization check package availability and supported Node/Vite versions from official sources, then pin the tested toolchain and commit one npm lockfile. Avoid `latest` dependency ranges and unnecessary plugin stacks.

Use Phaser for world rendering, movement, cameras, tilemaps, animation and audio. Use a lightweight typed HTML/CSS overlay for dialogue, accessible menus and workstation mini-apps. Do not mount an entire React app solely for a few modals; if an existing framework is present, adapt rather than rewrite. A small typed event bridge passes serializable commands and snapshots; do not create two independent authoritative game states.

Static host only. No backend/API requirement. New game, save, load, settings and campaign work without an account. Assets bundled or locally served; never depend on hotlinked reference images. PWA/offline caching is a later optional milestone with an explicit update strategy, not a prerequisite.

## Repository layout
```
public/assets/                 validated runtime PNG/audio/fonts/atlases
public/assets/manifest.json    canonical runtime manifest after Codex delivery
src/app/                      boot, config, wiring
src/game/scenes/               Boot, Preload, Menu, Office, Transition
src/game/world/                actors, movement, pathfinding, interaction, depth
src/game/render/               animation adapter, effects, camera
src/domain/                   pure simulation, state transitions, reducers
src/domain/events/             eligibility, selection, consequences
src/domain/tasks/              minigame models and scoring
src/content/                  validated authored event/dialogue payloads
src/ui/                       accessible overlay and localization
src/platform/                 persistence, audio unlock, visibility handling
src/shared/                   IDs and validation types
assets/source/                editable distributable art sources
assets/palette.json           original art palette
content/                      planning seed; migrate playable content explicitly
tools/                        reproducible build/asset/content validators
tests/unit/                   pure rules and serialization
tests/integration/            day transitions, scheduling, compatibility
tests/e2e/                    real browser journeys
docs/                         public contributor and design documentation
docs/reference-images/        concept references; never runtime dependencies
.github/workflows/            maintainable project CI, when implementation begins
```

The planning seed is not runtime content. Copy/compile only validated playable events into `src/content`. Runtime source imports must never read files from a private agent workspace. `public/assets` must not contain full-size concept boards.

## Domain contracts
Authoritative state includes `schemaVersion`, `contentVersion`, run ID, seed, four independent RNG streams, day/time, player state, NPC relation memories, quest/event statuses, project indicators, inventory/decorations, completed minigame outcomes, pending consequences and already-applied transition IDs. State transitions are pure functions or explicit commands around a single store. Scenes subscribe; UI sends commands. Rendering cannot award rewards directly.

Events have stable IDs, prerequisites, exclusions, time windows, priority, cooldown, location, required NPCs, dialogue, evidence, choices, outcome changes and followups. Use declarative typed conditions (flag, day comparison, relation threshold, all/any/not), not executable JavaScript in JSON. Validate all referenced IDs and bound recursion. Effects are typed operations: set flag, add bounded stat, record memory, schedule callback, grant unique item, update task. A transition ID makes applying a selected choice idempotent. Commit outcome + event status + rewards + callbacks as one state update.

Store full random stream state. Gameplay selection, NPC schedule variance, minigame payloads and cosmetic particles use separate streams. Saving after event selection and before its presentation prevents reload rerolls. A deterministic test runner simulates commands without Phaser or DOM.

## World implementation
Use orthogonal Tiled JSON and object layers with stable names: floor, wall-base, furniture-base, foreground, collision, spawns, navigation, interactions. Object custom properties include `id`, `kind`, `interactionId`, `depthAnchor`, `facing`, `requiredFlag`. Tileset IDs are not business IDs. Validate spawn reachability and interaction access.

Player speed about 72 logical px/sec initially; normalized diagonal input. Small foot collider (approximately 12×8) aligns to the declared foot anchor. Static floor collision, interaction radius about 22px, nearest reachable target with focus feedback. Walk depth sorts by actual foot Y plus a stable tie breaker. Tall furniture requires a depth anchor or split foreground; avoid a hard-coded layer that puts every desk over every human.

Pathfinding A* on a navigation grid with static obstacle mask; low-frequency schedule decisions (e.g. 2–4Hz), no all-pairs pathfinding every render frame. Repath on obstruction with a limit, yield or use fallback anchors, never push actors through walls. Store schedule state independently of sprite positions. UI text is not a collision trigger.

Pixel settings: `pixelArt: true`, `antialias: false`, camera roundPixels explicitly retained after camera follow, nearest-neighbor texture filtering, CSS `image-rendering: pixelated`. Fractional physics can still exist; renderer/camera coordinate policy must be tested during movement. Default 640×360 logical view; integer scale 2×/3× on suitable displays with letterbox. FIT is an aspect-ratio fallback and does not guarantee integer pixel scaling. Keep accessible DOM text resolution independent.

## Save/load and recovery
Use IndexedDB for multiple full saves and small localStorage settings if desired; handle quota, unavailable storage and private mode. Autosave on safe event completion and day transitions, with rolling previous-good backup. Never serialize halfway through reward application. Offer 3 manual slots and JSON export/import. Confirm before replacing an occupied slot or resetting a run.

Save envelope contains schema version, content version, timestamp for display only, checksum and payload. Validate imported files with size limits and exact schemas; no eval. Implement sequential migrations and tests. On invalid load, show a helpful recovery action, retain the original file and offer the previous-good save. A content ID removal requires a migration or compatibility mapping. An unknown version must not be silently overwritten.

## Performance and delivery budgets
Initial compressed download target under 12MB; lazy-load other areas/audio. Individual atlas max 2048×2048 on the baseline; measure decoded texture memory and keep normal play under a provisional 128MB texture budget. Prefer several purposeful atlases over one giant file. Limit active costly effects; pool small particles only when profiling justifies it. Prototype 12 named NPCs plus up to 8 anonymous background actors.

Target smooth play on an integrated-GPU laptop at 1366×768 and a modern desktop browser. Verify Chromium, Firefox and WebKit through Playwright where supported, plus one manual Chromium run. Treat 60fps as a measured target, not a guarantee. Record tested hardware/browser and p95 frame time. Suspend audio and simulation when hidden, resume safely, and unlock audio after user gesture. Provide fallback UI if WebGL initialization fails; do not promise full software-renderer parity without testing.

## Verification
Unit: event eligibility, effect idempotency, RNG restoration, costs, partial puzzle outcomes, stat bounds, ending qualification, migrations.
Integration: 30 day transitions, mandatory chain reachability, NPC fallback availability, incident timeout in relaxed mode, callback conflict rules, manifest animation binding.
Browser: new game to day 3 end; reload during dialogue; save after choice; import/export roundtrip; tab hide/resume; keyboard-only workstation; Russian long-text layout; camera motion/desk occlusion; no missing network assets or console errors.
Campaign: automated command simulations for at least 20 seeds and 4 strategies; at least 2 human-played routes through each act; one full end-to-end playthrough before calling the whole campaign shipped. These are gates for future work, not tests already run.

## Maintainable public presentation
README should show what is genuinely playable, one real gameplay screenshot/GIF, controls, objective, saving behavior, accessibility, local commands verified in CI, contributor overview, credits and unofficial-project status. Keep planned features clearly marked. Do not put AI prompts, private reasoning, machine paths, development diary or agent-control instructions in the public README.
