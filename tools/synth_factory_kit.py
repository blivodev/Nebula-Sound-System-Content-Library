# SPDX-License-Identifier: CC0-1.0
"""
synth_factory_kit.py

ELI5: makes the first REAL drum kit for the Nebula Content Library by
synthesizing four drum one-shots (kick, snare, closed hat, open hat) out of
nothing but math. It writes them as 24-bit, 48 kHz, mono PCM WAV files into
`one-shots/drums/...`. Each hit is an original recording created by this
script, so it is public-domain (CC0) by construction, deterministic on every
machine, and free to use in any song.

Why it exists:
  The in-app Content Library loader turns a `.nebkit` into a playable Drum
  Rack. This script gives that loader something real to play: a small
  factory-grade analog kit built to the repo's audio standards (48 kHz,
  24-bit mono, -0.5 dBFS headroom, ~2 ms zero-crossing fades). Run it, then
  author `kits/factory_analog.nebkit` to map the pads.

Usage:
  python tools/synth_factory_kit.py            # write the four one-shots (idempotent)
  python tools/synth_factory_kit.py --dry-run  # print what it would write, write nothing

No third-party packages are needed (standard library only).
"""

import argparse
import math
import os
import struct
import sys
import wave

SAMPLE_RATE = 48000
HEADROOM = 10.0 ** (-0.5 / 20.0)  # -0.5 dBFS: keep every peak at or below this
FADE_MS = 2.0                     # tiny head/tail fade to avoid pops


def _fade(samples):
    """Apply a ~2 ms fade-in and fade-out so the file starts and ends at zero (no click)."""
    n = max(1, int(SAMPLE_RATE * FADE_MS / 1000.0))
    out = list(samples)
    for i in range(n):
        t = i / n
        out[i] *= t
        out[-1 - i] *= t
    return out


def _env(i, sr, attack_s, decay_s):
    """An attack/decay envelope: ramps up over `attack_s`, then decays with time constant `decay_s`."""
    t = i / sr
    attack = min(1.0, t / attack_s) if attack_s > 0 else 1.0
    return attack * math.exp(-t / decay_s)


def _normalize(samples):
    """Scale so the peak sits exactly at -0.5 dBFS headroom."""
    peak = max((abs(s) for s in samples), default=0.0) or 1.0
    g = HEADROOM / peak
    return [s * g for s in samples]


def synth_kick():
    """A punchy analog sub-kick on E1: a sine whose pitch drops fast, plus a clicky transient."""
    n = int(0.45 * SAMPLE_RATE)
    out = []
    for i in range(n):
        t = i / SAMPLE_RATE
        freq = 150.0 * math.exp(-t / 0.06) + 41.0
        env = _env(i, SAMPLE_RATE, 0.001, 0.10)
        s = math.sin(2.0 * math.pi * freq * t)
        click = math.exp(-t / 0.004) * math.sin(2.0 * math.pi * 900.0 * t) * 0.4
        out.append((s + click * _env(i, SAMPLE_RATE, 0.0003, 0.004)) * env)
    return _normalize(_fade(out))


def synth_snare():
    """A cracky acoustic-style snare on D1: a short tonal body plus a noisy snap."""
    n = int(0.30 * SAMPLE_RATE)
    out = []
    seed = 0x9E3779B9
    for i in range(n):
        t = i / SAMPLE_RATE
        seed = (seed * 1103515245 + 12345) & 0x7FFFFFFF
        noise = ((seed & 0xFFFF) / 32768.0) - 1.0
        body = math.sin(2.0 * math.pi * 180.0 * t) * _env(i, SAMPLE_RATE, 0.0003, 0.05) * 0.6
        snap = noise * _env(i, SAMPLE_RATE, 0.0003, 0.02)
        ring = noise * _env(i, SAMPLE_RATE, 0.002, 0.09) * 0.3
        out.append((body + snap + ring) * _env(i, SAMPLE_RATE, 0.0004, 0.08))
    return _normalize(_fade(out))


def synth_closed_hat():
    """A bright, tight closed hat: a very short metallic noise burst (~90 ms)."""
    n = int(0.09 * SAMPLE_RATE)
    out = []
    seed = 0xC0FFEE
    for i in range(n):
        t = i / SAMPLE_RATE
        seed = (seed * 22695477 + 1) & 0x7FFFFFFF
        noise = ((seed & 0xFFFF) / 32768.0) - 1.0
        out.append(noise * _env(i, SAMPLE_RATE, 0.0002, 0.012))
    lp = 0.0
    filtered = []
    for s in out:
        lp += 0.5 * (s - lp)  # a crude one-pole low-pass to take the harsh edge off
        filtered.append(lp * 1.4)
    return _normalize(_fade(filtered))


def synth_open_hat():
    """A ringing open hat: a longer metallic noise burst that fades over ~0.4 s."""
    n = int(0.42 * SAMPLE_RATE)
    out = []
    seed = 0xBEAD
    lp = 0.0
    for i in range(n):
        t = i / SAMPLE_RATE
        seed = (seed * 1103515245 + 12345) & 0x7FFFFFFF
        noise = ((seed & 0xFFFF) / 32768.0) - 1.0
        lp += 0.4 * (noise - lp)
        out.append(lp * 1.5 * _env(i, SAMPLE_RATE, 0.0005, 0.10))
    return _normalize(_fade(out))


FACTORY_KIT = {
    "one-shots/drums/kicks/kick_analog_sub_e1.wav": synth_kick,
    "one-shots/drums/snares/snare_acoustic_crack_d1.wav": synth_snare,
    "one-shots/drums/hats/hat_closed_bright_tick.wav": synth_closed_hat,
    "one-shots/drums/hats/hat_open_airy.wav": synth_open_hat,
}


def write_wav_pcm24(path, samples):
    """Write a 24-bit mono PCM WAV at 48 kHz (standard library only)."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    half = 0xFFFFFF / 2.0
    frames = b""
    for s in samples:
        v = int(max(0.0, min(1.0, (s + 1.0) * 0.5)) * 0xFFFFFF)
        frames += struct.pack("<I", v)[0:3]
    with wave.open(path, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(3)
        w.setframerate(SAMPLE_RATE)
        w.writeframes(frames)


def main(argv):
    parser = argparse.ArgumentParser(description="Synthesize the factory analog drum kit one-shots (CC0, deterministic).")
    parser.add_argument("--dry-run", action="store_true", help="print what would be written without writing")
    args = parser.parse_args(argv)
    repo_root = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    for rel, synth in FACTORY_KIT.items():
        dest = os.path.join(repo_root, rel)
        if args.dry_run:
            print("would write", rel)
            continue
        write_wav_pcm24(dest, synth())
        print("wrote", rel)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
