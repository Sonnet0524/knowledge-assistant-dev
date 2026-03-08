# Research Content Migration Notice

## Important Notice

The research content previously in this directory has been **migrated** to L1 (agent-team-research) as part of the multi-repository architecture adjustment.

## Migration Details

**Migration Date**: 2026-03-08  
**Destination**: L1 agent-team-research  
**Location**: `/Users/sonnet/opencode/agent-team-research/migration-archive/from-knowledge-assistant-dev/`

## What Was Migrated

### 1. agents/research/
- Old Research Agent definition
- State memory (CATCH_UP.md)
- Essential guides
- Research guides

**New Location**: `.agent-team/template/.agent-team/research/migration-archive/from-knowledge-assistant-dev/agents-research/`

### 2. docs/research/
- Research topic directories
- Research log (24.7KB)
- Research documentation

**New Location**: `.agent-team/template/.agent-team/research/migration-archive/from-knowledge-assistant-dev/docs-research/`

### 3. practice/knowledge-base/experiences/research/
- Research experience records

**New Location**: `.agent-team/template/.agent-team/research/migration-archive/from-knowledge-assistant-dev/experiences-research/`

## Why the Migration

1. **Clear Responsibility**: L1 is responsible for research capabilities
2. **Reusability**: Research content can be shared across multiple L3 projects
3. **Better Architecture**: L1's new research-agent is designed for the L1 role

## How to Access

### Via Symbolic Links

```bash
# Access migrated agents/research/
cat .agent-team/template/.agent-team/research/migration-archive/from-knowledge-assistant-dev/agents-research/AGENTS.md

# Access migrated docs/research/
cat .agent-team/template/.agent-team/research/migration-archive/from-knowledge-assistant-dev/docs-research/research-log.md

# Access migrated experiences/
cat .agent-team/template/.agent-team/research/migration-archive/from-knowledge-assistant-dev/experiences-research/README.md
```

### Via Direct Path

```bash
# Direct path to L1 repository
cd /Users/sonnet/opencode/agent-team-research/migration-archive/from-knowledge-assistant-dev/
```

## Using Current Research Capabilities

For active research work, use the new L1 Research Agent:

```bash
# New Research Agent definition
cat .agent-team/template/.agent-team/research/agents/research-agent/AGENTS.md

# Research skills
ls .agent-team/template/.agent-team/research/agents/research-agent/skills/
```

## Research Delegation Workflow

L3 now delegates research tasks to L1:

1. **Create Research Request** (through L2)
   - L2 PM Agent creates research request
   - Stored in L2's collaboration/research-requests/

2. **L1 Processes Request**
   - L1 Research Agent picks up request
   - Uses SEARCH-R methodology (L0)
   - Executes research using skills

3. **Results Delivered**
   - Research results returned to L3
   - Instance stored in L0's research-instances/

## Reference vs Active Use

- **Migrated Content**: For historical reference only
- **New Research Agent**: For active research work
- **L1 Skills**: For current research capabilities

## Related Documentation

- [Dependencies](../collaboration/dependencies/README.md)
- [Migration Log](../migration-work/MIGRATION-LOG.md)
- [Final Report](../migration-work/FINAL-REPORT.md)

## Questions?

If you need to:
- Access old research content: See migrated files in L1
- Conduct new research: Use L1 Research Agent
- Understand migration: Check migration-work/ documentation

---

**Migration Date**: 2026-03-08  
**Migrated By**: Migration Agent  
**Status**: Complete
