<!-- SPDX-License-Identifier: CC0-1.0 -->
# Kits (`kits/`)

## ELI5: What belongs here?

A **kit** is an organized collection of drum and percussion sounds mapped onto finger-drumming pads. When you tap a pad or press a MIDI key, the kit plays the corresponding sound (such as a punchy kick on pad 1 or a crisp snare on pad 2).

This folder contains drum kit manifest files (`.nebkit`) that configure Nebula's Drum Rack.

---

## Supported File Format: `.nebkit`

Each kit is defined in a lightweight, human-readable `.nebkit` JSON file. A kit specifies:
- Display metadata (name, author, description, tags).
- A list of pad mappings linking MIDI note numbers (36 through 51) to relative audio file paths in `one-shots/`.
- Per-pad parameters: volume `gain`, pitch `tune_cents`, envelope `release_ms`, and `choke_group` routing.

See [`../FORMAT.md`](../FORMAT.md) for the formal `.nebkit` JSON specification.

---

## Standard Pad Layout (General MIDI 4×4 Grid)

Nebula's Drum Rack uses a 4×4 pad grid corresponding to standard General MIDI drum keys:

```text
Row 4 (Pads 13–16): [48] High Tom      [49] Crash Cymbal   [50] High Tom 2     [51] Ride Cymbal
Row 3 (Pads 9–12):  [44] Pedal Hat     [45] Low Mid Tom    [46] Open Hi-Hat    [47] High Mid Tom
Row 2 (Pads 5–8):   [40] Snare Rim     [41] Low Floor Tom  [42] Closed Hi-Hat  [43] High Floor Tom
Row 1 (Pads 1–4):   [36] Bass Drum     [37] Side Stick     [38] Acoustic Snare [39] Hand Clap
```

*(Pads may be customized for specific kits, but starting with the standard GM layout ensures immediate playability with hardware pad controllers.)*

---

## Choke Groups

Choke groups allow one pad to mute another pad immediately when triggered:
- **Group 1 (Hi-Hats):** Playing an Open Hi-Hat (note 46) and then triggering a Closed Hi-Hat (note 42) will immediately stop the open hat from ringing, mimicking the physics of an acoustic hi-hat cymbal.

---

## Rules & Licensing

- **Audio references:** Samples referenced in kit manifests must point to CC0 audio files residing in [`../one-shots/`](../one-shots/).
- **Strict CC0-1.0:** The kit manifest and all referenced audio samples must be dedicated to CC0.
- **Log every asset:** Add kit manifests to [`../CONTENT_LICENSES.md`](../CONTENT_LICENSES.md).
- **Keep index updated:** Run `python tools/build_index.py` after creating or editing kits.
