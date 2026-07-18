# Urgency Labeling Guide

**Label version:** 1.0  
**Reviewer:** Keith G. Broussard  
**Target:** Determine whether the current email requires timely attention from its recipient.

## Labels

| Label | Deterministic rule | Example |
|---|---|---|
| `urgent` | The recipient faces an imminent deadline, active incident, or meaningful consequence from delayed action. | An account must be secured today after a suspicious login. |
| `nonurgent` | The message is informational, routine, optional, resolved, or lacks a meaningful time constraint. | A monthly newsletter is available. |
| `needs_review` | The full message still lacks enough context or contains conflicting urgency evidence. | “Please handle this as discussed.” |

## Decision Sequence

Apply these rules in order.

| Step | Rule | Result |
|---|---|---|
| 1 | The record is empty, malformed, unreadable, or a duplicate. | Exclude |
| 2 | Read the 2,000-character review excerpt. If `excerpt_truncated` is true or the context is insufficient, inspect the full message. | Continue review |
| 3 | The full message still lacks enough context for a reliable label. | `needs_review` |
| 4 | The requested action applies entirely to someone other than the recipient. | Usually `nonurgent` |
| 5 | The recipient must act within 24 hours or by an explicit imminent deadline. | `urgent` |
| 6 | Delay could cause a security, account-access, financial, legal, academic, or operational consequence. | `urgent` |
| 7 | The message reports an active outage, access failure, security event, or other ongoing disruption requiring action. | `urgent` |
| 8 | The request has no meaningful deadline or consequence, or the message is informational, optional, promotional, routine, or resolved. | `nonurgent` |
| 9 | Credible evidence supports conflicting labels. | `needs_review` |

## Interpretation Rules

| Situation | Rule |
|---|---|
| “Urgent,” “immediately,” or “ASAP” appears | Do not label `urgent` unless the message also contains an applicable action, deadline, active incident, or credible consequence. |
| A quoted thread contains urgent language | Evaluate the newest message and the current unresolved request. |
| The message says the issue was resolved | Label `nonurgent`. |
| A deadline has passed | Label `urgent` if action and consequences remain; otherwise use `needs_review`. |
| A meeting is imminent | Label `urgent` only if the recipient must prepare, attend, respond, or correct something. |
| A general security newsletter describes threats | Label `nonurgent`. |
| A message reports a specific compromised account | Label `urgent`. |
| The message is automatically generated | Judge the required action and consequence, not the sender type. |
| The review excerpt is truncated or lacks necessary thread context | Inspect the full message before labeling. Use `needs_review` only if the available full context remains insufficient or conflicting. |

## Review Procedure

1. Assign only one label per record.
2. Write a brief `label_reason` based on the applicable rule.
3. Review the full email when the 2,000-character excerpt is truncated or insufficient.
4. Use `needs_review` only after reviewing all available context.
5. Exclude unresolved `needs_review` records from initial model training and evaluation.
6. Record any new recurring ambiguity before changing these version 1.0 rules.

## Compact Rule

```text
IF unusable or duplicate:
    EXCLUDE
ELSE IF context remains insufficient after reviewing the full message:
    NEEDS_REVIEW
ELSE IF the recipient faces an imminent deadline, active incident,
        or meaningful consequence from delayed action:
    URGENT
ELSE:
    NONURGENT
```
