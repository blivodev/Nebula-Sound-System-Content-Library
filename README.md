<!-- SPDX-License-Identifier: CC0-1.0 -->
# Nebula Sound System — Content Library

Factory presets, drum kits, one-shots, loops, and demo projects for [Nebula Sound System](https://github.com/blivodev/Nebula-Sound-System).

---

## ELI5: What is this repository?

Imagine buying a brand new electronic synthesizer or keyboard. When you turn it on, it already has buttons for grand piano, synth leads, funky basslines, and punchy drum kits ready to play.

This repository is that factory sound vault for Nebula Sound System. When users download Nebula, this library supplies the sounds, instruments, and demo songs they play with on day one.

**Current Status:** Skeleton seeded for Phase 9. Contains sample placeholder items to validate file schemas and automated indexing tooling. Production factory sound packs will drop here during Phase 9.

---

## Repository Structure

The library is organized into five top-level content directories, plus documentation and maintenance tooling:

```text
Nebula-Sound-System-Content-Library/
├── presets/             # Synth & effect patches (.nebpatch, .nebpreset)
├── kits/                # Drum kit manifests for Drum Rack (.nebkit)
├── one-shots/           # Single-hit samples (drums, bass stabs, foley, SFX)
├── loops/               # Tempo-synced audio loops (rhythms, grooves, arps)
├── demo-projects/       # Playable song projects and starter templates (.nebproj)
├── tools/               # Maintenance scripts (build_index.py)
├── CONTENT_LICENSES.md  # Licensing contract & per-asset audit ledger (CC0-1.0)
├── FORMAT.md            # Detailed schema definitions for all file formats
├── index.json           # Machine-readable catalog for DAW browser and CI
├── AGENTS.md            # Workflow rules for AI agents and contributors
└── HANDOFF.md           # Continuous development handoff log
```

---

## How Items Are Named

Consistency is essential so that sounds can be searched instantly by category, tempo, key, and character.

| Content Kind | Filename Pattern | Example |
|:---|:---|:---|
| **Presets** | `[role]_[descriptor].nebpatch` | `bass_acid_resonant.nebpatch` |
| **Device Presets** | `[device]_[descriptor].nebpreset` | `delay_slapback_vocal.nebpreset` |
| **Kits** | `[genre]_[descriptor].nebkit` | `electro_space_analog.nebkit` |
| **One-Shots** | `[category]_[subkind]_[key]_[descriptor].wav` | `kick_electronic_sub_f1.wav` |
| **Loops** | `[bpm]bpm_[key]_[role]_[descriptor]_[bars]bar.wav` | `124bpm_cmin_bass_acid_groove_4bar.wav` |
| **Demo Projects**| `[genre]_[title]_[bpm]bpm.nebproj` | `synthwave_starlight_124bpm.nebproj` |

> [!NOTE]  
> **Sample & Placeholder Items:**  
> Any test or placeholder file committed for scaffolding purposes must include the `sample_` prefix in the filename and `[SAMPLE]` in its metadata title so nobody mistakes it for final factory content.

---

## Licensing: Strict CC0-1.0

Nebula Sound System enforces an absolute licensing standard:

- **Everything is CC0-1.0 (Public Domain):** Every asset in this repository is dedicated to the public domain.
- **Zero Restrictions for Music Makers:** Music makers can use any sound in commercial tracks, video games, streams, or films without royalties, fees, or required attribution.
- **Third-Party CC0 Provenance:** Any imported sound must have documented, verified CC0 provenance.
- **Mandatory Ledger Record:** Every single file is cataloged in [`CONTENT_LICENSES.md`](CONTENT_LICENSES.md) with origin, author, and audit date.

Read the full licensing contract and view the asset ledger in [`CONTENT_LICENSES.md`](CONTENT_LICENSES.md).

---

## Machine-Readable Catalog: `index.json`

The file [`index.json`](index.json) provides a fast, structured lookup table for Nebula's in-app browser, search engine, and CI pipelines.

It maps:
$$\text{category} \longrightarrow \text{item key} \longrightarrow \{\text{name}, \text{license}, \text{tags}, \text{files}\}$$

Example:
```json
{
  "presets": {
    "sample_analog_lead": {
      "files": ["presets/sample_analog_lead.nebpatch"],
      "license": "CC0-1.0",
      "name": "[SAMPLE] Analog Lead (Placeholder)",
      "tags": ["analog", "lead", "placeholder", "preset", "sample", "synth"]
    }
  }
}
```

---

## Keeping `index.json` in Sync: `tools/build_index.py`

A Python script in `tools/build_index.py` automates indexing and ensures the repository never gets out of sync:

### 1. Rebuilding the Index
Whenever you add, modify, or rename an asset:
```bash
python tools/build_index.py
```
This scans all content folders, extracts metadata, formats tags, sorts keys deterministically, and writes `index.json`.

### 2. Validating in CI
To verify that `index.json` matches the disk content and that all assets are documented in `CONTENT_LICENSES.md`:
```bash
python tools/build_index.py --check
```
- If all assets are logged and `index.json` is clean: exits with status `0` (`OK`).
- If an unlogged asset or stale index is found: exits with status `1` (`ERROR`).

---

## How to Contribute (Checklist)

Before opening a pull request with new content:

1. [ ] Confirm sound is 100% CC0 (public domain) and self-created or properly verified.
2. [ ] Save in standard format: 24-bit 48 kHz PCM WAV for audio; JSON for presets/kits/projects (see [`FORMAT.md`](FORMAT.md)).
3. [ ] Follow naming conventions.
4. [ ] Add a new row to the Asset Ledger in [`CONTENT_LICENSES.md`](CONTENT_LICENSES.md).
5. [ ] Run `python tools/build_index.py` to regenerate `index.json`.
6. [ ] Run `python tools/build_index.py --check` and verify it reports `OK`.
7. [ ] Update [`HANDOFF.md`](HANDOFF.md) with details of your contribution.
