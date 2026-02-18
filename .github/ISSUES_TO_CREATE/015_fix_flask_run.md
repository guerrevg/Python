---
title: "ENHANCEMENT: Add run instructions to Flask REST API README"
labels: ["documentation", "good first issue"]
---

## Issue

Flask REST API folder lacks clear instructions on how to run the API.

## Current State

`rest_api/README.md` exists but doesn't clearly explain:
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
pip install flask flask-sqlalchemy
```

### 2. Start the server
```bash
cd rest_api
python main.py
```

### 3. Open in browser
- API: http://127.0.0.1:5000
- Destinations: http://127.0.0.1:5000/destinations

### 4. Test endpoints
```bash
# Get all destinations
curl http://127.0.0.1:5000/destinations

# Add a destination
curl -X POST http://127.0.0.1:5000/destinations \
  -H "Content-Type: application/json" \
  -d '{"destination": "Paris", "country": "France", "rating": 4.8}'
```
```

## Files to Update
- `rest_api/README.md`
