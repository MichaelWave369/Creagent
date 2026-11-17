# Creagent

**Creagent** is an open, portable agent skill for exploring a hand-drawn **Theory of Experience (TOE)** as a *relational map*. It connects symbolic concepts from mythology, religion, philosophy, and human experience without asserting that those concepts are physically real or equivalent.

> **Not a physical map and not a scientific Theory of Everything.** It is a navigable model of symbolic relationships. Its central reference point is the viewer: mind, body, soul, and choice.

## Core frame

| Direction or domain | Interpretation in the source diagram |
| --- | --- |
| Up | Oneness (ONE / Eden) |
| Down | Nothingness (Rotten / Abyss) |
| Left | Inward exploration (Moon / Jacob's Ladder) |
| Right | Outward exploration (Sun / Tower of Babel) |
| Top-right / bottom-left | Additional outward / inward diagonal cues |
| Center | The viewer, with mind, body, soul, and choice |
| Red / yellow / green / blue / purple | Reality / Dreamspace / Limbo / Quantum / Astral |
| Central spine | Yggdrasil, spanning above to abyss |
| Boundaries | Bardo (death-transition band), Ouroboros (outer symbolic enclosure) |

Asgard/Svarga and Tokoyo/Patala/underworld traditions are placed beyond the central material-plane square. The Mountain sits above the Astral layer, while the Rotten sits below it in the source design. These are **relationships as drawn**, not cross-tradition historical equivalences.

## Contents

```text
skills/creagent-toe/
  SKILL.md                 # Portable agent skill entrypoint
  references/map-guide.md  # Reading rules, interpretations, boundaries
  assets/ontology.json     # Machine-readable nodes, layers, axes and edges
  scripts/explore.py       # Offline graph validator / explorer (Python stdlib)
tests/test_explore.py      # Local checks and invariant tests
.github/workflows/test.yml # CI for tests
```

## Install in a skills-compatible agent

Copy the `skills/creagent-toe` directory into the skills directory your agent supports. The exact destination and activation mechanics vary by client. The agent reads `SKILL.md` when a request matches its description; the skill can consult its references and ontology only as needed.

## Local exploration

Python 3.10+; no external dependencies or network required.

```bash
python skills/creagent-toe/scripts/explore.py validate
python skills/creagent-toe/scripts/explore.py list --kind node
python skills/creagent-toe/scripts/explore.py neighbors viewer
python skills/creagent-toe/scripts/explore.py path moon sun
python skills/creagent-toe/scripts/explore.py show bardo
python -m unittest discover -s tests -v
```

The `path` command returns the **shortest graph connection**, not a metaphysical journey, a physical route, or verified causality.

## Example agent prompts

- "Read the Creagent map. What connects the Moon and Sun? Label speculation clearly."
- "Compare Bardo and Ouroboros without collapsing Buddhist and other traditions."
- "Trace an imagined inward journey from the viewer toward the Moon."
- "Give me a structured explanation of the five color bands and their boundaries."
- "Suggest one testable, psychology-oriented research question inspired by the observer in the center."

## Provenance and limits

This initial model transcribes a user's **work-in-progress hand-drawn diagram and their explanatory description**. Several symbol positions and connections are interpretive abstractions made for navigation; see the `epistemic` and `source` fields in `ontology.json`. The original diagram image is intentionally not included pending provenance and redistribution permission. No historical, theological, clinical, or physical claim is established by this project.

Contributions and corrections are welcome, especially when they preserve distinctions among traditions, link primary sources, and separate evidence from analogy.