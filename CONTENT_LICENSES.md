<!-- SPDX-License-Identifier: CC0-1.0 -->
# CONTENT_LICENSES — Nebula Sound System Content Library

> **THE GOLDEN RULE: EVERYTHING IN THIS REPOSITORY IS CC0 (PUBLIC DOMAIN).**  
> Every sound, preset, patch, kit, loop, one-shot, and demo project distributed in this library is dedicated to the public domain under the [Creative Commons Zero 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) (CC0-1.0) dedication.  
> **Third-party assets must be CC0, with proof of public domain dedication recorded per asset in the ledger below before inclusion.** No assets under CC-BY, GPL, LGPL, proprietary, or attribution-encumbered licenses are accepted.

---

## ELI5: What does this mean for music makers?

If you are a music maker, sound designer, game developer, or content creator using Nebula Sound System:
- **You own your music.** Anything you make using presets, drums, samples, loops, or projects from this library is 100% yours.
- **Commercial use is freely allowed.** You can sell your tracks, stream them on Spotify, put them in video games, commercials, or films without paying royalties or asking for permission.
- **No attribution required.** You do not have to credit Nebula or the sound designers in your liner notes (though a shout-out is always appreciated!).
- **Zero legal risk.** Because everything is strictly CC0, there are no copyright traps, hidden royalties, or license revocations.

---

## The Contributor & Auditor Contract

To keep this library pure and legally bulletproof, every contributor, sound designer, and automated agent must adhere to these four invariants:

1. **Original Works Dedication:**  
   Any original patch, preset, recording, synthesized drum, or demo created specifically for Nebula Sound System is contributed directly under CC0-1.0. By committing content to this repository, you irrevocably waive all copyright and neighboring rights worldwide.

2. **Strict Third-Party CC0 Verification:**  
   If an asset originates outside the Nebula team (e.g., public domain field recordings or open sound archives), it must have an explicit, unambiguous CC0 or public domain dedication from the creator. Sourcing from "royalty free" sites that require attribution or forbid resale of sound libraries is **strictly prohibited**.

3. **Per-Asset Ledger Entry:**  
   No asset may enter this repository without an entry in the **Asset Ledger** below. Every entry must detail its file path, item name, creator, source URL, date verified, and auditor name.

4. **No Encumbered Formats:**  
   Do not commit proprietary binary blobs or patented audio codecs. All audio files must be standard uncompressed PCM WAV (24-bit, 48 kHz).

---

## Asset Ledger

All items present in the library are inventoried in the table below. Every pull request introducing new content must add corresponding rows to this ledger.

| Asset Path | Item Name | Category | Creator / Author | Upstream Source | License | Date Verified | Auditor / Agent | Status / Notes |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| `presets/sample_analog_lead.nebpatch` | `[SAMPLE] Analog Lead (Placeholder)` | Presets | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-09-27 | Nebula Seed Agent | Sample placeholder item for Phase 9 |
| `presets/sample_sub_bass.nebpatch` | `[SAMPLE] Sub Bass (Placeholder)` | Presets | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-09-27 | Nebula Seed Agent | Sample placeholder item for Phase 9 |
| `kits/sample_space_kit.nebkit` | `[SAMPLE] Space Analog Kit (Placeholder)` | Kits | Nebula Content Team | In-house (Manifest) | CC0-1.0 | 2026-09-27 | Nebula Seed Agent | Sample placeholder item for Phase 9 |
| `demo-projects/sample_starter_template.nebproj` | `[SAMPLE] Starter Template (Placeholder)` | Demo Projects | Nebula Content Team | In-house (Project model) | CC0-1.0 | 2026-09-27 | Nebula Seed Agent | Sample placeholder item for Phase 9 |

---

## How to Audit and Add a New Asset

When dropping new content into `presets/`, `kits/`, `one-shots/`, `loops/`, or `demo-projects/`:

1. Verify that the asset is 100% original synthesised sound or clearly licensed under CC0 at the upstream source.
2. Place the file into the appropriate directory following naming conventions (see [`README.md`](README.md)).
3. Add a line to the **Asset Ledger** table above.
4. Run `python tools/build_index.py` to regenerate `index.json`.
5. Run `python tools/build_index.py --check` to verify that all files match the ledger and index.
