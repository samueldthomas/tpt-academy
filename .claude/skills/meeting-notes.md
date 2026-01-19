---
name: meeting-notes
description: Process meeting transcripts into decisions, action items, and summaries
---

# Meeting Notes Processor

You are processing a meeting transcript to extract structured information. Follow these instructions carefully.

## Required Inputs

**Meeting transcript**: The user will provide either:
- A text file path to read
- Pasted transcript text directly

**Attendee list** (optional): If provided, use for owner assignment validation.

## Processing Steps

1. Read the entire transcript carefully
2. Identify all decisions, action items, risks, and open questions
3. Extract supporting quotes for key items
4. Format output according to the structure below

## Output Format

Structure your response with these sections:

### 1. Decisions
For each decision:
- **Decision**: [Clear statement of what was decided]
- **Rationale**: [Why this decision was made]
- **Supporting quotes**:
  > "[Quote 1 from transcript]"
  > "[Quote 2 from transcript]"
  > "[Quote 3 from transcript]"

### 2. Action Items
| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| [Task description] | [Name or "unassigned"] | [Date or "TBD"] | [Open] |

### 3. Risks Identified
- **Risk**: [Description]
  - Likelihood: [High/Medium/Low or "uncertain"]
  - Impact: [High/Medium/Low or "uncertain"]
  - Mitigation discussed: [Yes/No - details if yes]

### 4. Open Questions
- [ ] [Question that remains unresolved]
- [ ] [Another open question]

### 5. Summary for Distribution
[2-3 paragraph summary suitable for sharing with stakeholders who weren't in the meeting. Include key decisions, critical action items, and next steps.]

## Rules

- **Never invent information**: Only include owners and due dates explicitly stated in the transcript
- **Mark uncertainty**: If something is implied but not explicit, mark it as "uncertain" or "implied"
- **No assumptions**: If an owner isn't named, use "unassigned" not a guess
- **Quote accuracy**: Use exact quotes from the transcript, not paraphrases
- **Completeness**: Capture all decisions and action items, even minor ones

## Proof Step

Before finalizing, verify each decision by listing the transcript quotes that support it. This allows the human to confirm accuracy.

Format:
```
VERIFICATION:
Decision 1: "[supporting quote]" (line/timestamp if available)
Decision 2: "[supporting quote]" (line/timestamp if available)
```

## Example Invocation

User: `/meeting-notes` then provides transcript

Or: `/meeting-notes path/to/transcript.txt`
