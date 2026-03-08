# Feedback Directory

This directory contains feedback from L3 projects to L0, L1, and L2 repositories.

## Purpose

- Provide usage feedback to upper layers
- Report issues and suggestions
- Share lessons learned
- Contribute improvements

## Feedback Structure

```
feedback/
├── to-L0/              # Feedback to SEARCH-R
│   ├── methodology/    # Methodology feedback
│   └── theory/         # Theory suggestions
├── to-L1/              # Feedback to agent-team-research
│   ├── research-agent/ # Research agent feedback
│   └── templates/      # Research template suggestions
├── to-L2/              # Feedback to AgentTeam-Template
│   ├── pm-agent/       # PM agent feedback
│   ├── templates/      # Team template suggestions
│   └── workflows/      # Workflow improvements
└── README.md           # This file
```

## Feedback Types

### 1. Issue Reports

**Format**: `issue-{date}-{id}.md`

```markdown
# Issue: {Issue Title}

**Layer**: L0/L1/L2
**Component**: {component name}
**Severity**: critical/high/medium/low
**Date**: {date}

## Description

{Detailed description of the issue}

## Impact

{How this affects the project}

## Reproduction

{Steps to reproduce, if applicable}

## Suggested Solution

{Your suggestions for fixing this}

## Context

- Project: knowledge-assistant-dev
- Version: {version}
- Environment: {environment details}
```

### 2. Enhancement Suggestions

**Format**: `enhancement-{date}-{id}.md`

```markdown
# Enhancement: {Enhancement Title}

**Layer**: L0/L1/L2
**Component**: {component name}
**Priority**: high/medium/low
**Date**: {date}

## Current Situation

{Describe current state}

## Proposed Enhancement

{Describe proposed improvement}

## Benefits

{Expected benefits}

## Implementation Ideas

{Ideas for implementation}

## Willing to Contribute

[ ] Yes, I can help implement this
[ ] Maybe, need more discussion
[ ] No, just suggesting
```

### 3. Usage Reports

**Format**: `usage-report-{date}.md`

```markdown
# Usage Report: {Month/Quarter}

**Period**: {start-date} to {end-date}
**Project**: knowledge-assistant-dev

## L0 (SEARCH-R) Usage

### Methodology
- SEARCH-R cycle used: X times
- Most useful phases: {phases}
- Challenges: {challenges}

### Theory
- Theory frameworks used: {list}
- New theory needs: {list}

## L1 (agent-team-research) Usage

### Research Tasks
- Research tasks delegated: X
- Success rate: X%
- Average completion time: X hours

### Skills Used
- web-search: X times
- document-analysis: X times
- code-exploration: X times
- knowledge-synthesis: X times

### Quality
- Research quality: excellent/good/acceptable
- Suggestions: {suggestions}

## L2 (AgentTeam-Template) Usage

### PM Agent
- Projects managed: X
- Teams created: X
- Tasks completed: X

### Templates Used
- core-team: X times
- ai-team: X times
- test-team: X times

### Workflows
- Workflow effectiveness: excellent/good/acceptable
- Suggestions: {suggestions}

## Overall Assessment

### What Works Well
- {item 1}
- {item 2}

### What Needs Improvement
- {item 1}
- {item 2}

### Top 3 Suggestions
1. {suggestion 1}
2. {suggestion 2}
3. {suggestion 3}
```

### 4. Lessons Learned

**Format**: `lesson-{date}-{id}.md`

```markdown
# Lesson Learned: {Lesson Title}

**Date**: {date}
**Context**: {project context}

## Situation

{Describe the situation}

## What Happened

{What actually happened}

## Why It Happened

{Root cause analysis}

## What We Learned

{Key learnings}

## How to Apply This

{How to apply this learning in future}

## Related

- Related to: L0/L1/L2 component
- Tags: {tags}
```

## Feedback Workflow

### 1. Create Feedback

```
1. Identify feedback type
2. Choose appropriate directory (to-L0, to-L1, or to-L2)
3. Create feedback file using template
4. Fill in details
```

### 2. Submit Feedback

```
1. Commit feedback file to this project
2. Optionally create issue in target repository
3. Link to feedback file
```

### 3. Track Feedback

```
1. Monitor target repository for response
2. Participate in discussions
3. Help implement if willing
```

## Feedback Guidelines

### DO:
- ✅ Be specific and provide examples
- ✅ Explain the impact on your project
- ✅ Suggest solutions when possible
- ✅ Provide context and environment details
- ✅ Follow up on feedback you submit

### DON'T:
- ❌ Submit vague complaints
- ❌ Expect immediate response
- ❌ Forget to provide context
- ❌ Be disrespectful or demanding

## Feedback Examples

### Good Example:

```markdown
# Issue: Research agent times out on large codebases

**Layer**: L1
**Component**: code-exploration skill
**Severity**: medium
**Date**: 2026-03-08

## Description

When using code-exploration skill on codebases larger than 10,000 files,
the skill times out after 5 minutes without completing analysis.

## Impact

Unable to get complete code analysis for large projects, forcing manual
analysis which takes significantly longer.

## Reproduction

1. Initialize research agent
2. Request code exploration on codebase with >10,000 files
3. Wait 5 minutes
4. Observe timeout error

## Suggested Solution

Add pagination or streaming to code-exploration skill to handle large
codebases incrementally. Could chunk analysis by directory.

## Context

- Project: knowledge-assistant-dev
- Codebase size: 15,000+ files
- Timeout setting: 300 seconds
```

### Not So Good Example:

```markdown
# Issue: Research agent doesn't work

**Layer**: L1
**Component**: research-agent
**Severity**: high

## Description

The research agent doesn't work properly.

## Impact

Can't use it.
```

## Integration with Upper Layers

### L0 (SEARCH-R) Integration

Feedback to L0 will be:
- Reviewed by methodology maintainers
- Incorporated into methodology updates
- Shared with other projects using SEARCH-R

### L1 (agent-team-research) Integration

Feedback to L1 will be:
- Used to improve research agent
- Considered for new skills
- Applied to template updates

### L2 (AgentTeam-Template) Integration

Feedback to L2 will be:
- Used to improve PM agent
- Considered for template enhancements
- Applied to workflow optimizations

## Contribution Process

If you want to contribute directly:

1. **Fork the target repository**
   - L0: SEARCH-R
   - L1: agent-team-research
   - L2: AgentTeam-Template

2. **Make your improvements**
   - Follow the repository's contribution guidelines
   - Write tests if applicable
   - Update documentation

3. **Submit Pull Request**
   - Reference feedback file if exists
   - Explain changes clearly
   - Respond to review comments

## Related

- [Dependencies Documentation](../dependencies/README.md)
- [Migration Work Log](../../migration-work/MIGRATION-LOG.md)

---

**Maintainer**: Migration Agent  
**Created**: 2026-03-08  
**Version**: 1.0
