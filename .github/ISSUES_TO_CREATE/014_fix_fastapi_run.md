---
title: "ENHANCEMENT: Add run instructions to FastAPI README"
labels: ["documentation", "good first issue"]
---

## Issue

FastAPI folder lacks clear instructions on how to run the API.

## Current State

`fastapi/README.md` exists but doesn't clearly explain:
- How to install dependencies
- How to start the server
- What endpoints are available
- How to test the API

## Expected

Add clear run instructions:

```markdown
## Quick Start

### 1. Install dependencies
```bash
pip install fastapi uvicorn
```

### 2. Start the server
```bash
cd fastapi
uvicorn main:app --reload
```

### 3. Open in browser
- API: http://127.0.0.1:8000
- Docs: http://127.0.0.1:8000/docs
- Interactive: http://127.0.0.1:8000/redoc

### 4. Test endpoints
```bash
# Get all campaigns
curl http://127.0.0.1:8000/campaigns

# Create a campaign
curl -X POST http://127.0.0.1:8000/campaigns \
  -H "Content-Type: application/json" \
  -d '{"name": "Test", "due_date": "2026-12-31"}'
```
```

## Files to Update
- `fastapi/README.md`
