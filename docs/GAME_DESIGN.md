# Avito: Probation — Game Design Bible
Version 1.0 · Prepared 2026-10-31 · Design targets, not claims about a finished game.

## Contents
1. Product promise and scope
2. Player experience and game loop
3. Time, resources, fairness and progression
4. Office, characters and relationships
5. Campaign and systemic storytelling
6. Twelve minigames
7. Endings, replayability and accessibility
8. Completion criteria

## 1. Product promise and scope
Build a browser-native, single-player, top-down 2D pixel-art office life simulation with light RPG progression and authored branching stories. The working Russian title is **Авито: испытательный срок**; the English title is **Avito: Probation**. The player is an adult intern joining a fictional product team at an Avito-inspired office. This is an unofficial fictional fan project, not a depiction of actual internal systems, real staff or company policies.

The emotional promise: arrive feeling lost, learn where everything is, discover the personalities behind job titles, become useful, make imperfect decisions, and eventually feel that the office is your place. Work should be understandable to a non-programmer. Technical knowledge can unlock flavor dialogue but must not be required to progress.

Three pillars:
- **A place with a life:** colleagues travel, work, take breaks, hold conversations and remember events; empty desks and altered whiteboards communicate yesterday's consequences.
- **Decisions with context:** information gathering, collaboration and boundaries matter; avoid a universal obviously correct button or a hidden morality meter.
- **Small actions, accumulating stories:** a borrowed charger, skipped rehearsal or honest admission can reappear days later with a visible causal connection.

Experience targets: a polished 3-day vertical slice first; then a 10-day first act; then the full 30-day campaign. Target 6–9 hours for a focused first campaign and 8–12 with optional conversations, investigations and decorating. These are pacing hypotheses that must be measured in playtests. Do not inflate duration with walking, repetitive clicking, mandatory grind or waiting for timers.

Full campaign scope: 30 authored days; 120 distinct event premises with three authored choices each; 12 recurring colleagues; 12 minigame families; 8 relationship arcs; 6 endings plus personal epilogues; 4 connected office areas using one coherent tileset. Do not build all content before proving the slice. No multiplayer, real marketplace connection, real user data, live generative dialogue, paid API dependency, account creation, monetization or cloud backend in v1.

## 2. Player experience and game loop
### A day
1. Arrive at 09:30. See a one-sentence recap and two important commitments.
2. Walk through the office; overhear short optional ambient lines.
3. Attend a short stand-up, accept or negotiate one primary assignment.
4. Investigate through desk tools, colleagues, whiteboards and optional evidence.
5. Complete a 2–5 minute minigame or resolve a conversation with meaningful choices.
6. Encounter one social or operational complication; optionally take lunch or explore.
7. Deliver the work, review consequences and choose whether to finish or leave an optional task for tomorrow.
8. Receive a compact end-of-day recap: what changed, who noticed, what carries forward.

The player can move with WASD/arrows, interact with E/Enter, use mouse or keyboard in interfaces, and pause with Escape. Display only the nearest valid interaction prompt. Multiple nearby targets use a small selectable list, never guess silently. Canceling an interaction must return to the same world position safely.

### Two connected play spaces
**Physical office:** spatial exploration, conversations, schedules, ambient discoveries, furniture interactions and relationship scenes.
**Workstation:** fictional task board, messenger, listing inspector, release board, evidence notebook and minigames. Retain a small visible part of the office or a clear return action so it feels like sitting at a desk inside a world.

Opening beats, first 15 minutes: receive a badge; find your desk; ask a human for help; inspect a harmless listing; make one meaningful tradeoff; see the result reflected in a colleague's dialogue. Avoid ten text boxes explaining systems before movement is available.

