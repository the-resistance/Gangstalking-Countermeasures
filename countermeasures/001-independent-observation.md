---
Document Title: CM-001 — Independent Observation and Sound-Source Identification
Document ID: CM-001
Countermeasure Number: CM-001
Author: Kevin Mahan
Version: 1.0.0
Created: 2026-10-08T11:07:03-05:00
Last Updated: 2026-10-08T11:07:03-05:00
Category: Independent observation / source investigation
Associated Scenarios: SCN-001
---

# CM-001 — Independent Observation and Sound-Source Identification

This proposed observation procedure is associated with [SCN-001](../scenarios/001-audible-beeping-transitioning.md). Follow the [Versioning Policy](../governance/VERSIONING.md) and [Anti-Drift Policy](../governance/ANTI_DRIFT.md). Record only observations actually made; do not infer a source from an object or vehicle merely being nearby.

## Objective

Use independent observation and synchronized recordings to determine whether an audible event can be independently detected and whether its physical source can be identified. Record separately whether a sound was detected, independently confirmed, and attributed to a specific source.

## Applicable Conditions

Use only for an ordinary transition that the participant has independently chosen to observe, with a trusted observer who agrees to participate. Select a lawful public or otherwise authorized observation position and respect privacy, access restrictions, and applicable recording laws. Do not approach, follow, confront, or record people in private spaces.

## Technical Basis

Independent firsthand notes and recordings with aligned clocks can help compare event timing, sound characteristics, and environmental conditions. A recording can document what its microphone captured; it does not alone establish a source, cause, or intent. Clock alignment, microphone placement, recording quality, and ambient noise limit precision. Distinguish a verified physical source from a nearby object or vehicle whose operation has not been established.

## Required Equipment

- A recording device capable of documenting relevant audio; video is optional and should be used only when lawful and privacy-respecting.
- A second observer's recording device or written observation method.
- A way to compare device clocks or record their offset.
- A written observation log or the [SCN-001 incident recording form](../scenarios/001-audible-beeping-transitioning.md#incident-recording-template).

Do not create or imply recordings where none exist.

## Preparation

1. Arrange for a trusted second observer before the anticipated transition; obtain agreement to participate and discuss lawful recording and privacy.
2. Choose a safe observation position in a public or authorized area without trespassing or obstructing others.
3. Align device clocks where practical. Record each device's displayed time and any known offset; do not claim perfect synchronization.
4. Prepare audio or video equipment and confirm storage, battery, and microphone placement.
5. Decide in advance what event will be observed and what objective measures will be recorded.

## Procedure

1. **Begin before the transition.** The primary participant remains in the ordinary location where the reported event occurs. The second observer independently monitors the surrounding environment from the authorized position. Start any planned recordings before the anticipated transition and log each recording's start time.
2. **Record the transition.** Perform only the ordinary transition being observed. Potential examples include awakening and beginning movement, moving inside a parked vehicle, unlocking it, opening a door, or activating vehicle electronics. Record the transition time and the action actually performed.
3. **Make independent notes.** Without coordinating descriptions during the event, the second observer records firsthand:
   - Exact time of any audible event and the observer's clock reference.
   - Number of beeps, duration, and audible characteristics.
   - Estimated direction, noting uncertainty.
   - Nearby environmental activity and directly observed equipment operation.
   - Observable vehicle lighting changes.
4. **Compare records.** After the observation, compare the participant's account, observer's independent notes, and recording timestamps. Preserve original files and document any clock offsets, edits, or conversions.
5. **Investigate candidate sources.** Examine only directly observable equipment or environmental conditions. If vehicle-system inspection or testing is appropriate, use an authorized owner/operator or qualified technician. Record what was tested and the result; do not identify a source based solely on proximity.
6. **Repeat when appropriate.** If the participant and observer freely agree, repeat during separate ordinary events. Record each session independently, including sessions where no sound is heard.
7. **Document results and limitations.** For each session, answer: Was a sound detected? Was it independently detected? Was a specific physical source identified and by what evidence? Did it occur near the documented transition? Were alternative explanations evaluated? Was any relationship reproduced?

## Expected Results

A timestamped observation record that states whether a sound was detected, whether the second observer independently detected it, whether its physical source was identified, and what evidence and limitations apply. A null result is also recorded; no outcome is assumed in advance.

## Evidence Collection

Preserve original recordings and notes when actually collected. Use a unique evidence identifier only for an actual evidence item, record acquisition time and time zone, retain available metadata, identify original versus derived files, and calculate SHA-256 hashes when original files are available. Follow the [Evidence Documentation Standards](../evidence/README.md) and use the [Evidence Log Template](../templates/EVIDENCE_LOG_TEMPLATE.md). Avoid publishing sensitive personal information.

## Effectiveness Evaluation

This procedure evaluates independent detection and source-identification evidence; it does not reduce or mask sound. For each session, compare the participant's report with the observer's separately recorded account and available recording. Report whether observations converge on event timing and characteristics, whether a source was affirmatively identified, and what alternative explanations remain. A nearby object alone is not source-identification evidence.

## Limitations

An observer or recording may fail to detect a quiet, brief, obstructed, or masked sound. Devices may have clock drift, automatic gain control, compression, or microphone limitations. Line-of-sight and estimated direction are uncertain. A correlation with transitioning does not establish monitoring, signaling, conditioning, or intent. Repetition under uncontrolled conditions does not by itself establish causation.

## Safety Considerations

Do not conduct observations while driving or operating a vehicle. Keep all participants in safe, authorized locations; do not trespass, confront anyone, interfere with equipment, or record where prohibited. Obtain consent from the participating observer, limit incidental capture of others, and handle recordings privately unless release is lawful and appropriate.

## Related Scenarios

- [SCN-001 — Audible Beeping During Transitioning](../scenarios/001-audible-beeping-transitioning.md)

## Appendments

No appendments are recorded at initial publication. Future procedural changes must be dated and separately identified; preserve this initial procedure in Git history.

## Governance References

- [Versioning Policy](../governance/VERSIONING.md)
- [Anti-Drift Policy](../governance/ANTI_DRIFT.md)
- [Evidence Documentation Standards](../evidence/README.md)

## Revision History

| Version | Timestamp | Description | Author |
|---------|-----------|-------------|--------|
| 1.0.0 | 2026-10-08T11:07:03-05:00 | Initial publication of an independent observation and sound-source identification procedure for SCN-001. | Kevin Mahan |
