# Last Signal

Single-player vehicle survival game for Windows PC (Unreal Engine 5.8, controller-first). Make one more desperate drive, bring home salvage, physically improve a battered car, and follow a missing partner's trail through a chain of safe garages.

**Status:** pre-production. The repository contains the design pack and an uncompiled C++ project scaffold. Nothing has been built or playtested yet. Next step: **M00 Preflight** on the Windows development PC.

## Layout

| Path | Contents |
| --- | --- |
| `CLAUDE.md`, `AGENTS.md` | Root instructions for Claude Code and Codex |
| `PROJECT_STATE.md` | Current task, verified behaviour and handoff — keep this current |
| `Docs/LastSignal/` | Design and production pack (start with `00_START_HERE.md`) |
| `Docs/LastSignal/tasks/` | Task cards M00–M22, worked in roadmap order |
| `Docs/LastSignal/data/` | `balance_seed.json` (tuning source of truth) and asset manifest |
| `Docs/LastSignal/BUILD_COMMANDS.md` | Verified local build commands — filled in during M00 |
| `LastSignal.uproject`, `Source/`, `Config/` | Minimal C++ project scaffold |
| `Scripts/Blender/` | Repeatable Blender batch scripts |
| `Scripts/Unreal/` | Editor Python tooling (validation scripts land in M00/M01) |

## Getting started on the dev PC

1. Install Git LFS, then clone: `git lfs install` followed by `git clone <repo-url>`.
2. Install UE 5.8 and the matching Visual Studio toolchain per Epic's docs. If the installed version string differs from `5.8`, right-click `LastSignal.uproject` → *Switch Unreal Engine version*.
3. Right-click `LastSignal.uproject` → *Generate Visual Studio project files*, then build `LastSignalEditor` (Development Editor, Win64).
4. Start Claude Code in the repo root and give it the M00 prompt from `Docs/LastSignal/PROMPTS.md`.
