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
| `one-shots/bass/bass_808_sub_a1.wav` | Bass 808 Sub A1 | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/bass/bass_saw_stab_a2.wav` | Bass Saw Stab A2 | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/drums/claps/clap_hand_group.wav` | Clap Hand Group | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/drums/cymbals/crash_bright_wash.wav` | Crash Bright Wash | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/drums/cymbals/crotale_glass_ping.wav` | Crotale Glass Ping | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/drums/cymbals/ride_shimmer_ring.wav` | Ride Shimmer Ring | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/drums/cymbals/triangle_muted_ping.wav` | Triangle Muted Ping | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/drums/hats/hat_closed_tick.wav` | Hat Closed Tick | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/drums/hats/hat_open_ring.wav` | Hat Open Ring | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/drums/kicks/kick_analog_sub_a1.wav` | Kick Analog Sub A1 | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/drums/percussion/agogo_hi_bell.wav` | Agogo Hi Bell | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/drums/percussion/agogo_lo_bell.wav` | Agogo Lo Bell | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/drums/percussion/bongo_hi_slap.wav` | Bongo Hi Slap | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/drums/percussion/bongo_lo_warm.wav` | Bongo Lo Warm | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/drums/percussion/bongo_mid_tone.wav` | Bongo Mid Tone | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/drums/percussion/cabasa_scratch_buzz.wav` | Cabasa Scratch Buzz | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/drums/percussion/claves_wood_tick.wav` | Claves Wood Tick | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/drums/percussion/conga_hi_slap.wav` | Conga Hi Slap | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/drums/percussion/conga_lo_open.wav` | Conga Lo Open | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/drums/percussion/conga_low_boom.wav` | Conga Low Boom | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/drums/percussion/conga_tumba_deep.wav` | Conga Tumba Deep | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/drums/percussion/cowbell_analog_ring.wav` | Cowbell Analog Ring | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/drums/percussion/guiro_rasp_scrape.wav` | Guiro Rasp Scrape | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/drums/percussion/maracas_shake_swell.wav` | Maracas Shake Swell | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/drums/percussion/rim_side_stick.wav` | Rim Side Stick | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/drums/percussion/shaker_grain_swish.wav` | Shaker Grain Swish | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/drums/percussion/snap_finger_crack.wav` | Snap Finger Crack | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/drums/percussion/stick_wood_click.wav` | Stick Wood Click | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/drums/percussion/tambourine_jingle_burst.wav` | Tambourine Jingle Burst | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/drums/percussion/woodblock_hollow_knock.wav` | Woodblock Hollow Knock | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/drums/snares/snare_acoustic_crack.wav` | Snare Acoustic Crack | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/drums/toms/tom_floor_deep.wav` | Tom Floor Deep | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/drums/toms/tom_high_rack.wav` | Tom High Rack | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/drums/toms/tom_low_floor.wav` | Tom Low Floor | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/drums/toms/tom_mid_rack.wav` | Tom Mid Rack | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/foley/foley_click_pen.wav` | Foley Click Pen | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/foley/foley_pop_bubble.wav` | Foley Pop Bubble | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/foley/foley_water_drip_plink.wav` | Foley Water Drip Plink | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/foley/foley_whoosh_air.wav` | Foley Whoosh Air | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/fx/fx_boom_cinematic.wav` | Fx Boom Cinematic | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/fx/fx_glitch_stutter.wav` | Fx Glitch Stutter | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/fx/fx_riser_build.wav` | Fx Riser Build | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/fx/fx_zap_laser.wav` | Fx Zap Laser | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/synths/synth_bell_fm.wav` | Synth Bell Fm | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/synths/synth_blip_ui.wav` | Synth Blip Ui | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
| `one-shots/synths/synth_pluck_bright.wav` | Synth Pluck Bright | One-Shots | Nebula Content Team | In-house (Synthesized) | CC0-1.0 | 2026-10-08 | Nebula Agent | Full-spread CC0 one-shot bundle (generated in Nebula's code)
