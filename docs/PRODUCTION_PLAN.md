# Production Roadmap and Acceptance Gates

## Work order
0. Read public specifications and private role prompt; inventory real tools.
1. Install and verify the role-specific local skills using the separate production pack.
2. Codex produces a style proof, iterates the hero and environment kit, then completes the core art gate.
3. Codex pushes a clean art commit to `main` or a clearly named art branch, with validated metadata and previews. If branch protection requires a PR, report the branch and PR; do not claim it is merged.
4. The user starts Claude Code explicitly. Claude reads the checked-out art commit, validates handoff and begins integration.
5. Build and play the 3-day vertical slice; complete remaining art and story content in parallel only after the slice proves the core loop.
6. Expand to days1–10,11–20,21–30, verifying each act before the next.
7. Polish, accessibility, performance, complete-route playtesting and user-facing documentation.

## Gate A — Style proof
Deliver hero turnaround, complete six-frame south walk, desk/chair/plant vignette and one dialogue panel. Review at 1× and integer enlargement; consistent silhouette, anchor, palette, camera and distinct poses. A good-looking high-resolution reference board does not pass this gate.

## Gate B — Core art
Meet ASSET_CONTRACT core requirements. Verify metadata and actual art-preview room. Include source, exports, previews, provenance and truthful readiness. No production game implementation yet. The 5 extra NPCs and other areas can follow in support deliveries while Claude works only in areas with complete art.

## Gate C — Vertical slice, days1–3
Playable entry/menu/save/settings; main floor; core cast schedules; desk/workstation; listing-detective, search-relevance and support-conversation foundations; 9 authored story events and 6 distinct puzzle payloads; at least one delayed consequence and one repair route; playable evening recap and next-day transition. No placeholder hero or furniture in user-facing paths. Implement one real relationship change and one visible desk-state change.

Acceptance: a new player can finish day 3 without a console, no softlock on missed meeting, reload does not duplicate rewards, keyboard-only path works, Russian text fits, world pauses when hidden. Record a real gameplay capture. Do not describe the full 30-day campaign as available yet.

## Gate D — First act, days1–10
Complete the first30 story event premises as playable events, at least 12 optional office situations and 5 minigame families. Add product annex only once support art is ready. Introduce project health and the first incident. Exercise callbacks, independent NPC schedules and recoverable partial outcomes. Run10 seeded progression simulations and two played routes.

## Gate E — Middle act, days11–20
Add cross-team dependencies, accessibility/research/data puzzles, relationship forks and feature ownership. Main30-day arc state is fully serializable. No context reset between weeks. Test interrupted tasks and content migrations. Expand to 8 minigame families and meaningful role-specific approaches.

## Gate F — Launch and closure, days21–30
Complete all 90 story anchors and the30 reactive premises with actual authored Russian runtime text, all 12 minigame families and 6 semantic payloads per family,6 primary endings plus8 personal epilogue variants. Include24+ actual delayed callbacks,12+ cross-event branches and verified mandatory recovery paths. Reachable endings verified by state simulations and actual play. Rebalance premature/dominant endings using measured outcomes.

## Gate G — Release candidate
Profile real devices; check Cyrillic font license/glyphs; import/export save; storage recovery; audio gesture and volume; browser compatibility; reduced motion; text scaling; actual credits; production build and static-host routing/base path. Confirm no broken asset URLs, console errors, secret/debug data or private agent files in staged changes. Public README accurately describes this build and includes real captures. Do not fabricate screenshots or performance results.

## Agent work organization
If the host supports subagents, delegate narrowly with explicit ownership: domain simulation; world/rendering; narrative content; workstation/minigames; integration/QA. Keep one integrator. Separate branches/worktrees for writes, stable schema first, focused diffs and checked interfaces. Do not let two agents edit package-lock, the central store or the same content IDs concurrently. Let reviewers inspect evidence without the implementer’s preferred conclusion. If subagents are unavailable, execute the same milestones serially without inventing delegation.

## Scope control
P0: coherent slice, reliable save/load, movement/interaction, one meaningful consequence, approved art.
P1: complete first act, robust event director, core relationships, workstation tool variety.
P2: full authored campaign, all required art and minigames, endings and accessibility.
P3: optional cosmetics, extra ambient variants, touch, PWA, advanced weather. Never trade P0 reliability for P3 volume.

Track done by observable behavior and gates, not number of files or TODO comments. At a genuine tool/permission block, complete independent work and state the precise missing capability. Do not repeatedly ask whether to continue ordinary authorized work.
