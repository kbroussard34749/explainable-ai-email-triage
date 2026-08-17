# Week 8 Project Demonstration — Multilingual Media QA

- **Prepared for:** Keith G. Broussard
- **Course:** MSAI-699-B01 Capstone
- **QA date:** 2026-08-17
- **Package:** `Week_8_Project_Demonstration_Multilingual/`
- **Recommended submission:** `Week_8_Project_Demonstration_Keith_Broussard_Multilingual_Subtitles.mp4`

## Scope

The revised demonstration adds an explicit repository evidence map and an organic closing thank-you to the professor and class. English remains the authoritative narration. Separate Spanish, Hindi, and Simplified Chinese editions use user-authorized language-specific voice synthesis based on Keith's reference voice. The English-authoritative edition provides four selectable subtitle tracks.

The 11-scene visual sequence shows the controlled research boundary, synthetic input, actual 49.5% result, 0.45/0.50 threshold disagreement, bounded feature contributions, human-review and privacy limits, safe missing-model behavior, 13 automated tests, 60 deterministic inferences, exact repository evidence paths, and the closing thank-you. Representative-frame inspection found all scenes readable, correctly ordered, and free of private or unrelated content.

## Narration and Caption Fidelity

- Each language contains 41 sentence-level caption cues across 11 scenes.
- English narration was transcribed sentence by sentence with local ASR; required technical claims were preserved.
- Spanish narration received sentence-level local ASR review and preserved the required claims.
- Chinese narration was regenerated after QA identified a pronunciation issue. The final ASR preserved the critical values 49.5%, 0.45, 0.50, 13 tests, and 60 inferences.
- Hindi narration was regenerated with native-language number words. Local ASR remained inconsistent when rendering Hindi decimal phrases, so the exact authoritative values remain visible in the interface and matching Hindi subtitles. No technical value was removed from the source narration or captions.
- All embedded subtitle tracks were extracted and compared with the external SRT text. Every comparison passed.

## Technical Validation

| Edition | Duration | Embedded subtitles | Loudness | True peak | Full A/V decode |
|---|---:|---|---:|---:|---|
| English | 4:03.860 | English, default | -17.62 LUFS | -1.39 dBTP | Passed |
| Spanish | 5:26.140 | Spanish, default | -16.62 LUFS | -1.43 dBTP | Passed |
| Hindi | 4:43.740 | Hindi, default | -16.68 LUFS | -1.41 dBTP | Passed |
| Simplified Chinese | 4:20.780 | Simplified Chinese, default | -16.65 LUFS | -1.43 dBTP | Passed |
| Multilingual subtitles | 4:03.860 | English default; Spanish, Hindi, and Simplified Chinese selectable | -17.62 LUFS | -1.39 dBTP | Passed |

All five videos are H.264, 1920×1080, 30 fps, with AAC mono audio at 48 kHz. All four external SRT files contain 41 cues. The multilingual edition's four subtitle streams were extracted successfully, English is the only default subtitle, and all subtitle text matched its external language file.

## Integrity Hashes

### Videos

- English: `e2245f6d25488ef38b9b908b12e8ad791c8ee833eb925ffaa3a9be3271f3ac9f`
- Spanish: `81321e1a14cc69b4eb1f0265ea72670b87f13710c720940bbe3de6e9d8b44830`
- Hindi: `331908ee567f008e81ff2a872a776c25173a2840af3fdd40bdca9fdf477ab127`
- Simplified Chinese: `549da7f5801df8c387c8b1d70a10910d8f015d12f02ca278d1ed8fd3d6a34c4e`
- Multilingual subtitles: `c26b00b5020df8630e5acedf16ed1161857329537910ece1260b2276764fd508`

### External Captions

- English: `f54fa1c26cc0c03533140979b6afec03648fb312ed5473d422bd68e64a496c0e`
- Spanish: `0b1c96ab913fc96a22f23c278c73a55c9fd166a53550d3c5a56d15379b60c2e3`
- Hindi: `a1c049d8bc68da6a259f6ed2cb74a88b958b1791796cfc28fb5478f44df01fe9`
- Simplified Chinese: `37b624e1db1fe14e37a99a44b86e2897358057a20bbf788b2c4b4b6d033c9a33`

## Repository Evidence Boundary

The best review entry point is `docs/project_review_guide.md`, linked from the repository's main `README.md`. It connects the claims in `docs/` to the exact CSV and JSON evidence in `results/metrics/`. The demonstration and repository support Gate A application readiness only. The classifier remains `revise`; Gate B predictive reliability did not pass; human review is required; and shadow testing and production deployment remain unapproved.

## Remaining Human Check

Before Blackboard submission, replay the recommended multilingual-subtitle MP4 once with sound on and confirm that the authorized English synthesized narration and final closing are acceptable. Optionally spot-check the three dubbed editions. Blackboard submission and its single remaining attempt are not part of this QA.
