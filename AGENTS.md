<!-- SPDX-License-Identifier: CC0-1.0 -->
# Instructions for AI Agents and Contributors

ELI5: Rules and standard operating procedures for any AI agent or human contributor working in the **Nebula Sound System Content Library** repository.

---

## 1. Non-Negotiable Core Rules

1. **Licensing Contract:**  
   **Everything in this repository is CC0-1.0 (Public Domain).**  
   Never commit material licensed under GPL, LGPL, CC-BY, proprietary, or attribution-encumbered licenses. Third-party assets must have unambiguous proof of CC0 dedication and must be individually recorded in [`CONTENT_LICENSES.md`](CONTENT_LICENSES.md) before merging.

2. **Always Update `CONTENT_LICENSES.md` & `index.json`:**  
   Whenever an asset is added, moved, or deleted, you must:
   - Update the ledger in [`CONTENT_LICENSES.md`](CONTENT_LICENSES.md).
   - Run `python tools/build_index.py` to update [`index.json`](index.json).
   - Run `python tools/build_index.py --check` to prove zero discrepancies.

3. **SPDX Headers & ELI5 Documentation:**  
   - Every script, schema, and document must start with an SPDX identifier (`# SPDX-License-Identifier: CC0-1.0` or `<!-- SPDX-License-Identifier: CC0-1.0 -->`).
   - Every file must have an ELI5 (Explain Like I'm 5) plain-English summary explaining what it does and why it exists.

4. **Commit & Push to GitHub Only:**  
   Commit every change with a descriptive commit message and push to `origin/main` on GitHub (`https://github.com/blivodev/Nebula-Sound-System-Content-Library.git`).

5. **Scope Discipline:**  
   Do not touch parallel repositories (`Nebula Sound System`, `Nebula-Sound-System-API`, SDKs) when working on Content Library tasks.

6. **Continuous Handoff (`HANDOFF.md`):**  
   Every session must update [`HANDOFF.md`](HANDOFF.md) detailing what was changed, design rationale, verification results, and pending tasks.

---

## 2. Audio & File Formats

- **Audio:** 24-bit 48 kHz uncompressed PCM WAV (`.wav`). Peak normalized with `-0.5 dBFS` headroom. Clean zero-crossing fades (minimum 2 ms).
- **Presets & Patches:** JSON documents matching `.nebpatch` or `.nebpreset` specifications in [`FORMAT.md`](FORMAT.md).
- **Kits:** JSON manifests matching `.nebkit` specification in [`FORMAT.md`](FORMAT.md).
- **Projects:** JSON documents matching `.nebproj` specification in [`FORMAT.md`](FORMAT.md).
- **Lightweight Skeletons:** Do not invent large binary blobs during architectural / scaffolding phases. Keep placeholders clearly labeled with `sample_` and `[SAMPLE]`.
