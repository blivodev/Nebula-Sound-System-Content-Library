<!-- SPDX-License-Identifier: CC0-1.0 -->
# File Formats in the Nebula Content Library

ELI5: Every patch, preset, kit, and project file in Nebula is human-readable JSON text that you can open in any text editor. Audio files are standard lossless WAV files. This document describes the schema of every file type found in the Content Library.

---

## 1. General Rules for All Nebula JSON Formats

1. **Self-Describing Envelope:** Every JSON document begins with `"format": "<type>"` and `"format_version": <integer>`.
2. **Deterministic & Sorted Keys:** Keys are written in deterministic (alphabetical) order for clean, legible git diffs.
3. **Key-Based Parameters:** Device knob parameters are keyed by stable string names (e.g. `"cutoff_hz"`), never numeric indices, ensuring forward and backward compatibility.
4. **Resilient Loading:** Unknown fields are ignored or preserved rather than failing the parser. Missing optional knobs fall back to device defaults.
5. **No Proprietary Codecs:** Sound content is stored in open, uncompressed PCM audio files.

---

## 2. Synth & Effect Patches: `.nebpatch` (v1)

A `.nebpatch` file defines a modular instrument or effect chain: which DSP modules exist, how their knobs are set, and which virtual patch cables connect them together.

### Schema Specification

```json
{
  "category": "synth",
  "connections": [
    {
      "from": 0,
      "slot": 0,
      "to": 2
    },
    {
      "from": 1,
      "slot": 0,
      "to": 3
    }
  ],
  "format": "nebula-patch",
  "format_version": 1,
  "name": "Modular Lead",
  "nodes": [
    {
      "device": "nebula.mod.keyboard",
      "id": 0,
      "label": "Pitch",
      "parameters": {
        "output": 0.0
      }
    },
    {
      "device": "nebula.mod.vco",
      "id": 2,
      "label": "Oscillator",
      "parameters": {
        "level": 0.6,
        "waveform": 2.0
      }
    }
  ],
  "output": 2,
  "voices": 8
}
```

### Fields

| Field | Type | Description |
|:---|:---|:---|
| `format` | string | Must be `"nebula-patch"`. |
| `format_version` | integer | Currently `1`. |
| `name` | string | Display name of the patch in the Nebula browser. |
| `category` | string | One of: `"synth"`, `"bass"`, `"pad"`, `"lead"`, `"drums"`, `"fm"`, `"sampler"`. Sets the browser icon and layout. |
| `voices` | integer | (Optional) Maximum polyphonic voice replication count (1 to 8, default `8`). A monophonic patch or drum kit specifies `1`. |
| `nodes` | array | List of module nodes in the patch. Each node has an integer `id`, a device identifier `device` (e.g. `nebula.mod.vco`), an optional descriptive `label`, and a `parameters` object mapping knob keys to numeric values. |
| `connections` | array | List of virtual patch cables. Each connection defines `from` (source node ID), `to` (destination node ID), and `slot` (destination input slot index, e.g. slot 0 = audio in, slot 1 = CV in). |
| `output` | integer | Node ID whose audio stream feeds the instrument's final output. |

---

## 3. Device Presets: `.nebpreset` (v1)

A `.nebpreset` represents a single device's knob positions saved under a friendly name (for example, a "Slapback" setting for the Delay effect).

### Schema Specification

```json
{
  "author": "Nebula Sound System",
  "device": "nebula.delay",
  "device_version": 1,
  "format": "nebula-preset",
  "format_version": 1,
  "name": "Slapback Echo",
  "parameters": {
    "feedback": 0.15,
    "mix": 0.25,
    "time_ms": 90.0
  },
  "tags": ["delay", "echo", "slapback", "short"]
}
```

### Fields

| Field | Type | Description |
|:---|:---|:---|
| `format` | string | Must be `"nebula-preset"`. |
| `format_version` | integer | Currently `1`. |
| `device` | string | Stable device ID (e.g. `"nebula.delay"`, `"nebula.reverb"`, `"nebula.eq"`, `"nebula.compressor"`). |
| `device_version`| integer | Device parameter layout version (default `1`). |
| `name` | string | Preset title. |
| `author` | string | Creator name or sound designer. |
| `tags` | array | String tags for search and filtering. |
| `parameters` | object | Map of knob parameter names to their target values. Knobs not listed revert to their factory default values. |

---

## 4. Drum Kits & Sample Sets: `.nebkit` (v1)

A `.nebkit` is a manifest file defining a playable drum kit or multi-pad instrument for Nebula's Drum Rack. It maps MIDI note numbers (standard General MIDI drum octave: 36 through 51) to relative sample audio paths, with individual pad tuning, gain, envelope release times, and choke grouping.

### Schema Specification

