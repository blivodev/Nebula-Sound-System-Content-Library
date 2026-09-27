<!-- SPDX-License-Identifier: CC0-1.0 -->
# One-Shots (`one-shots/`)

## ELI5: What belongs here?

A **one-shot** is a single, non-looping audio recording that plays once from start to finish when triggered. Examples include a single punchy kick drum hit, a crisp snare crack, a handclap, a metallic percussion strike, a short bass stab, a synthesizer blip, or a foley sound effect.

One-shots serve two main roles in Nebula:
1. They are loaded into **Drum Rack** pads via `.nebkit` files.
2. They are loaded into the **Sampler** instrument to be pitched across the keyboard or triggered directly in audio tracks.

---

## Directory Organization

To keep thousands of individual sample files searchable and intuitive, organize them by instrument family and role:

```text
one-shots/
├── drums/
│   ├── kicks/           # Electronic sub kicks, acoustic bass drums, transient thumps
│   ├── snares/          # Snare drums, acoustic cracks, rimshots, layered claps
│   ├── claps/           # Solo claps, group handclaps, snaps
│   ├── hats/            # Closed, open, half-open, pedal hi-hats
│   ├── toms/            # High, mid, low acoustic and electronic toms
│   ├── cymbals/         # Crashes, rides, splashes, chinas
│   └── percussion/      # Bongos, congas, shakers, cowbells, woodblocks, rim clicks
├── bass/                # 808 hits, synth bass stabs, acoustic bass plucks
├── synths/              # Chords, stabs, bell chimes, tonal plucks
├── foley/               # Real-world acoustic textures, clicks, mechanical sounds
└── fx/                  # Laser zaps, impacts, downlifters, glitches, sub drops
```

---

## Audio Engineering Standards

Every audio file in `one-shots/` must meet these specifications:

- **Format:** Uncompressed Linear PCM WAV (`.wav`). No MP3, OGG, FLAC, or proprietary formats.
- **Sample Rate:** `48,000 Hz` (48 kHz) native.
- **Bit Depth:** `24-bit` (preferred) or `16-bit`.
- **Channel Configuration:** Mono for single drums, kicks, bass hits, and directional percussion; Stereo for spatial cymbals, stereo claps, and widening effects.
- **Zero-Crossing & Fades:** Files must start and end at exact zero-crossings, with a tiny micro-fade (1–2 ms) applied to head and tail to eliminate any transient pop or DC click.
- **No DC Offset:** Audio must be centered vertically on 0.0 amplitude.
- **Peak Headroom:** Normalized with at least `-0.5 dBFS` headroom to prevent inter-sample clipping when summed into a mix bus.

---

## Naming Conventions

Filenames should be descriptive, lowercase snake_case, and self-documenting:

```text
[category]_[subkind]_[tonal_key_if_applicable]_[descriptor].wav
```

Examples:
- `kick_analog_punchy_f1.wav`
- `snare_acoustic_crack_d1.wav`
- `hat_closed_bright_tick.wav`
- `bass_stab_cmin_acid.wav`
- `fx_laser_zap_high.wav`

---

## Rules & Licensing

- **Strict CC0-1.0:** Every audio sample must be 100% CC0 public domain.
- **Ledger Record:** Every audio file added must be logged in [`../CONTENT_LICENSES.md`](../CONTENT_LICENSES.md) with origin, author, and source link.
- **No Large Binary Blobs in Skeleton:** During development and repository initialization (Phase 9 skeleton), do not commit massive audio bundles; only light, sample-grade files are accepted until factory production drop.
