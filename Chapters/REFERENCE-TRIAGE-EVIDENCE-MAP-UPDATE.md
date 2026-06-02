# REFERENCE-TRIAGE-EVIDENCE-MAP-UPDATE.md

Author: Kevin "Andie" Williams, with G
Status: Draft v0.1 — awaiting Andie adjudication
Project: Tiny Door — You Have Another Option
Evidence standard: proof, not citation
Date: 2026-06-02

---

## Purpose

This addendum records completion status for the first-pass T1 evidence maps drafted on 2026-06-02. It exists as a safe append-only companion to `Chapters/REFERENCE-TRIAGE.md` so the full 208-reference triage register is not accidentally overwritten while updating the Priority Queue.

---

## Evidence Map Drafting Status

T1 evidence maps have been drafted for all requested claim groups.

Created files:

- `References/ABA-EVIDENCE-MAP.md`
- `References/MORTALITY-EVIDENCE-MAP.md`
- `References/DOUBLE-EMPATHY-EVIDENCE-MAP.md`
- `References/MASKING-EVIDENCE-MAP.md`
- `References/STANFORD-PRISON-EVIDENCE-MAP.md`
- `References/CONVERSION-THERAPY-LEGAL-EVIDENCE-MAP.md`

---

## Priority Queue Update

The `Chapters/REFERENCE-TRIAGE.md` Priority Queue should now point to the drafted map files:

**Lifespan and mortality claims:**
Refs 1, 46, 47, 100, 122  
Evidence map: `References/MORTALITY-EVIDENCE-MAP.md`

**ABA harm claims:**
Refs 23, 37, 38, 39, 40, 126, 128, 129, 130, 137, 138, 140  
Evidence map: `References/ABA-EVIDENCE-MAP.md`

**Double empathy / social theory:**
Ref 63  
Evidence map: `References/DOUBLE-EMPATHY-EVIDENCE-MAP.md`

**Masking and harm:**
Ref 188  
Evidence map: `References/MASKING-EVIDENCE-MAP.md`

**Stanford Prison Experiment / obedience:**
Refs 132, 134  
Evidence map: `References/STANFORD-PRISON-EVIDENCE-MAP.md`

**Conversion therapy legal classification:**
Refs 37, 38, 39, 40  
Evidence map: `References/CONVERSION-THERAPY-LEGAL-EVIDENCE-MAP.md`

---

## Issues Surfaced During Evidence Mapping

The first-pass maps identified several source-control issues that should be adjudicated before manuscript use:

- Ref 46 is commentary, not the primary Danish suicide study.
- Ref 47 appears to be a wrong-slot JAMA life-expectancy/income source, not autism mortality evidence.
- Ref 122 remains content-unconfirmed from the URL alone.
- Ref 134 appears to be Milgram/obedience journalism, not Stanford Prison Experiment-specific critique.
- Ref 188 is the Health Stigma and Discrimination Framework, not an autistic masking study.
- Ref 137 appears to be Kupferstein (2018) and should be verified immediately because it may already be the missing ABA/PTSD source.
- Ref 147 remains wrong-slot for ABA/PTSD and should be removed or reassigned.

---

## Suggested Replacement Text for `Chapters/REFERENCE-TRIAGE.md`

Replace the existing `## Priority Queue for Evidence Maps` section with the following after Andie review:

```markdown
## Priority Queue for Evidence Maps

T1 evidence maps have been drafted for all current high-priority claim groups. Each map remains Draft v0.1 and awaits Andie adjudication before manuscript reliance.

**Lifespan and mortality claims:**
Refs 1, 46, 47, 100, 122  
Evidence map: `References/MORTALITY-EVIDENCE-MAP.md`

**ABA harm claims:**
Refs 23, 37, 38, 39, 40, 126, 128, 129, 130, 137, 138, 140  
Evidence map: `References/ABA-EVIDENCE-MAP.md`  
Note: ref 137 appears to be Kupferstein (2018) and should be verified immediately; ref 147 remains wrong-slot for ABA/PTSD.

**Double empathy / social theory:**
Ref 63  
Evidence map: `References/DOUBLE-EMPATHY-EVIDENCE-MAP.md`

**Masking and harm:**
Ref 188  
Evidence map: `References/MASKING-EVIDENCE-MAP.md`  
Note: ref 188 appears to be a wrong-slot stigma-framework source, not a masking study.

**Stanford Prison Experiment / obedience:**
Refs 132, 134  
Evidence map: `References/STANFORD-PRISON-EVIDENCE-MAP.md`  
Note: ref 134 appears to be Milgram/obedience journalism, not SPE-specific critique.

**Conversion therapy legal classification:**
Refs 37, 38, 39, 40  
Evidence map: `References/CONVERSION-THERAPY-LEGAL-EVIDENCE-MAP.md`
```

---

Status: Draft v0.1
Date: 2026-06-02
Next action: Andie reviews; then merge this addendum into `Chapters/REFERENCE-TRIAGE.md` when safe full-file patching is available.
