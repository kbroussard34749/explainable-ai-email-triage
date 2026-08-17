# Week 7 Presentation Candidate 3

Candidate 3 is the expanded stakeholder presentation for the Explainable AI Email Triage capstone. It retains Candidate 2's restrained visual system while adding the context needed to explain the evidence review, nested evaluation, preliminary holdout, Week 7 software validation, planned Week 8 demonstration, and final recommendation. Candidates 1 and 2 remain unchanged for comparison.

## Start here

- `Week_7_Capstone_Presentation_Keith_Broussard_Candidate_3.pptx` — editable 11-slide presentation with recording-aligned speaker notes and repository-relative source blocks.
- `Week_7_Capstone_Presentation_Keith_Broussard_Candidate_3_Multilingual.mp4` — 7:36 narrated presentation with selectable English, Spanish, Hindi, and Simplified Chinese subtitle tracks.
- `Week_7_Candidate_3_Timed_Narration_Plan.txt` — measured slide-transition plan coordinated to the MP4.
- `Week_7_Candidate_3_Spoken_Words.txt` — narration text without timing instructions.
- `Week_7_Capstone_Presentation_Candidate_3_English.srt` — authoritative English captions.
- `Week_7_Capstone_Presentation_Candidate_3_Spanish.srt` — Spanish accessibility captions.
- `Week_7_Capstone_Presentation_Candidate_3_Hindi.srt` — Hindi accessibility captions.
- `Week_7_Capstone_Presentation_Candidate_3_Simplified_Chinese.srt` — Simplified Chinese accessibility captions.
- `Week_7_Capstone_Presentation_Candidate_3_QA.md` — content, layout, timing, caption, and evidence validation record.

## Presentation logic

The 11-slide sequence addresses the assignment's required problem statement, methodology, data analysis, results, and conclusions. The expanded narrative adds five points that benefit a stakeholder audience:

1. a concrete explanation of the human-control boundary;
2. the evidence a reviewer will see in the planned Week 8 demonstration;
3. how nested cross-validation separates inner selection from outer evaluation;
4. why the preliminary holdout is descriptive rather than untouched final evidence; and
5. a direct recommendation for Week 8 and any later model experiment.

## Evidence boundary

The presentation preserves the frozen Week 6 `revise` disposition. During Week 7, Gate A passed as a software and interface readiness check: 13 automated tests passed, 60 repeated synthetic inferences were deterministic within each case, and all five validation checks passed. This prepares the repository for the planned Week 8 controlled local demonstration; it does not establish predictive reliability. Gate B failed because neither tested threshold provided a reliable operating point. Human review remains required, and neither shadow testing nor production deployment is approved.

The preliminary holdout is reported as descriptive evidence at both tested thresholds. At 0.45, the model identified all six urgent messages but labeled all 34 nonurgent messages urgent. At 0.50, it identified two of the six urgent messages, missed four, and produced one false positive. This comparison explains why full recall at 0.45 did not constitute a usable operating point.

The English narration is authoritative. Translated subtitle tracks are accessibility aids and preserve technical terms and the model's decision boundary. All visible project claims trace to executed notebooks, saved metrics, figures, experiment records, test results, or decision artifacts in the repository.

## Playback

Open the MP4 in a player that supports selectable subtitle tracks. English is the default embedded track. The four SRT files are included for learning-management systems or players that prefer sidecar captions.
