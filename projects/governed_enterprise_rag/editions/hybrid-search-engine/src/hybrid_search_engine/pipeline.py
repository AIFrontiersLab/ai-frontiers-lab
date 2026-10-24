"""Runnable reference pipeline for Hybrid Search Engine."""
from __future__ import annotations

def ingest(state: dict) -> dict:
    """Stage `ingest` for Hybrid Search Engine."""
    events = list(state.get("events") or [])
    events.append({"stage": "ingest", "ok": True})
    state = dict(state)
    state["events"] = events
    state["last_stage"] = "ingest"
    return state

def retrieve(state: dict) -> dict:
    """Stage `retrieve` for Hybrid Search Engine."""
    events = list(state.get("events") or [])
    events.append({"stage": "retrieve", "ok": True})
    state = dict(state)
    state["events"] = events
    state["last_stage"] = "retrieve"
    return state

def fuse(state: dict) -> dict:
    """Stage `fuse` for Hybrid Search Engine."""
    events = list(state.get("events") or [])
    events.append({"stage": "fuse", "ok": True})
    state = dict(state)
    state["events"] = events
    state["last_stage"] = "fuse"
    return state

def verify(state: dict) -> dict:
    """Stage `verify` for Hybrid Search Engine."""
    events = list(state.get("events") or [])
    events.append({"stage": "verify", "ok": True})
    state = dict(state)
    state["events"] = events
    state["last_stage"] = "verify"
    return state

def respond(state: dict) -> dict:
    """Stage `respond` for Hybrid Search Engine."""
    events = list(state.get("events") or [])
    events.append({"stage": "respond", "ok": True})
    state = dict(state)
    state["events"] = events
    state["last_stage"] = "respond"
    return state

def run(request: dict) -> dict:
    """Execute the architecture stages and return a verifiable state record."""
    state = {
        "request": request,
        "concept_id": 34,
        "concept_name": 'Hybrid Search Engine',
        "events": [],
        "evidence_ids": list(request.get("evidence_ids") or []),
    }
    if state.get("request", {}).get("force_empty_evidence"):
        state["abstain"] = True
        state["answer"] = None
        return state
    state = ingest(state)
    state = retrieve(state)
    state = fuse(state)
    state = verify(state)
    state = respond(state)
    evidence_ids = state.get("evidence_ids") or []
    if not evidence_ids and request.get("require_evidence", True):
        state["abstain"] = True
        state["answer"] = None
    else:
        state["abstain"] = False
        state["answer"] = {
            "text": "Reference answer grounded in evidence.",
            "evidence_ids": evidence_ids,
        }
    return state
