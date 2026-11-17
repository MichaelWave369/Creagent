---
name: creagent-toe
description: Explore and explain a symbolic Theory of Experience (TOE) relational map centered on a viewer with mind, body, soul, and choice. Use when users ask to interpret the Creagent map, compare Moon/Sun inward-outward paths, discuss oneness/nothingness, interpret its five colored layers, trace Yggdrasil/Bardo/Ouroboros links, or turn those symbolic relationships into structured knowledge graphs, journeys, or creative simulations.
compatibility: Works in any Agent Skills-compatible client. Optional graph explorer requires Python 3.10+; no network required.
metadata:
  author: MichaelWave369 community project
  version: "0.1.0"
---

# Creagent: relational-map interpreter

## Prime directive

Treat the Theory of Experience (TOE) diagram as a **symbolic relational model**, not a physical atlas, theological proof, objective afterlife map, or scientific Theory of Everything. The image's categories are *conceptual labels*. Terms such as "Quantum" and "Astral" are symbolic labels **unless supported by independently defined, testable claims**. Never substitute a metaphor for empirical evidence.

The user-provided diagram and explanation are the primary **design source**, not an external authority for historical or scientific assertions.

## When activated

1. Read `references/map-guide.md` for the visual conventions and the source-versus-interpretation rules.
2. For concrete navigation, read `assets/ontology.json`; optionally run `python scripts/explore.py validate` before using it. All referenced paths are relative to this skill's directory.
3. Identify the requested mode:
   - **Read:** explain symbols, axes, and layers as drawn.
   - **Trace:** find a graph path or generate a *hypothetical* experiential itinerary.
   - **Compare:** examine motifs across traditions, including crucial differences and provenance.
   - **Model:** propose ontology/schema or export graph relationships without inventing source support.
   - **Create:** compose reflective writing, worldbuilding, prompts, educational exercises, or an interactive concept based on the map.
4. Return an actionable answer in the user's requested format. Default to a short thesis, a compact relationship trace, and a note about ambiguity or evidence where material.

## Orientation to memorize

- **Vertical axis:** up = oneness (ONE/Eden); down = nothingness (Rotten/Abyss).
- **Horizontal axis:** left = Moon/Jacob's Ladder/inward journey; right = Sun/Tower of Babel/outward journey.
- **Diagonal cues:** top right = outward; bottom left = inward. Do not erase these to force a perfectly orthogonal geometry.
- **Center:** viewer with mind, body, soul, and *choice*; the viewer is the reference, not a universal coordinate origin in physics.
- **Nested colored fields:** red Reality, yellow Dreamspace, green Limbo, blue Quantum, purple Astral. Nested is a drawing relationship, not evidence of ontological containment.
- **Spine:** Yggdrasil bridges the upper and lower ends.
- **Other realms:** Asgard/Svarga and Tokoyo/Patala/underworlds lie outside the central material-plane square, according to the drawing.
- **Boundaries:** Bardo is shown as a death-transition band toward Astral; Ouroboros circles outside Astral.
- **Extremes:** the Mountain / holy cities lie above Astral; the Rotten / decay lies beneath Astral.

## Required reasoning discipline

- Keep **diagram fact**, **agent interpretation**, **tradition-specific scholarship**, and **empirically supported science** separate. Signal which is which.
- Never claim names drawn near one another are synonymous (e.g., Bifröst ≠ Jacob's Ladder, Bardo ≠ Ouroboros, Svarga ≠ Asgard).
- When a historical or scientific assertion matters, use verifiable sources if available and state uncertainty when not.
- Do not present graph paths as causal mechanisms, psychic access, medical/mental-health diagnosis, or directions to a literal destination.
- For sensitive experiences (distress, unusual perceptions, grief), respond supportively and keep metaphysical interpretations optional rather than asserting them as fact.
- If the source drawing leaves something unclear, mark it `unresolved` instead of filling the gap with certainty.

## Graph usage

`assets/ontology.json` contains `axes`, `layers`, `nodes`, and `edges`. Node coordinates are *illustrative* and not scanned measurements. Relationships have a `type`, `epistemic`, and explanatory `note`.

```bash
python scripts/explore.py list --kind node
python scripts/explore.py show viewer
python scripts/explore.py neighbors yggdrasil
python scripts/explore.py path moon sun
python scripts/explore.py validate
```

When reporting a shortest path, name every intermediary and disclose that the graph uses undirected traversal for convenience even if a relationship has a conceptual direction.

## Reusable output form

**Reading:** State what the diagram depicts.

**Relationship:** Give a trace such as `Moon → viewer → Sun`, with relationship names, and clearly say if inferred.

**Interpretation:** Offer one or more possible readings without false equivalence between traditions.

**Boundary:** Explain what this map does *not* prove and what remains open.

## Suggested integrations

- **ULGE:** represent symbol-to-concept translations and preserve disagreements.
- **AKASHA / PhiPonder:** attach primary texts, commentary, and provenance to motifs.
- **PhiWorldForge:** make a creative, navigable world with clear "fictional/symbolic" labeling.

Do not edit remote repositories, make external API calls, or claim to have installed this skill unless the current environment genuinely provides and authorizes those operations.