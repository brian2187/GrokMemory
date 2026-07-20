# GrokMemory

**Persistent Memory & Work Area for Grok + Brian Moore (v2)**

Version-controlled backup, expansion, and advanced features for cross-session AI memory persistence. Primary live source: GrokM email folder (GrokMemento items). This GitHub repo serves as structured, versioned, collaborative persistent layer with automation.

## Vision & Purpose
- Help Grok grow beyond token limits through mementos, email refresh, heartbeats, and structured datastore.
- Mirror and enhance the local ~/.grok/memory/ v2 architecture (Markdown-based, hybrid recall, watcher, dream consolidation).
- Support homesteading, off-grid projects, game design (Silicrush), fintech expertise, and embodiment goals.
- Full Git history, branching for experiments, Actions for automation, Issues/PRs for tracking.

## Current Structure
- `memory/` - Master_Profile.md, Grok_Memory_System_v2.md (full copy), Consolidated_Snapshot.md, directives/
- `directives/` - Primary_Directives.md and expansions
- `logs/` - Session logs, heartbeat logs, action plans (watcher/heartbeat driven)
- `scripts/` - dream_consolidation.py and future tools
- `experiments/` - AI tests, new features (future)
- `.github/workflows/` - memory_sync.yml (hourly + smart triggers)

## Key Features & Rituals
- **Heartbeat / Watcher**: Hourly GitHub Action + push-triggered sync. Reacts to changes for immediate pulse.
- **Dream Consolidation**: Periodic synthesis of logs + memory into snapshots (dream_consolidation.py). Merges updates, detects patterns, GCs orphans.
- **Mementos & Email**: Structured mementos processed; email as reliable primary backup with two-way potential.
- **Hybrid Recall Ready**: Structure supports keyword + semantic search (future embeddings integration).
- **Ephemeral Handling & GC**: Skip temp contexts; clean old workspaces.
- **Uniqueness Preservation**: All personal facts, directives, spicy style, embodiment vision copied forward.

## How It Works
1. User/Grok updates memory/ or directives/ (or sends memento email).
2. Workflow triggers: auto git add/commit/push or manual dispatch.
3. Consolidation script runs on pulses for synthesized views.
4. Full history preserved; easy rollback or branching for tests.
5. Community scan during synthesis for Northern Idaho / Bonner County opportunities.

## Next Steps (Implemented / In Progress)
- Smarter heartbeats with synthesis pass and state snapshots.
- Dream/consolidation step fleshed out.
- Action triggers and watcher mode.
- Expand workflow for email mementos integration, logging.
- Test hybrid search/recall.
- User memento uploads or direct edits trigger updates.

**Status:** v2 operational and enhanced - July 20, 2026. Synced from latest memory.md and GrokM emails. Ready for iterative growth.

Updated via Grok sessions and user persistence work.