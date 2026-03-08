# .agent-team Directory

This directory contains links to upper layer repositories.

## Structure

```
.agent-team/
├── template -> ../AgentTeam-Template    # Link to L2 (AgentTeam-Template)
└── README.md                            # This file
```

## Purpose

Since Git submodules with local file paths have security restrictions,
we use symbolic links to establish dependencies.

## Usage

### Access L2 (AgentTeam-Template) Resources

```bash
# Use PM Agent
cat .agent-team/template/agents/pm/AGENTS.md

# Access team templates
ls .agent-team/template/agents/_templates/

# View collaboration framework
ls .agent-team/template/collaboration/

# Use research delegation
cat .agent-team/template/framework/skills/collaboration/research-delegation.md
```

### Project Management Workflow

```bash
# Access PM Agent capabilities
cat .agent-team/template/agents/pm/CATCH_UP.md

# Create project tasks
# Task files stored in local tasks/ directory
# Not in .agent-team/template/tasks/
```

### Research Delegation

Through L2's research delegation:
```bash
# L2 -> L1 -> L0 chain
.agent-team/template/collaboration/research-requests/
  -> L1 agent picks up
  -> L1 uses SEARCH-R methodology
```

## Indirect Access

L3 can indirectly access L0 and L1 through L2:
```bash
# L0 through L2
.agent-team/template/.agent-team/search-r/

# L1 through L2
.agent-team/template/.agent-team/research/
```

## Platform Compatibility

### macOS/Linux
Symbolic links work natively.

### Windows
Requires:
- Administrator privileges, or
- Developer Mode enabled

Alternative for Windows:
```cmd
# Use junction instead
mklink /J .agent-team\template ..\AgentTeam-Template
```

## Future Migration

When repositories are pushed to GitHub:
```bash
# Remove symbolic link
rm .agent-team/template

# Add proper Git submodule
git submodule add https://github.com/{org}/AgentTeam-Template.git .agent-team/template
```

## Dependency Verification

Verify links work correctly:
```bash
# Test L2 access
cat .agent-team/template/opencode.json

# Test indirect L1 access
cat .agent-team/template/.agent-team/research/opencode.json

# Test indirect L0 access
cat .agent-team/template/.agent-team/search-r/opencode.json
```

## Configuration Reference

L3 depends on:
- L2: AgentTeam-Template (direct link)
- L1: agent-team-research (through L2)
- L0: SEARCH-R (through L2)

See: `collaboration/dependencies/README.md` for details.

## Related

- L2 Repository: AgentTeam-Template (../AgentTeam-Template)
- Dependencies Documentation: ../collaboration/dependencies/README.md
- Feedback Documentation: ../collaboration/feedback/README.md

---

**Created**: 2026-03-08
**Purpose**: L2 dependency for L3
