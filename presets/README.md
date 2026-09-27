<!-- SPDX-License-Identifier: CC0-1.0 -->
# Presets (`presets/`)

## ELI5: What belongs here?

A **preset** is a saved recipe for sound. Think of it like a chef's recipe card: instead of twisting every knob and plugging in virtual cables from scratch every time you want an acid bassline or a shimmering ambient pad, a preset restores those settings instantly with one click.

This folder contains factory presets for Nebula's built-in synthesizers and audio effects.

---

## Supported File Formats

1. **Modular Patches (`.nebpatch`):**  
   Complete modular synthesis graphs—specifying which oscillator, filter, envelope, LFO, and mixer modules to instantiate, their knob parameters, and the virtual cables patched between them. Used by the polyphonic modular synthesizer.
   
2. **Device Presets (`.nebpreset`):**  
   Knob snapshots for individual audio effect devices (Delay, Reverb, Parametric EQ, Compressor, Chorus, etc.) or standalone instruments.

Detailed schemas for these formats are documented in [`../FORMAT.md`](../FORMAT.md).

---

## Directory Organization

When populating this folder, organize presets into logical subfolders by sonic character and instrument kind:

```text
presets/
├── bass/           # Sub basses, acid lines, synth basses, 808s
├── pads/           # Warm strings, lush evolving ambient textures
├── leads/          # Solos, piercing leads, melodic hooks
├── keys/           # Electric pianos, organs, bells, plucks
├── fx/             # Risers, downlifters, sweeps, modular noise bursts
└── devices/        # Single-device effect presets (.nebpreset)
```

---

## Naming Conventions

- **File names:** Use clean, descriptive kebab-case or snake_case with clear indicators, e.g.:
  - `neon_lead.nebpatch`
  - `deep_sub_clean.nebpatch`
  - `slapback_vocal.nebpreset`
- **Internal `"name"` field:** A friendly, title-cased name visible in the DAW browser, e.g. `"Neon Lead"`.
- **Sample/Placeholder items:** Must be clearly prefixed with `sample_` in the filename and `[SAMPLE]` in the display name so they are never mistaken for final factory production content.

---

## Rules & Licensing

- **Strict CC0-1.0:** Every patch and preset must be dedicated to CC0.
- **Log every asset:** Every new preset must be recorded in [`../CONTENT_LICENSES.md`](../CONTENT_LICENSES.md).
- **Update index:** Re-run `python tools/build_index.py` after adding presets to keep `index.json` in sync.
