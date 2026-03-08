# Dependencies Documentation

This directory contains documentation about dependencies on L0, L1, and L2 repositories.

## Dependency Structure

```
L3 (knowledge-assistant-dev) - 当前项目
    ├── Depends on L2 (AgentTeam-Template)
    │   ├── PM Agent and team templates
    │   ├── Management framework
    │   └── Workflow skills
    │
    ├── Depends on L1 (agent-team-research)
    │   ├── Research Agent capabilities
    │   ├── Research templates
    │   └── Research instance management
    │
    └── Depends on L0 (SEARCH-R)
        ├── SEARCH-R methodology
        ├── Research frameworks
        └── Theory foundations
```

## L2 Dependency: AgentTeam-Template

### Submodule Integration (Planned)

**Path**: `.agent-team/template` (to be added)

**Purpose**:
- Access PM Agent for project management
- Use team templates for agent creation
- Apply workflow skills

**Usage**:
```yaml
# PM Agent access
pm_agent:
  source: .agent-team/template/agents/pm
  
# Team templates
templates:
  source: .agent-team/template/agents/_templates
```

### What L2 Provides

1. **PM Agent**
   - Project planning and coordination
   - Team management
   - Task tracking

2. **Team Templates**
   - Core Team template
   - AI Team template
   - Test Team template
   - Integration Team template
   - Research Team template

3. **Management Framework**
   - Status tracking
   - Report generation
   - Knowledge base structure

## L1 Dependency: agent-team-research

### Submodule Integration (Planned)

**Path**: `.agent-team/research` (to be added)

**Purpose**:
- Delegate research tasks to research agent
- Access research templates and skills
- Receive research results

**Usage**:
```yaml
# Research delegation
research:
  agent: .agent-team/research/agents/research-agent
  skills:
    - web-search
    - document-analysis
    - code-exploration
    - knowledge-synthesis
```

### Research Delegation Workflow

1. **Create Research Request**
   ```
   collaboration/research-requests/{request-id}.json
   ```
   (This directory would be in L2's collaboration space)

2. **L1 Agent Processes**
   - Receives request
   - Executes research
   - Stores results in L0 instances

3. **Receive Results**
   - Research reports
   - Decision support
   - Implementation guides

### Current Research Content Migration

**Status**: In Progress

Research content currently in this project will be migrated to L1:
- `agents/research/` → L1's research agent space
- `docs/research/` → L1's knowledge base
- `practice/knowledge-base/experiences/research/` → L1's instances

After migration, this project will:
- Delegate research tasks to L1
- Use L1's research capabilities
- Focus on business implementation

## L0 Dependency: SEARCH-R

### Methodology Reference

**Path**: `../SEARCH-R` (relative path)

**Purpose**:
- Understand research methodology
- Follow research best practices
- Access theory frameworks

**Usage**:
```yaml
# Methodology reference
methodology:
  source: ../SEARCH-R/methodology
  cycle: SEARCH-R-cycle.md
  depth: research-depth.md
```

### Research Instances

When delegating research to L1, instances stored in L0:
```
../SEARCH-R/research-instances/knowledge-assistant-dev/
```

## Integration Benefits

### 1. Clear Responsibility Separation

**L3 (This Project) - Focus**:
- Business logic implementation
- Feature development
- Testing and deployment

**L2 (AgentTeam-Template) - Provides**:
- Project management
- Team coordination
- Process framework

**L1 (agent-team-research) - Provides**:
- Research capabilities
- Knowledge synthesis
- Technical evaluation

**L0 (SEARCH-R) - Provides**:
- Methodology foundation
- Theory frameworks
- Research standards

### 2. Reusable Capabilities

- Multiple L3 projects can use same L1 research agent
- Research knowledge shared across projects
- Avoid duplication of research efforts

### 3. Standardized Workflows

- Common methodology (SEARCH-R)
- Standard research depth levels
- Consistent documentation formats

## Migration Status

### Current Phase: Architecture Adjustment

- [x] L1 repository created
- [x] L0 configuration updated
- [x] L2 configuration updated
- [x] L3 configuration updated (this project)
- [ ] Submodule dependencies added
- [ ] Research content migrated
- [ ] Validation completed

### Research Content to Migrate

1. **agents/research/**
   - AGENTS.md
   - Research guides
   - Session logs

2. **docs/research/**
   - Research logs
   - Research reports

3. **practice/knowledge-base/experiences/research/**
   - Research experiences
   - Methodology notes

## Next Steps

1. Add L2 and L1 as submodules
2. Migrate research content to L1
3. Update agent configurations
4. Test collaboration workflows
5. Document lessons learned

## Related Documentation

- [Feedback to L0-L2](../feedback/README.md)
- [Migration Work Log](../../migration-work/MIGRATION-LOG.md)
- [Project README](../../README.md)

---

**Maintainer**: Migration Agent  
**Created**: 2026-03-08  
**Version**: 1.0
