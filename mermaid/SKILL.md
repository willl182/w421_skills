---
name: mermaid
description: 'Create Mermaid diagrams from scratch or convert text descriptions to Mermaid syntax. Supports flowcharts, sequence diagrams, class diagrams, state diagrams, ER diagrams, Gantt charts, GitGraph, mindmaps, timelines, kanban boards, and architecture diagrams. Use when asked to create diagrams, visualize processes, document systems, or generate any Mermaid code. Triggers: "create a diagram", "flowchart for", "sequence diagram", "class diagram", "ER diagram", "Gantt chart", "git graph", "mindmap", "timeline", "kanban", "architecture diagram", "visualize", "diagram this".'
---

# Mermaid Diagrams

Create diagrams using Mermaid syntax. Reference detailed docs in `references/` for complex cases.

## Quick Reference

| Diagram | Keyword | Use For |
|---------|---------|---------|
| Flowchart | `flowchart` | Processes, decisions, workflows |
| Sequence | `sequenceDiagram` | API calls, interactions, protocols |
| Class | `classDiagram` | OOP design, data models |
| State | `stateDiagram-v2` | State machines, lifecycles |
| ER | `erDiagram` | Database schemas, relationships |
| Gantt | `gantt` | Project timelines, schedules |
| GitGraph | `gitGraph` | Git branching, versioning |
| Mindmap | `mindmap` | Brainstorming, hierarchies |
| Timeline | `timeline` | Chronologies, roadmaps |
| Kanban | `kanban` | Task boards, workflows |
| Architecture | `architecture-beta` | Infrastructure, cloud |

## Flowchart

```mermaid
flowchart LR
    A[Start] --> B{Decision}
    B -->|Yes| C[Action 1]
    B -->|No| D[Action 2]
    C --> E[End]
    D --> E
```

**Directions**: `TB` (top-bottom), `LR` (left-right), `BT`, `RL`

**Node Shapes**:
- `[text]` Rectangle
- `(text)` Rounded
- `{text}` Diamond
- `((text))` Circle
- `[(text)]` Database
- `{{text}}` Hexagon

**Links**: `-->` arrow, `---` line, `-.->` dashed, `==>` thick

For subgraphs, styling, icons: see `references/01-flowchart.md`

## Sequence Diagram

```mermaid
sequenceDiagram
    participant C as Client
    participant S as Server
    participant D as Database
    
    C->>S: HTTP Request
    activate S
    S->>D: Query
    D-->>S: Results
    S-->>C: Response
    deactivate S
```

**Arrows**: `->>` solid, `-->>` dashed, `-x` error, `-)` async

**Blocks**: `loop`, `alt/else`, `opt`, `par/and`, `critical/option`, `break`, `rect`

For activations, notes, boxes: see `references/02-sequence-diagram.md`

## Class Diagram

```mermaid
classDiagram
    class Animal {
        +String name
        +int age
        +makeSound()* void
    }
    class Dog {
        +String breed
        +bark() void
    }
    Animal <|-- Dog
```

**Visibility**: `+` public, `-` private, `#` protected, `~` package

**Relations**: `<|--` inheritance, `*--` composition, `o--` aggregation, `-->` association

For generics, namespaces, annotations: see `references/03-class-diagram.md`

## State Diagram

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Processing : start
    Processing --> Success : done
    Processing --> Error : fail
    Success --> [*]
    Error --> Idle : retry
```

**Special States**: `[*]` start/end, `<<choice>>`, `<<fork>>`, `<<join>>`

For composite states, concurrency, notes: see `references/04-state-diagram.md`

## Entity Relationship

```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ LINE_ITEM : contains
    CUSTOMER {
        int id PK
        string name
        string email UK
    }
```

**Cardinality**: `||` one, `o|` zero-one, `}|` one-many, `}o` zero-many

**Keys**: `PK` primary, `FK` foreign, `UK` unique

For relationships, aliases: see `references/05-entity-relationship-diagram.md`

## Gantt Chart

```mermaid
gantt
    title Project Timeline
    dateFormat YYYY-MM-DD
    
    section Phase 1
        Task A :done, a1, 2024-01-01, 5d
        Task B :active, a2, after a1, 3d
    
    section Phase 2
        Task C :crit, b1, after a2, 4d
        Milestone :milestone, m1, after b1, 0d
```

**States**: `done`, `active`, `crit`

**Dependencies**: `after taskId`

For date formats, excludes, vertical markers: see `references/07-gantt.md`

## GitGraph

```mermaid
gitGraph
    commit id: "init"
    branch develop
    checkout develop
    commit id: "feat-1"
    checkout main
    merge develop tag: "v1.0.0"
    commit id: "hotfix" type: REVERSE
```

**Commands**: `commit`, `branch`, `checkout`, `merge`, `cherry-pick`

**Types**: `NORMAL`, `HIGHLIGHT`, `REVERSE`

For orientations, themes: see `references/11-gitgraph.md`

## Mindmap

```mermaid
mindmap
    root((Project))
        Planning
            Requirements
            Timeline
        Development
            Frontend
            Backend
        Testing
            Unit
            E2E
```

**Shapes**: `(())` circle, `[]` square, `()` rounded, `))((` bang, `)(` cloud

For icons, classes: see `references/13-mindmap.md`

## Timeline

```mermaid
timeline
    title Product Roadmap
    section 2024 Q1
        January : Planning
        March : Beta Launch
    section 2024 Q2
        April : Public Release
        June : v2.0
```

For sections, multiple events: see `references/14-timeline.md`

## Kanban

```mermaid
kanban
    todo[To Do]
        task1[Design mockups]
        task2[Write tests]
    inprogress[In Progress]
        task3[Implement API]
    done[Done]
        task4[Setup CI/CD]
```

For metadata, ticket URLs: see `references/20-kanban.md`

## Architecture

```mermaid
architecture-beta
    group api[API Layer]
    
    service lb(cloud)[Load Balancer] in api
    service app(server)[App Server] in api
    service db(database)[Database] in api
    
    lb:R -- L:app
    app:R -- L:db
```

**Icons**: `server`, `database`, `disk`, `internet`, `cloud`

**Positions**: `T` top, `B` bottom, `L` left, `R` right

For groups, junctions: see `references/21-architecture.md`

## Configuration

Add frontmatter for themes and settings:

```mermaid
---
config:
  theme: forest
  look: handDrawn
---
flowchart LR
    A --> B
```

**Themes**: `default`, `forest`, `dark`, `neutral`, `base`

## Preview

After creating a diagram, use `scripts/preview.py` to render and preview:

```bash
python scripts/preview.py diagram.mmd
```

## Workflow

1. Identify diagram type from user request
2. Write Mermaid code with proper syntax
3. For complex cases, consult `references/` docs
4. Generate preview if requested
