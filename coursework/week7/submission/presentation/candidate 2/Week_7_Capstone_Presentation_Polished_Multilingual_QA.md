# Polished Presentation Quality Assurance Record

## PowerPoint checks

- Slide count: 9
- Format: 16:9 widescreen
- Render inspection: all nine slides inspected at 1920 × 1080
- Overflow test: passed; no element overflow detected
- Template-fidelity test: passed; zero issues
- Speaker notes: coordinated to the 5:36 narration, use recording-aligned timing cues, and include repository-relative source blocks
- Links: repository and university email links are present and clickable on Slide 9
- Content audit: no unrelated alternate-deck datasets, citations, local course paths, or course-administration references remain
- Structure: Candidate 1's original nine-slide geometry was retained; no alternate-deck panels, pills, overlays, or duplicate graphics were added
- Alignment review: every slide was inspected individually at full resolution, including card edges, timeline nodes, text baselines, figure proportions, and margins
- Visual system: dark opening, disposition, and contact frames are balanced by open white evidence slides and a restrained navy, blue, orange, and red palette

## Video checks

- Runtime: 336.033 seconds, approximately 5:36
- Video: H.264, 1920 × 1080, 30 frames per second
- Audio: AAC, 48 kHz, mono
- Embedded subtitles: English, Spanish, Hindi, and Simplified Chinese
- Default subtitle: English
- Subtitle cues: 91 per language
- Decode test: video and audio decoded without errors; all four subtitle streams extracted without errors
- Narration integrity: encoded audio SHA-256 matches the previously reviewed presentation audio stream
- Visual synchronization: frames sampled from the middle of all nine slide intervals matched the intended slide order

## Evidence checks

- Retains the Week 6 `revise` disposition
- Reports 199 reviewed messages: 30 urgent and 169 nonurgent
- Reports the fixed 159-message training and 40-message preliminary holdout split
- Reports threshold 0.45 as 100% urgent recall with 135 false positives and all messages predicted urgent
- Reports threshold 0.50 as 8.3% urgent recall with 22 false negatives and no false positives
- Reports Gate A as passed with 13 automated tests and 60 deterministic synthetic inference runs
- Reports Gate B as failed and does not claim shadow-testing or production approval

## Checksums

- PowerPoint SHA-256: `0538bb5bc5856d12fb862bba111ffc43a14545d2f64faabff026bbe763029202`
- MP4 SHA-256: `bc83d7aa7432485df5f1b9593adc2d11c6384f6eae2d15484882f9db4675bcce`
