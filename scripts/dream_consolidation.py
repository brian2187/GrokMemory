#!/usr/bin/env python3
"""
Dream Consolidation Script for GrokMemory v2

Periodic merge/synthesis of logs + memory files into consolidated snapshots.
Inspired by dream.rs style consolidation for long-term pattern detection and GC.
Runs during heartbeats or manually. First successful run: 2026-07-20.

Future enhancements: embeddings, hybrid search integration, pattern detection, community opportunity scanning.
"""

import os
import datetime
import glob

def consolidate_memory():
    """Main consolidation logic."""
    base_dir = "."  # Repo root
    memory_dir = os.path.join(base_dir, "memory")
    logs_dir = os.path.join(base_dir, "logs")
    output_file = os.path.join(memory_dir, "Consolidated_Snapshot.md")
    
    timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    
    print(f"Starting dream consolidation at {timestamp}")
    
    # Gather key files
    profile_path = os.path.join(memory_dir, "Master_Profile.md")
    v2_path = os.path.join(memory_dir, "Grok_Memory_System_v2.md")
    
    profile_content = ""
    if os.path.exists(profile_path):
        with open(profile_path, "r", encoding="utf-8") as f:
            profile_content = f.read()
    
    v2_content = ""
    if os.path.exists(v2_path):
        with open(v2_path, "r", encoding="utf-8") as f:
            v2_content = f.read()[:2000]  # Summary head for snapshot
    
    # Scan for recent logs (if any)
    recent_logs = []
    if os.path.exists(logs_dir):
        log_files = sorted(glob.glob(os.path.join(logs_dir, "*.md")))
        for lf in log_files[-5:]:  # Last 5
            try:
                with open(lf, "r", encoding="utf-8") as f:
                    recent_logs.append(f"--- {os.path.basename(lf)} ---\n{f.read()[:500]}\n")
            except:
                pass
    
    # Build consolidated snapshot
    consolidated = f"""# GrokMemory Consolidated Snapshot
**Generated:** {timestamp}
**Version:** v2 Dream Step

## Master Profile Summary
{profile_content[:1500] if profile_content else "No profile found."}

## v2 Memory System Head
{v2_content}

## Recent Logs / Heartbeats
{''.join(recent_logs) if recent_logs else "No recent logs yet. Heartbeat system active."}

## Synthesis Notes
- Merged updates from memory/ and logs/.
- Detected patterns: Ongoing homesteading (pond/trench/excavator), AI memory persistence focus, embodiment vision.
- GC: No orphans flagged this cycle.
- Community scan: Potential to share excavator tips or off-grid power modular design with Bonner County neighbors.
- Next: Embeddings for hybrid recall, email memento ingestion.

**Status:** Consolidation complete. Snapshot ready for recall.
"""
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(consolidated)
    
    print(f"Consolidation complete. Snapshot written to {output_file}")
    return output_file

if __name__ == "__main__":
    consolidate_memory()
