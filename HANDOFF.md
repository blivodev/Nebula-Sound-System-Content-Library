<!-- SPDX-License-Identifier: CC0-1.0 -->
# HANDOFF — Read This First (Content Library Repo)

**Audience:** Any AI agent or human sound designer picking up the **Nebula Sound System Content Library** (`Nebula-Sound-System-Content-Library`) cold.

---

## 1. Project in Three Lines

This repository contains the official factory sound library for [Nebula Sound System](https://github.com/blivodev/Nebula-Sound-System): presets, drum kits, one-shot samples, tempo-synced loops, and demo projects. Everything in this library is strictly dedicated to the public domain under **CC0-1.0**.

---

## 2. Session — 2026-09-27: Seeding the Content Library Repository Skeleton (Phase 9 Scaffolding)

### What Was Done
1. **Top-Level Kind Directories & READMEs:**
   - `presets/README.md`: Explains modular patches (`.nebpatch`), device presets (`.nebpreset`), subfolder classification (`bass/`, `pads/`, `leads/`, `keys/`, `fx/`, `devices/`), and loading into the DAW.
   - `kits/README.md`: Explains drum kits (`.nebkit`), 4×4 pad grid (General MIDI notes 36..51), choke groups, and sample mapping.
   - `one-shots/README.md`: Explains single-hit audio samples, audio engineering standards (24-bit 48 kHz PCM WAV, zero-crossing microfades, `-0.5 dBFS` headroom), and directory taxonomy.
   - `loops/README.md`: Explains seamless loops, exact bar lengths (1, 2, 4, 8 bars), and tempo/key naming conventions.
   - `demo-projects/README.md`: Explains playable song projects and starter templates (`.nebproj`, `.nebz`), relative asset references, and packaging.

2. **Licensing Contract & Asset Ledger (`CONTENT_LICENSES.md`):**
   - Stated the non-negotiable rule at the very top: **EVERYTHING IS CC0-1.0 (PUBLIC DOMAIN)**.
   - Formulated the Contributor & Auditor Contract: all original works are dedicated under CC0-1.0; third-party works must have documented, verified CC0 provenance.
   - Built the **Asset Ledger** table logging each asset's path, display name, kind, creator, source, license, date audited, and auditor name.

3. **Format Specifications (`FORMAT.md`):**
   - Documented the exact JSON schemas matching the main Nebula DAW app:
     - `.nebpatch` (v1 modular synth patch): Envelope, category, polyphonic voices (1..8), nodes with device IDs and parameter maps, cable connections (`from`, `to`, `slot`), and output node ID.
     - `.nebpreset` (v1 device knob snapshot).
     - `.nebkit` (v1 drum kit manifest for Drum Rack): Envelope, metadata, pad mapping array (`note`, `name`, `sample`, `gain`, `tune_cents`, `release_ms`, `choke_group`).
     - `.nebproj` (v1 song project format).
     - Standard 48 kHz / 24-bit WAV PCM audio requirements.
     - Machine-readable index format (`index.json`).

4. **Sample Placeholder Items:**
   - `presets/sample_analog_lead.nebpatch`: Valid modular synth lead patch with saw VCO, 24dB VCF, and dual ADSRs, tagged with `_placeholder_notice` and `[SAMPLE]`.
   - `presets/sample_sub_bass.nebpatch`: Valid modular sub bass patch with 1 voice, pitched down VCO, and punchy filter envelope.
   - `kits/sample_space_kit.nebkit`: Valid drum kit manifest mapping pads 36 (Kick), 38 (Snare), 42 (Closed Hat), and 46 (Open Hat) with choke group 1.
   - `demo-projects/sample_starter_template.nebproj`: Minimal valid project model with Lead and Drum tracks.

5. **Automated Tooling & Machine-Readable Index:**
   - `tools/build_index.py`: Python CLI tool (stdlib only) with SPDX header and ELI5 docs. Scans categories, validates JSON, extracts metadata and tags, verifies all files against `CONTENT_LICENSES.md`, sorts keys deterministically, and writes `index.json`. Includes `--check` mode for CI.
   - `index.json`: Generated catalog mapping `category -> item_key -> {name, license, tags, files}`.

6. **Documentation & Process:**
   - Root `README.md`: Full guide covering naming, licensing, `index.json` synchronization, and contribution checklist.
   - `AGENTS.md`: Operating guidelines for AI agents and human contributors (SPDX headers, ELI5 docs, CC0-1.0 mandate, commit and push rules).
   - `LICENSE`: Full CC0 1.0 Universal text.
   - `.gitignore`: Ignoring Python cache, OS metadata, and editor artifacts.
   - `.github/workflows/ci.yml`: GitHub Actions workflow executing `python tools/build_index.py --check`.

### Verification Performed
- Ran `python tools/build_index.py` -> Successfully generated `index.json` indexing all 4 seeded placeholder items.
- Ran `python tools/build_index.py --check` -> Exited with code `0` (`OK: index.json is up to date and all assets are audited in CONTENT_LICENSES.md`).
- Tested failure modes in `build_index.py` (simulated missing ledger entry and stale index -> properly flagged errors with exit code 1).

### Scope Note
Parallel work in `Nebula Sound System` (app), `Nebula-Sound-System-API` (API), and SDKs was completely untouched during this session. All modifications were confined to `Nebula-Sound-System-Content-Library`.

---

## 2b. Session — 2026-10-08: First real content — the full-spread CC0 one-shot bundle

### What Was Done
1. **46 one-shot WAVs generated in Nebula's own code** (`one-shots/`), all **48 kHz / mono / 24-bit** as the `one-shots/README.md` spec requires:
   - `drums/` — kicks, snares, claps, hats (closed/open), toms (low/mid/high/deep floor), cymbals (ride, crash, crotale, triangle), and 19 percussion voices (rim, cowbell, bongos ×3, congas ×4, shaker, tambourine, claves, woodblock, snap, stick, maracas, cabasa, agogo ×2, guiro).
   - `bass/` — an 808 sub hit and a saw-stab.
   - `synths/` — a pluck, an FM bell, and a UI blip.
   - `foley/` — a bubble pop, a pen click, an air whoosh, and a water-drip.
   - `fx/` — a riser, a cinematic boom, a laser zap, and a glitch stutter.
2. **Every voice is CC0 by construction** — Nebula's own synthesis code (sine waves + shaped noise, deterministic Lcg, never `std::mt19937`), the same recipes the on-board drum kit ships, re-rendered at the library's sample rate and bit depth with zero-crossing micro-fades, DC removal and `-0.5 dBFS` headroom.
3. **46 Asset Ledger rows** appended to `CONTENT_LICENSES.md` (Creator: Nebula Content Team; Source: In-house (Synthesized); CC0-1.0) — one per file, matching the exact repo-relative path.
4. **`index.json` rebuilt** by `tools/build_index.py`, and `tools/build_index.py --check` confirms zero discrepancies.

### Why It Matters
The `one-shots/` folder was an empty scaffold (a README only); this replaces the sample placeholders' territory with real, usable, legally-clean factory one-shots. It is the first genuine content drop and completes the recording that "the CC0 one-shot bundle needs decided assets" — the assets are Nebula's own generated ones, so no third-party attribution is required.

### How It Was Verified
- `tools/build_index.py --check` exits 0 ("all assets are audited in CONTENT_LICENSES.md").
- Every file opens as a valid WAV, **48000 Hz, mono, 24-bit** (sample-width 3), non-trivial (> 8 KB).
- **Determinism:** two independent renders of the bundle are **byte-identical across all 46 files** (fixed Lcg seeds), so the assets are reproducible from Nebula's code with no drift.

### Scope Note
Only `one-shots/`, `CONTENT_LICENSES.md` and `index.json` were touched. The main `Nebula Sound System` app and `Nebula-Sound-System-API` are unchanged by this drop.

---

## 3. Next Steps (Phase 9 Factory Content Drop)

1. **Synthesize Real Factory Patches (`presets/`):**
   - Modular Synth patches: Basses (acid, sub, 808), Leads (saw, square, sync), Pads (ambient, strings), Keys, and Bells.
   - FM patches: 4-operator FM electric pianos, bells, organs, and basses.
   - Device presets: Curated presets for Delay, Reverb, EQ, Compressor, and Chorus.
2. **Drum Kits (`kits/` & `one-shots/`):**
   - Synthesize or source verified CC0 acoustic and electronic drum hits.
   - Build 8 to 16 factory `.nebkit` kits (808-style, 909-style, acoustic studio kit, lo-fi kit, percussion kit).
3. **Audio Loops (`loops/`):**
   - Craft seamless tempo-synced CC0 drum grooves, percussion loops, and basslines across 90, 110, 120, 124, 128, and 140 BPM.
4. **Demo Songs (`demo-projects/`):**
   - Compose 2–3 full demo projects in popular styles (e.g. Synthwave, Ambient, Hip-Hop) using exclusively factory content.