## 3. Time, resources, fairness and progression
### Clock
Workday 09:30–18:00, with a clearly offered optional evening event. One simulation minute per two real seconds during free exploration is an initial tuning value. Dialogue, reading, settings, menus and minigames pause the world clock. Completing a task applies its stated simulation-minute cost once; do not also run passive time during it. Players can inspect a cost before committing. After the primary commitment and available anchor scenes are resolved or explicitly deferred, offer a clear Finish day action that summarizes remaining work and advances the clock to 18:00. Do not make the player wait for the clock or enforce an artificial minimum duration. Calibrate days toward12–18 minutes through meaningful authored play, then adjust content and costs rather than adding filler.

Never use wall-clock time, time zones, a closed tab or an unfocused browser as simulated work time. Pause on page visibility loss. A narrative incident countdown counts **active incident time** only and supports a relaxed option. Meetings have warning windows and a summary alternative; getting lost once must not irreversibly break the campaign.

### State
| State | Range / behavior | Purpose |
|---|---|---|
| Energy | 0–100, initial 80 | Soft limits on consecutive demanding activities |
| Stress | 0–100, initial 20 | Changes flavor, support options and pacing; never diagnoses the player |
| Team trust | 0–100, initial 45 | Access to collaborative approaches and evaluation context |
| Work quality | Per deliverable 0–100 | Derived from evidence, checks and task decisions |
| Relationship | Each NPC -3 to +3 plus explicit memory flags | Contextual responses; not a gift-farming currency |
| Competencies | Analysis, collaboration, delivery; 0–5 | New approaches, not raw numerical dominance |
| Project health | Named indicators with reasons | Long-term consequences visible in office tools |

Energy below 25 offers a break and lower-intensity alternatives. High stress changes barks and opens support conversations. Bathroom visits, drinking water, disability accommodations, reporting harassment, sick leave and ordinary boundaries never incur moral punishment. Coffee has capped temporary benefit and diminishing returns; it is optional. No all-night grind as the optimal strategy. Player failure produces alternate tasks, support and epilogues, not humiliation.

### Progression and motivation
Week 1: orientation and safe tasks. Week 2: supervised ownership. Week 3: cross-team dependencies. Week 4: feature responsibility and incident preparation. Week 5: launch and mentoring. Week 6: handover, review and an ending.

Pay/stipend is granted weekly and buys optional desk cosmetics. Main story tools and accessibility features are free. Collectibles: office stickers with authored provenance, notebook entries, silly internal awards, photos earned through scenes. Desk personalization persists and appears in the final office panorama. No daily login streaks or pressure mechanics.

## 4. Office and cast
### Four areas
**Main floor:** entrance, lockers, intern desk, team desks, glass meeting room, kitchenette, lounge, printer nook. Introduced day 1. Strong landmarks: lilac carpet at the team, cyan locker, large window, plant wall. Walking paths at least 2 tiles wide; circulation does not cut through collision footprints.
**Product annex:** research room, QA corner, accessibility test desk, quiet pods. Opens day 6 via a visible invitation, not a numerical grind gate.
**Operations room:** incident board and system diagrams, opened day 13 with a mentor. It is a meeting room, not a movie hacker bunker.
**Rooftop / terrace:** lunch and optional social scenes; weather changes the look, not essential access. Available by lift from day 6. No jumping or falling mechanics.

Use believable compact geography. First-time travel can have a conversation; later allow a learned quick route between areas. Do not make every room its own loading screen.

