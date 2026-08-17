# Candidate 3 Presentation Quality Assurance Record

## PowerPoint checks

- Slide count: 11
- Format: 16:9 widescreen
- Presentation structure: problem statement, stakeholder workflow, evidence boundary, methodology, data analysis, measured results, engineering validation, disposition, recommendation, and project access
- Render inspection: all 11 slides rendered and inspected at 1920 × 1080
- Overflow test: passed; no content overflow detected
- Template-fidelity test: passed; zero issues
- Speaker notes: 11 recording-aligned timing blocks and 11 repository-relative `[Sources]` blocks
- Links: the repository URL and `mailto:` university email link are present on Slide 11
- Placeholder scan: no `Click to add` or `Lorem ipsum` text remains
- Privacy and portability scan: no local course-folder paths, Blackboard links, or course-administration references are present
- Visual review: titles, card edges, timeline nodes, figure proportions, baselines, slide numbers, margins, and contact links were inspected in the final render

## Video and narration checks

- Runtime: 456.4 seconds, approximately 7:36
- Video: H.264, 1920 × 1080, 30 frames per second
- Audio: AAC, 48 kHz, mono
- Audio level: mean −17.3 dB; peak −1.3 dB
- Pacing: narration slowed four percent without pitch alteration to improve metric-heavy sections
- Embedded subtitles: English, Spanish, Hindi, and Simplified Chinese
- Default subtitle: English
- Subtitle cues: 67 per language
- Decode test: the complete video and audio streams decoded without errors
- Subtitle extraction: all four embedded subtitle streams extracted without errors and retained 67 cues
- Transition test: frames sampled from the midpoint of all 11 measured intervals matched the intended slide order
- Narration construction: generated locally from the approved voice reference using sentence-bounded segments and the final spoken-words script
- Closing transcription check: the final recording contains one spoken “Thank you.”

## Evidence checks

- Reports 517,401 Enron source records
- Reports 199 reviewed messages: 30 urgent and 169 nonurgent
- Reports the fixed 159-message training and 40-message preliminary holdout split
- Explains that nested cross-validation used outer evaluation folds and inner threshold-selection folds
- States that the preliminary holdout is descriptive evidence rather than an untouched final test
- Reports the frozen 0.45 holdout comparison correctly: all 6 urgent messages identified and all 34 nonurgent messages labeled urgent
- Reports the 0.50 preliminary holdout comparison correctly: 2 of 6 urgent messages identified, 4 false negatives, and 1 false positive
- Reports threshold 0.45 outer-fold evidence correctly: 100% urgent recall, 26.2% urgent F1, 135 false positives, and all 159 training messages predicted urgent
- Reports threshold 0.50 outer-fold evidence correctly: 8.3% urgent recall, 15.4% urgent F1, 22 false negatives, and no false positives
- Reports that 157 of 159 out-of-fold probabilities fell from 0.45 to below 0.50
- Reports Gate A as passed with 13 automated tests, 60 deterministic synthetic inferences, and five validation checks
- Reports Gate B as failed and preserves the `revise` disposition
- Identifies Gate A as Week 7 software and interface readiness for the planned Week 8 demonstration
- Does not imply that a Week 7 demonstration occurred
- Does not claim predictive reliability, shadow-testing approval, production readiness, demographic fairness, or production performance

## Checksums

- PowerPoint SHA-256: `a84b6c0545e070bba05bfbf4aa4f833a431b38a24087410db644b8397b26b1cb`
- MP4 SHA-256: `2f90515bc75b3b01d1cb5c79f44318615e550a6a90f429eba2caf59e6b43efdf`
- Spoken-words script SHA-256: `8660b05385edb14395fd437e567a18fc98bd22e69477a676bd1f7e31add9b586`
- Timed narration plan SHA-256: `b45b59a032001ab3367667e8481db907e2fa87a1fb31ccbf4d76abcc43138603`
