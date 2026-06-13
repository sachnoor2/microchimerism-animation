#!/usr/bin/env python3
import asyncio
import edge_tts
import os
import subprocess
from pathlib import Path

FPS = 60
AUDIO_DIR = Path("public/audio")
SEG_DIR = AUDIO_DIR / "segments"
TOTAL_FRAMES = 2700

AUDIO_DIR.mkdir(parents=True, exist_ok=True)
SEG_DIR.mkdir(parents=True, exist_ok=True)

SCENES = [
    { "id": "s01", "fs": 15,   "fe": 180,  "text": "Aap apni maa ke dil mein abhi bhi zinda hain. Literally." },
    { "id": "s02", "fs": 215,  "fe": 500,  "text": "Pregnancy ke waqt, bache ke kuch cells placenta cross karke maa ke khoon mein mil jaate hain." },
    { "id": "s03", "fs": 535,  "fe": 760,  "text": "Isse Microchimerism kehte hain." },
    { "id": "s04", "fs": 790,  "fe": 1060, "text": "Ye cells sirf wahan rehte nahi—ye repair team ki tarah kaam karte hain." },
    { "id": "s05", "fs": 1095, "fe": 1450, "text": "Agar maa ka dil ya lungs damage ho jayein, toh ye bache ke cells wahan jaakar naye tissue ban jaate hain." },
    { "id": "s06", "fs": 1490, "fe": 1900, "text": "Science ke hisaab se, aapka ek hissa aapki maa ke andar dashakon tak dhadakta rehta hai." },
    { "id": "s07", "fs": 1950, "fe": 2200, "text": "Aap unhe kabhi poori tarah nahi chhodte." },
    { "id": "s08", "fs": 2250, "fe": 2680, "text": "Kya aapne kabhi apni maa ke liye ye 'healing' feel ki hai? Comment mein batao." },
]

VOICES = {
    "Madhur": "hi-IN-MadhurNeural",
    "Swara": "hi-IN-SwaraNeural"
}

async def generate_scenes(voice_key, voice_id):
    print(f"── Generating Narration with {voice_key} ({voice_id}) ──")
    v_dir = SEG_DIR / voice_key
    v_dir.mkdir(parents=True, exist_ok=True)
    for sc in SCENES:
        print(f"  Synthesizing {sc['id']} for {voice_key}...")
        communicate = edge_tts.Communicate(sc["text"], voice_id, rate="+10%")
        await communicate.save(str(v_dir / f"{sc['id']}.mp3"))

def combine_audio(voice_key):
    v_dir = SEG_DIR / voice_key
    total_s = TOTAL_FRAMES / FPS
    inputs, filter_parts, labels = [], [], []
    for idx, sc in enumerate(SCENES):
        seg = v_dir / f"{sc['id']}.mp3"
        start_ms = int(sc["fs"] / FPS * 1000)
        inputs += ["-i", str(seg)]
        filter_parts.append(f"[{idx}]adelay={start_ms}|{start_ms}[d{idx}]")
        labels.append(f"[d{idx}]")

    fc = ";".join(filter_parts) + ";" + "".join(labels) + f"amix=inputs={len(SCENES)}:normalize=0[out]"
    output_path = AUDIO_DIR / f"narration_{voice_key.lower()}.mp3"
    subprocess.run(["ffmpeg", "-y"] + inputs + ["-filter_complex", fc, "-map", "[out]", "-t", str(total_s), "-b:a", "192k", str(output_path)], check=True)
    print(f"✅ {voice_key} Audio pipeline complete: {output_path}")

async def main():
    print("\n🚀 STARTING NARRATOR: MADHUR")
    await generate_scenes("Madhur", VOICES["Madhur"])
    combine_audio("Madhur")

if __name__ == "__main__":
    asyncio.run(main())