### Twelve colleagues (all fictional adults)
| ID | Name / role | Surface and deeper motive | Schedule / personal prop |
|---|---|---|---|
| vera | Vera, team lead | Calm and specific; protecting time while learning to delegate | Stand-up 10:00, review 15:00; green notebook |
| max | Max, backend mentor | Dry humor; recovering from over-owning every problem | Focus 11:00–12:30, coffee 14:20; duck |
| anya | Anya, QA engineer | Curious rather than adversarial; wants testing involved earlier | QA corner and device desk; labeled cables |
| lev | Lev, product manager | Optimistic, pressured by competing needs; can negotiate | Meeting room 11:30; overfull sticky-note board |
| sonya | Sonya, designer | Observant; wants research translated into decisions | Research room mornings; sketchbook |
| timur | Timur, data analyst | Precise; learning to communicate uncertainty simply | Focus pod 13:00; tiny plant |
| polina | Polina, support specialist | Knows user stories behind metrics; needs sustainable escalation | Calls at 12:00, quiet lunch; mug |
| oleg | Oleg, operations engineer | Methodical; teaches clear incident roles | Operations room afternoons; checklist |
| nika | Nika, accessibility advocate | Witty and pragmatic; dislikes being invited after decisions | Research room and lounge; tactile keyring |
| artem | Artem, fellow intern | Appears confident; afraid to admit uncertainty | Adjacent desk; collectible pins |
| irina | Irina, people partner | Warm but not magical; creates concrete support processes | Entrance mornings, appointments after lunch; calendar |
| denis | Denis, office coordinator | Remembers how the office actually works; has his own priorities | Printer and kitchen rounds; tool pouch |

Eight relationship arcs: Vera/delegation; Max/boundaries; Anya/early QA; Sonya+Nika/inclusive research; Polina/user empathy; Artem/comparison to collaboration; Oleg/incident confidence; Denis/invisible office work. Each arc has 3–4 scenes, one optional discovery, one fork, one later callback and an epilogue variant. Trust is earned through useful attention, honest commitments and repair; lunch choice is not a personality quiz with a mathematically optimal answer.

### Scheduling
Give each NPC a deterministic timetable with location, activity, fallback location and interruption policy. Visible calendar markers explain absence. Critical quest NPCs always offer a messenger appointment or alternate evidence path. Spawn a replacement interaction at the next safe anchor if pathfinding fails; do not teleport in front of the player. NPC avoidance must never lock a quest door or narrow aisle. Conversations stop the participants, not the whole office animation.

## 5. Campaign and systemic storytelling
Use `content/CAMPAIGN_SEED.json` and `EVENT_CATALOG.md`. The catalog is a content scaffold: every event has authored premise and choices; Claude must write complete Russian dialogue, evidence, minigame payloads and consequences before marking it playable. A data row is not finished gameplay.

Main arcs: **Search quality**, **Marketplace trust**, **A usable feature**, **Becoming a colleague**. They overlap without requiring the player to remember dozens of plot threads. Each week closes one question and opens the next.

Event director: deterministic seeded random stream separate from cosmetic randomness; story anchors outrank optional reactive events; at most one active major incident and two optional interruptions; protected focus period after accepting a substantial task. Candidate filters include day range, location, prerequisites, exclusions, cooldown, unfinished followups, NPC availability and repetition family. Select by priority and recency-adjusted weight. Store selection in the save before showing it. Restoring a save must not reroll the queue.

An event is `unseen -> available -> active -> resolved|deferred|expired`. Choices apply once atomically, with durable choice IDs. Consequences can be scheduled for a future day and safe interaction point. Do not process delayed events during a modal or load screen. Explicit repair routes are required for every mandatory chain. Record a short player-facing reason for each major consequence.

At least 24 anchor events need a delayed callback 1–7 days later, at least 12 cross-event conditions, and 8 NPC epilogues. Include a consequence notebook linking a later scene to the remembered decision, without exposing raw flag IDs. Random ambient chatter cannot substitute for authored causal connections.

## 6. Twelve minigame families
Each has a 20-second tutorial, keyboard/mouse parity, relaxed mode, one practice example, a meaningful partial result, three difficulty tiers and at least six **semantically different** payloads. Do not count swapping names or colors as a new puzzle. Full campaign targets 72 playable payloads; vertical slice implements only 3 families with 2 payloads each.

