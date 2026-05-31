<!--
Copyright 2026 Kevin "Andie" Williams

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

SPDX-License-Identifier: Apache-2.0
-->

# Move Section Audit 001

Author: Kevin "Andie" Williams  
Status: Audit report  
Project: You Have Another Option  
Repository: AnotherOption  
Date: 2026-05-30

---

## 1. Purpose

This audit responds to the C Bridge Sprint review package and Andie's authorial note:

> I would say not ten examples. 1-2. But keep them maybe? Might need them later.

The audit checks Options 001–008 for Move section length, list count, and cognitive load.

No prose repairs are executed in this audit.

---

## 2. Audit Conclusion

Pattern confirmed.

Across the first eight Options, Move sections often carry too many examples or too many prompt questions.

This does not usually break word count.

It does create scan-load.

For a dysregulated reader, long example strings can feel like another task instead of a handhold.

Recommended rule:

> Move sections should usually contain one leading question or action and one to two examples.
>
> Five examples is a hard ceiling, not a target.
>
> Lists beyond five items violate the Bathroom Chapter Rule in spirit even when the word count is technically short.

---

## 3. File-by-File Audit

| File | Move pattern | Count / load | Status |
|---|---|---:|---|
| `Options/001-the-saxophone.md` | one main reflective question plus several follow-up questions | 5 prompt questions | watch |
| `Options/002-the-broken-tool.md` | one sentence move plus long inline example scan | ~8 examples inline | watch / later trim possible |
| `Options/003-you-were-never-going-to-make-those-notes.md` | one strong grief/shame move plus long inline example scan | ~11 examples inline | watch / later trim possible |
| `Options/004-the-first-mercy.md` | one pressure-naming move plus long example scan | ~9 examples | watch / later trim possible |
| `Options/005-another-option.md` | one pressure choice, one question, then two lists | 11 pressure examples + 10 option examples | repair recommended later |
| `Options/006-why-this-book-exists.md` | one stayable-life question plus example scan | 9 examples | repair now |
| `Options/007-the-problem-is-not-autistic-behavior.md` | one behavior-as-signal question plus example scan | 8 examples | repair now |
| `Options/008-the-number-is-not-destiny.md` | two nested questions plus example scan | 8 examples | repair now |

---

## 4. Immediate Repairs Recommended

Apply now to Bridge Sprint files:

### Option 006

Trim Move examples to one or two.

Suggested keeps:

```text
a room
a recurring demand that takes more from you than people can see
```

Hold the rest in a future examples bank.

### Option 007

Trim Move examples to one or two.

Suggested keeps:

```text
sound
too many demands
```

Add protective sentence before the Move prompt to address the difference between applying the question to oneself and to someone else.

Suggested sentence:

```text
If you are asking this about your own behavior, go slowly; it can be harder to offer yourself curiosity than to offer it to someone else.
```

### Option 008

Reduce to one leading question.

Suggested lead:

```text
What is one preventable pressure near me?
```

Trim examples to one or two.

Suggested keeps:

```text
sensory overload
having no one to call before things get worse
```

---

## 5. Held Material Recommendation

Do not discard excess examples.

Create a later holding file:

```text
Holding/move-examples-bank.md
```

Purpose:

- preserve useful examples cut from Move sections;
- allow future reuse in workbooks, companion guides, worksheets, or later Options;
- reduce reader load without losing raw material.

---

## 6. Workflow Update Recommended

Update `rfc/editorial-workflow.md` with the Move section rule.

Recommended text:

```text
Move sections should usually contain one leading question or action and one to two examples. Five examples is a hard ceiling, not a target. Lists beyond five items violate the Bathroom Chapter Rule in spirit even when the word count is technically short.
```

---

## 7. Status

Audit complete.

No prose repairs executed in this file.

Proceed after Andie confirms the proposed one-to-two example keeps and the protective sentence for Option 007.
