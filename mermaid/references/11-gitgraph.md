# GitGraph (Diagrama Git) - Mermaid

> Documentacion oficial: https://mermaid.js.org/syntax/gitgraph.html

Los diagramas GitGraph representan visualmente commits, branches y merges de repositorios Git.

## Sintaxis Basica

```mermaid
gitGraph
    commit
    commit
    branch develop
    checkout develop
    commit
    commit
    checkout main
    merge develop
    commit
```

## Estructura General

```
gitGraph [orientacion]:
    commit [opciones]
    branch nombre
    checkout nombre
    merge nombre [opciones]
    cherry-pick id:"id"
```

## Comandos Principales

### commit

Crea un nuevo commit en la rama actual:

```mermaid
gitGraph
    commit
    commit
    commit
```

### branch

Crea una nueva rama desde el punto actual:

```mermaid
gitGraph
    commit
    branch feature
    commit
    branch hotfix
    commit
```

### checkout

Cambia a una rama existente:

```mermaid
gitGraph
    commit
    branch develop
    checkout develop
    commit
    checkout main
    commit
```

### merge

Fusiona una rama en la rama actual:

```mermaid
gitGraph
    commit
    branch feature
    checkout feature
    commit
    commit
    checkout main
    merge feature
    commit
```

### cherry-pick

Aplica un commit especifico de otra rama:

```mermaid
gitGraph
    commit id: "inicial"
    branch develop
    commit id: "feat-1"
    commit id: "feat-2"
    checkout main
    cherry-pick id: "feat-1"
    commit
```

## Opciones de Commit

### ID Personalizado

```mermaid
gitGraph
    commit id: "inicio"
    commit id: "feature-1"
    commit id: "release-v1"
```

### Tipo de Commit

```mermaid
gitGraph
    commit id: "normal"
    commit id: "highlight" type: HIGHLIGHT
    commit id: "reverse" type: REVERSE
```

| Tipo | Descripcion | Apariencia |
|------|-------------|------------|
| `NORMAL` | Commit normal (default) | Circulo solido |
| `HIGHLIGHT` | Commit resaltado | Rectangulo |
| `REVERSE` | Commit revertido | Circulo cruzado |

### Tags

```mermaid
gitGraph
    commit id: "inicio"
    commit id: "feature"
    commit id: "release" tag: "v1.0.0"
    commit id: "hotfix" tag: "v1.0.1"
```

### Mensaje de Commit

```mermaid
gitGraph
    commit id: "1" msg: "Initial commit"
    commit id: "2" msg: "Add feature A"
    commit id: "3" msg: "Fix bug in feature A"
```

### Combinando Opciones

```mermaid
gitGraph
    commit id: "inicio" msg: "Initial commit"
    commit id: "feature" msg: "Add login" type: HIGHLIGHT
    commit id: "release" msg: "Release 1.0" tag: "v1.0.0" type: HIGHLIGHT
```

## Orientacion

### Left to Right (Default)

```mermaid
gitGraph LR:
    commit
    commit
    branch develop
    commit
    checkout main
    merge develop
```

### Top to Bottom

```mermaid
gitGraph TB:
    commit
    commit
    branch develop
    commit
    checkout main
    merge develop
```

### Bottom to Top

```mermaid
gitGraph BT:
    commit
    commit
    branch develop
    commit
    checkout main
    merge develop
```

## Flujos de Trabajo

### Git Flow

```mermaid
gitGraph
    commit id: "inicial"
    branch develop
    checkout develop
    commit id: "dev-1"
    
    branch feature/login
    checkout feature/login
    commit id: "login-1"
    commit id: "login-2"
    checkout develop
    merge feature/login
    
    branch feature/dashboard
    checkout feature/dashboard
    commit id: "dash-1"
    checkout develop
    merge feature/dashboard
    
    branch release/1.0
    checkout release/1.0
    commit id: "prep-release"
    checkout main
    merge release/1.0 tag: "v1.0.0"
    checkout develop
    merge release/1.0
```

### GitHub Flow

```mermaid
gitGraph
    commit id: "init"
    commit id: "base"
    
    branch feature-auth
    checkout feature-auth
    commit id: "auth-1"
    commit id: "auth-2"
    checkout main
    merge feature-auth tag: "merge-1"
    
    branch fix-bug
    checkout fix-bug
    commit id: "fix-1"
    checkout main
    merge fix-bug
    
    branch feature-api
    checkout feature-api
    commit id: "api-1"
    commit id: "api-2"
    checkout main
    merge feature-api tag: "v1.1.0"
```

### Trunk Based Development

```mermaid
gitGraph
    commit id: "init"
    commit id: "feat-1" type: HIGHLIGHT
    commit id: "feat-2"
    commit id: "fix-1" type: REVERSE
    commit id: "feat-3"
    commit id: "release" tag: "v1.0.0" type: HIGHLIGHT
    commit id: "feat-4"
    commit id: "hotfix" type: REVERSE
    commit id: "release-2" tag: "v1.0.1"
```

### Hotfix Flow

