# AI Frontiers Daily Challenge

Separate Hermes mode inside AI Frontiers Architecture Lab. Does **not** modify the Architecture Lab `aifa-send` job or other project crons.

**Tweet channel** = PosterGen’s configured WhatsApp tweet group (same as ArchitectureContentGen). It is **not** direct publishing to X.

## Roles

| Host | Responsibility |
|---|---|
| **Mac Mini** | Schedule, own SQLite (`~/.hermes/state/aifa-daily-challenge.db`), originality history, Hermes send to tweet channel |
| **Mac Studio** | SharedRoute model calls, 9-candidate create/review, codegen, tests, poster SVG/PNG |

## One-time setup

### Studio

```bash
cd /Users/aiserver/Documents/Workspace/AIFrontiersArchitectureLab
./scripts/install_hermes_daily_challenge.sh
```

### Mac Mini

```bash
# 1) Local checkout for SQLite coordinator (required)
git clone <this-repo> ~/AIFrontiersArchitectureLab
cd ~/AIFrontiersArchitectureLab
python3.12 -m venv .venv
.venv/bin/pip install -r requirements.txt

# 2) SSH host `studio` must work (BatchMode)

# 3) Install Mini wrappers
AIFA_DC_ROOT=$HOME/AIFrontiersArchitectureLab \
  ./scripts/install_hermes_daily_challenge_mini.sh

# 4) Optional Hermes cron (07:15 America/Los_Angeles)
AIFA_DC_ACTIVATE_CRON=1 AIFA_DC_CRON="15 7 * * *" \
  ./scripts/install_hermes_daily_challenge_mini.sh
```

## Commands to run on Mac Mini

```bash
# Validate Studio generation without publishing
~/.hermes/scripts/aifa-daily-challenge-dry-run.sh

# Full daily job: generate on Studio → ingest Mini DB → tweet channel deliver
~/.hermes/scripts/aifa-daily-challenge-run.sh

# Generate only (no deliver)
~/.hermes/scripts/aifa-daily-challenge-generate.sh

# Deliver a ready edition only
~/.hermes/scripts/aifa-daily-challenge-deliver.sh

# Status / doctor
~/.hermes/scripts/aifa-daily-challenge-status.sh
~/.hermes/scripts/aifa-daily-challenge-doctor.sh
```

## Commands on Studio (debug)

```bash
python -m app.main daily-challenge dry-run
python -m app.main daily-challenge generate --mode live
python -m app.main daily-challenge contract
python -m app.main daily-challenge deliver
python -m app.main daily-challenge calibrate
python -m app.main daily-challenge doctor
```

## What an edition contains

1. Specific engineering problem (not a topic blurb)
2. Scenario + explicit constraints (hypothetical labeled)
3. Architectural challenge question
4. Proposed solution + trade-offs
5. 4–6 box poster (SVG + PNG)
6. Focused GitHub/implementation slice + tests
7. README with Mermaid
8. Channel post: `AI Frontiers Daily Challenge #N`

## Reliability notes

- Unique `(series_id, edition_date)` reservation in SQLite
- Delivery queue with claim / ack / **unknown** (no blind repost after timeout)
- Never invents repository links
- Originality: normalized hash + structured overlap + hashed embedding similarity (calibrate via `calibrate`)
- Architecture Lab jobs remain untouched
