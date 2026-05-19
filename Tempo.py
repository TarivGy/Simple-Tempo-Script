import sys
import librosa

def analyze(audio_path):
    y, sr = librosa.load(audio_path)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)

    bpm = tempo.item()
    first_beat_ms = beat_times[0] * 1000 if len(beat_times) else None
    return bpm, first_beat_ms, beat_times

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python tempo.py <audio_file>")
        sys.exit(1)

    bpm, first_beat_ms, beat_times = analyze(sys.argv[1])
    est_offset = first_beat_ms % (60000 / bpm)
    print(f"Estimated tempo: {bpm:.2f} BPM")
    if first_beat_ms is not None:
        print(f"First detected beat: {first_beat_ms:.2f} ms from start")
        print(f"Total beats detected: {len(beat_times)}")
        print(f"Calculated offset: {est_offset:.0f} ms")