```mermaid
gitGraph
    commit id: "v1.0" tag: "v1.0.0"
    branch develop
    checkout develop
    commit id: "dev-1"
    commit id: "dev-2"
    
    checkout main
    branch hotfix/critical
    checkout hotfix/critical
    commit id: "fix" type: REVERSE
    checkout main
    merge hotfix/critical tag: "v1.0.1"
    
    checkout develop
    merge hotfix/critical
    commit id: "dev-3"
```

## Ejemplos por Escenario

### Release con Bugfixes

```mermaid
gitGraph
    commit id: "inicial"
    branch develop
    checkout develop
    commit id: "feat-A"
    commit id: "feat-B"
    
    branch release/2.0
    checkout release/2.0
    commit id: "version-bump"
    commit id: "bugfix-1" type: REVERSE
    commit id: "bugfix-2" type: REVERSE
    
    checkout main
    merge release/2.0 tag: "v2.0.0" type: HIGHLIGHT
    
    checkout develop
    merge release/2.0
```

### Feature Branch con Conflictos

```mermaid
gitGraph
    commit id: "base"
    branch feature-A
    checkout feature-A
    commit id: "A-1"
    
    checkout main
    commit id: "main-1"
    commit id: "main-2"
    
    checkout feature-A
    commit id: "A-2"
    commit id: "merge-main" type: HIGHLIGHT
    commit id: "A-3"
    
    checkout main
    merge feature-A
```

### Multiples Features en Paralelo

```mermaid
gitGraph
    commit id: "init"
    
    branch feature-1
    branch feature-2
    branch feature-3
    
    checkout feature-1
    commit id: "f1-work"
    
    checkout feature-2
    commit id: "f2-work"
    commit id: "f2-more"
    
    checkout feature-3
    commit id: "f3-work"
    
    checkout main
    merge feature-2
    merge feature-1
    merge feature-3 tag: "v1.0.0"
```

## Configuracion

### Mostrar/Ocultar Elementos

```mermaid
%%{init: { 'gitGraph': {'showBranches': true, 'showCommitLabel': true}} }%%
gitGraph
    commit id: "1"
    branch develop
    commit id: "2"
    checkout main
    merge develop
```

### Personalizar Apariencia

```mermaid
%%{init: { 'gitGraph': {
    'mainBranchName': 'master',
    'mainBranchOrder': 0
}} }%%
gitGraph
    commit
    branch feature
    commit
    checkout master
    merge feature
```

### Opciones de Configuracion

| Opcion | Descripcion | Default |
|--------|-------------|---------|
| `showBranches` | Mostrar nombres de ramas | true |
| `showCommitLabel` | Mostrar etiquetas de commits | true |
| `mainBranchName` | Nombre de rama principal | 'main' |
| `mainBranchOrder` | Orden de rama principal | 0 |
| `rotateCommitLabel` | Rotar etiquetas | true |
| `arrowMarkerAbsolute` | Flechas absolutas | false |

### Tema

```mermaid
%%{init: {'theme': 'dark'}}%%
gitGraph
    commit
    branch develop
    commit
    checkout main
    merge develop
```

### Personalizar Colores de Ramas

```mermaid
%%{init: { 'theme': 'base', 'themeVariables': {
    'git0': '#ff6b6b',
    'git1': '#4ecdc4',
    'git2': '#45b7d1',
    'git3': '#f9ca24',
    'gitBranchLabel0': '#ffffff',
    'gitBranchLabel1': '#ffffff',
    'gitBranchLabel2': '#ffffff'
}} }%%
gitGraph
    commit
    branch feature-a
    commit
    branch feature-b
    commit
    checkout main
    merge feature-a
    merge feature-b
```

## Variables de Tema

| Variable | Descripcion |
|----------|-------------|
| `git0` - `git7` | Colores de ramas (0=main) |
| `gitBranchLabel0` - `gitBranchLabel7` | Color texto etiquetas |
| `gitInv0` - `gitInv7` | Colores invertidos |
| `commitLabelColor` | Color etiquetas commit |
| `commitLabelBackground` | Fondo etiquetas commit |
| `commitLabelFontSize` | Tamano fuente etiquetas |
| `tagLabelColor` | Color etiquetas tag |
| `tagLabelBackground` | Fondo etiquetas tag |
| `tagLabelBorder` | Borde etiquetas tag |
| `tagLabelFontSize` | Tamano fuente tags |

## Resumen de Comandos

| Comando | Sintaxis | Descripcion |
|---------|----------|-------------|
| `commit` | `commit [id: "x"] [msg: "x"] [type: X] [tag: "x"]` | Crear commit |
| `branch` | `branch nombre` | Crear rama |
| `checkout` | `checkout nombre` | Cambiar a rama |
| `merge` | `merge nombre [id: "x"] [tag: "x"] [type: X]` | Fusionar rama |
| `cherry-pick` | `cherry-pick id: "x" [tag: "x"] [parent: "x"]` | Cherry-pick |

## Tips y Mejores Practicas

1. **IDs descriptivos**: Usar IDs que representen el cambio
2. **Tags para releases**: Marcar versiones importantes
3. **Tipos apropiados**: HIGHLIGHT para hitos, REVERSE para reverts
4. **Orientacion segun contexto**: TB para historiales largos, LR para flujos simples
5. **Colores consistentes**: Mantener convencion de colores por tipo de rama
6. **Simplificar**: No representar cada commit, solo los significativos