1. **Listing detective:** inspect photo, seller history and messages; select supporting evidence, then approve/request information/escalate. Cheap prices and new profiles alone do not prove fraud. At least one benign false-positive case per tier.
2. **Search relevance:** rank 5–7 listings for a user intent; distinguish exact intent, attributes and irrelevant matches. Show why a result fits; no arbitrary secret order when two are equivalent.
3. **Dependency investigation:** connect symptoms to 4–7 service/evidence cards. Ask for an observation before choosing the failing component. Visual systems puzzle, no terminal knowledge required.
4. **Release planning:** allocate a fixed review budget across risk cards. Dependencies are visible; acceptance is based on residual risk, not clicking every box.
5. **QA reproduction:** arrange reproduction steps, select a device/context and identify the missing condition. Discovery should feel earned, not trial-and-error on hidden combinations.
6. **Support conversation:** choose clarification, empathy and next action using context. Acknowledge uncertainty; never reward making a false promise.
7. **Research synthesis:** group observations and choose which finding supports a design claim. Separate evidence from assumption with multiple valid groupings.
8. **Accessible flow audit:** navigate a small fictional interface with keyboard, locate focus/order/contrast failures and select fixes. Supply text and symbol alternatives.
9. **Data interpretation:** compare a small chart with counts, baseline and uncertainty. Catch missing denominators or a confounder; statistics explanations use plain language.
10. **Capacity balancing:** distribute jobs across limited lanes while respecting dependencies and a fairness constraint. Pauseable planning, not frantic typing.
11. **Incident coordination:** assign roles, choose reversible mitigation, communicate status, then investigate. Use a visible evidence timeline; asking for help is viable.
12. **Demo rehearsal:** select a truthful story, order three examples and prepare one fallback. Unexpected question branches depend on what you actually learned.

Scoring: evidence completeness 40%, validity of reasoning 35%, communication 25% where relevant, with per-puzzle rubric overrides. Display two concrete observations after submission rather than a shaming red grade. Partial success advances the day with a repair task. Never require perfect minigame performance to reach the ordinary completion ending.

## 7. Endings and replayability
Six primary endings, selected by transparent combinations of project outcomes and commitments, not one final choice:
1. **A place on the team:** useful delivery, collaboration and an honest handover.
2. **The careful specialist:** excellent investigation/quality; a specialist path is offered.
3. **The connector:** cross-team work unlocked a sustainable solution.
4. **A different direction:** internship completed, player chooses a better-fitting role; a valid positive ending.
5. **One more iteration:** mixed results, clear support plan and extension.
6. **A graceful departure:** unresolved work or voluntary departure, with closure and practical learning.

Calculate all qualified endings, show evidence, let the player choose among genuinely earned directions. Keep failure and voluntary departure distinct in epilogues. Add per-NPC callbacks and a final desk panorama. An optional post-campaign mode offers explicit new challenge seeds, unresolved side stories and decorating; no false promise of infinite authored content.

Accessibility: adjustable text speed with instant display; scalable UI; Cyrillic-capable font; keyboard remapping; interaction toggle instead of hold; reduced motion; no color-only clues; relaxed deadlines; readable dialogue history; subtitles and separate volume sliders; no screen shake by default; pause anywhere except atomic save operations. Phone portrait mode provides an honest rotate/support notice until touch controls are actually implemented. Desktop keyboard/mouse is the v1 commitment.

## 8. Completion criteria
A campaign day is complete only when it has an opening, traversable places, available NPCs, a finishable assignment, authored complication, optional discovery, state changes, evening transition, save/load coverage and a checked fallback for missed content. A whole campaign is complete only after a real played run from new game to an ending, plus automated alternate-route simulations.

Ship quality means: no placeholder characters in release-critical scenes; no missing frame keys; no text overflow in Russian; no quest softlocks; no duplicated rewards after reload; no invented playtime claims; no production debug overlay; no user-facing AI prompts. When schedule pressure arrives, finish a smaller coherent act and label it clearly rather than displaying 30 hollow days.
