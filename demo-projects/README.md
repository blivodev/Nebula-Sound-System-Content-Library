<!-- SPDX-License-Identifier: CC0-1.0 -->
# Demo Projects (`demo-projects/`)

## ELI5: What belongs here?

A **demo project** is a complete, ready-to-play song or starter template made entirely in Nebula. It showcases the DAW's sound quality, arrangement tools, and mixing capabilities.

When new users install Nebula Sound System, opening a demo project lets them:
1. Hear what the DAW is capable of on day one.
2. Inspect how tracks, instruments, effects, clips, and automation are arranged.
3. Use starter templates as creative launchpads for their own original music.

---

## Supported File Formats

- **Nebula Project (`.nebproj`):**  
  Human-readable JSON project file holding track lists, clip launcher scenes, timeline notes, instrument choices, and effect chains.
- **Nebula Project Bundle (`.nebz`):**  
  *(Planned for Phase 3/9)* Self-contained zip archive containing a `.nebproj` plus any associated custom audio recordings and preset dependencies bundled together.

See [`../FORMAT.md`](../FORMAT.md) for detailed schema specifications.

---

## Types of Projects

```text
demo-projects/
├── templates/       # Blank starter templates (e.g. "Electronic Starter", "Band Recording", "Podcast Setup")
├── genre-demos/     # Finished showcase songs (Synthwave, Hip Hop, Ambient, Lo-Fi, Orchestral)
└── tutorials/       # Educational projects accompanying documentation and tutorial chapters
```

---

## Asset Dependency & Packaging Rules

1. **Relative Paths Only:**  
   Any sample, one-shot, or loop referenced by a track's Sampler or Drum Rack must use relative paths within the Content Library (e.g. `one-shots/drums/kick_analog.wav`), never absolute local paths like `C:\Users\...`.
2. **Zero Encumbrance:**  
   Every synth preset, drum hit, loop, and clip within the project must use content from this repository or be dedicated under CC0.
3. **Optimized Load Time:**  
   Keep demo project file sizes lean and avoid excessive track counts or unrendered heavy stems.

---

## Naming Conventions

- Directory or project filename: `genre_title_bpm.nebproj` (e.g. `synthwave_starlight_120bpm.nebproj`).
- Template filename: `template_[name].nebproj` (e.g. `template_four_on_the_floor.nebproj`).
- Sample placeholder items: Filenames must be prefixed with `sample_` and project titles must start with `[SAMPLE]` to clearly signify scaffolding material.

---

## Rules & Licensing

- **Strict CC0-1.0:** The entire musical arrangement, MIDI data, project structure, and audio assets must be dedicated to CC0.
- **Log every project:** Record the project and any newly included assets in [`../CONTENT_LICENSES.md`](../CONTENT_LICENSES.md).
- **Update index:** Run `python tools/build_index.py` after adding demo projects.
