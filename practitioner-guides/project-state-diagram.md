# Project state markers — state diagram & short overview

This Practitioner Guide shows typical lifecycle states an open-source project may be in and recommended actions for users, contributors, and adopters.

> Issue: [Practitioner Guide]: Project state markers (state diagram & overview) — CHAOSS WG Data Science. (See issue #165)

---

## State diagram (Mermaid `stateDiagram-v2`)

```mermaid
stateDiagram-v2
    state "New" as new
    state "Maintained/Active" as maintained
    state "Abandoned/Unmaintained" as abandoned
    state "Archived" as archived
    state "Quarantined" as quarantined
    state "Dormant" as dormant
    state "Under custodianship" as custody
    state "Deprecated" as deprecated
    state "Done" as done

    [*] --> new
    new --> maintained
    archived --> new : Fork
    archived --> maintained : Adopt
    maintained --> new : Fork
    maintained --> deprecated : Deprecate
    maintained --> quarantined
    maintained --> dormant
    maintained --> custody
    maintained --> done
    deprecated --> new : Superseed
    maintained --> archived : Deprecate
    custody --> new : Fork
    custody --> maintained : Adopt
    dormant --> abandoned
    dormant --> maintained : Handoff
    dormant --> new : Fork
    abandoned --> maintained : Adopt
    abandoned --> new : Fork
    archived --> [*]
    done --> [*]
    quarantined --> [*]
    abandoned --> [*]


