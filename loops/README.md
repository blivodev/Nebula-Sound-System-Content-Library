<!-- SPDX-License-Identifier: CC0-1.0 -->
# Loops (`loops/`)

## ELI5: What belongs here?

A **loop** is a recorded musical phrase or rhythmic groove edited to repeat seamlessly over and over without any awkward stutter or click. When you drop a loop onto an audio track in Nebula's Clip Launcher or Timeline, it plays continuously in sync with the song's tempo.

This folder contains factory loops: drum grooves, percussion rhythms, basslines, synth arpeggios, chord progressions, and ambient textures.

---

## Directory Organization

Organize loops by musical role:

```text
loops/
├── drums/           # Full drum grooves, stripped beat stems (top loops, kick/snare stems)
├── percussion/      # Shaker loops, bongo grooves, tambourine rhythms
├── bass/            # Funky basslines, driving synth arpeggios, sub grooves
├── synth/           # Synth arpeggios, pluck patterns, lead phrases
├── keys/            # Electric piano comping, organ grooves, piano chords
└── textures/        # Evolving ambient backgrounds, vinyl noise, drone pads
```

---

## Loop Audio Standards

Every loop file must adhere to these technical standards:

- **Format:** Uncompressed Linear PCM WAV (`.wav`).
- **Sample Rate:** `48,000 Hz` (48 kHz).
- **Bit Depth:** `24-bit` (preferred) or `16-bit`.
- **Exact Bar Lengths:** Loops must be cut to precise musical durations: exactly 1, 2, 4, 8, or 16 bars at their native tempo. No trailing tail or cut-off beats.
- **Seamless Loop Points:** The audio waveform at the loop's end must match smoothly with the waveform at the start. Use zero-crossing cuts or subtle crossfades to prevent clicks when the playhead loops back to beat 1.
- **Normalization:** Normalized with headroom between `-1.0 dBFS` and `-0.5 dBFS`.

---

## Naming Conventions

Loop filenames must inform the producer of the **tempo (BPM)**, **musical key** (for tonal sounds), **instrument role**, and **bar length**:

```text
[bpm]bpm_[key]_[role]_[descriptor]_[bars]bar.wav
```

Examples:
- `124bpm_amin_bass_deep_pulse_4bar.wav`
- `120bpm_drums_punchy_breakbeat_2bar.wav`
- `095bpm_percussion_shaker_groove_1bar.wav`
- `128bpm_fmaj_synth_arpeggio_8bar.wav`
- `110bpm_texture_rainy_vinyl_drone_4bar.wav`

---

## Rules & Licensing

- **Strict CC0-1.0:** Every loop must be 100% public domain. Loops derived from copyrighted commercial records or uncleared samples are **strictly forbidden**.
- **Log every loop:** Add an entry for every file in [`../CONTENT_LICENSES.md`](../CONTENT_LICENSES.md).
- **Update index:** Run `python tools/build_index.py` after adding new loops.