```json
{
  "author": "Nebula Content Team",
  "description": "Analog drum kit crafted with modular oscillators and noise sources.",
  "format": "nebula-kit",
  "format_version": 1,
  "license": "CC0-1.0",
  "name": "Space Analog Kit",
  "pads": [
    {
      "choke_group": 0,
      "gain": 1.0,
      "name": "Kick",
      "note": 36,
      "release_ms": 350.0,
      "sample": "one-shots/drums/kick_analog_punch.wav",
      "tune_cents": 0.0
    },
    {
      "choke_group": 0,
      "gain": 0.9,
      "name": "Snare",
      "note": 38,
      "release_ms": 220.0,
      "sample": "one-shots/drums/snare_noise_crack.wav",
      "tune_cents": 0.0
    },
    {
      "choke_group": 1,
      "gain": 0.75,
      "name": "Closed Hat",
      "note": 42,
      "release_ms": 75.0,
      "sample": "one-shots/drums/hat_closed_metallic.wav",
      "tune_cents": 0.0
    },
    {
      "choke_group": 1,
      "gain": 0.8,
      "name": "Open Hat",
      "note": 46,
      "release_ms": 400.0,
      "sample": "one-shots/drums/hat_open_sizzle.wav",
      "tune_cents": 0.0
    }
  ],
  "tags": ["drums", "electronic", "analog", "kit"]
}
```

### Fields

| Field | Type | Description |
|:---|:---|:---|
| `format` | string | Must be `"nebula-kit"`. |
| `format_version` | integer | Currently `1`. |
| `name` | string | Display name of the kit. |
| `author` | string | Creator of the kit. |
| `license` | string | Mandatory `"CC0-1.0"`. |
| `tags` | array | Search tags (e.g. `["drums", "analog", "hiphop"]`). |
| `pads` | array | List of pad definitions (see below). |

#### Pad Definition Object

| Field | Type | Description |
|:---|:---|:---|
| `note` | integer | MIDI trigger note (36 = Kick / C1, 38 = Snare / D1, etc.). Range 0–127, typically 36–51. |
| `name` | string | Pad label shown in the 4×4 Pad Grid. |
| `sample` | string | Relative path to the audio file from the repository root (e.g. `one-shots/...`). |
| `gain` | float | Playback volume scaling factor (0.0 to 2.0, default 1.0). |
| `tune_cents` | float | Pitch offset in cents (-2400.0 to +2400.0, default 0.0). |
| `release_ms` | float | Envelope release time in milliseconds after trigger. |
| `choke_group` | integer | Choke group ID (0 = none; pads sharing the same non-zero group ID cut each other off, e.g. open/closed hi-hats on group 1). |

---

## 5. Song Projects & Templates: `.nebproj` (v1)

A `.nebproj` file represents an entire song arrangement or starter project template, including tracks, MIDI clips, notes, effects, and routing.

### Top-Level Structure

```json
{
  "format": "nebula-project",
  "format_version": 1,
  "id": "c56a4180-65aa-42ec-a945-5fd21dec0538",
  "name": "Demo Song",
  "tempo_bpm": 124.0,
  "tracks": [
    {
      "clips": [],
      "devices": [],
      "id": "e3057e93-13e2-45e0-b6a1-9a70f4b301a2",
      "instrument_patch": "Modular Lead",
      "kind": "midi",
      "name": "Synth Lead",
      "volume": 0.85
    }
  ]
}
```

---

## 6. Audio Files (One-Shots & Loops)

All audio assets committed to `one-shots/` and `loops/` must satisfy these audio engineering standards:

- **Format:** Uncompressed Linear PCM WAV (`.wav`).
- **Sample Rate:** `48,000 Hz` (48 kHz) native.
- **Bit Depth:** `24-bit` (or 16-bit where appropriate, 24-bit preferred for high dynamic range).
- **Channels:** Mono for localized drum hits and bass one-shots; Stereo for pads, spatial effects, and stereo loops.
- **Normalization:** Peak levels normalized with safety headroom to prevent clipping (between `-1.0 dBFS` and `-0.3 dBFS`).
- **Clean Edits:** Zero-crossings at start and end; fades applied (minimum 2 ms) to prevent clicks or pops on note onset/cutoff.

---

## 7. Machine-Readable Catalog: `index.json`

The Content Library catalog `index.json` provides an instant index for the Nebula browser, search subsystem, and CI checks.

### Shape

```json
{
  "<category>": {
    "<item_key>": {
      "files": ["presets/sample_analog_lead.nebpatch"],
      "license": "CC0-1.0",
      "name": "[SAMPLE] Analog Lead (Placeholder)",
      "tags": ["sample", "placeholder", "synth", "lead"]
    }
  }
}
```

Where `<category>` is one of:
- `presets`
- `kits`
- `one-shots`
- `loops`
- `demo-projects`
