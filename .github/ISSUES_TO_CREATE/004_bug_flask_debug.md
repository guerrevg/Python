---
title: "BUG: Flask debug mode enabled in production code"
labels: ["bug", "security", "priority: high"]
---

## Bug Description

The Flask REST API has debug mode enabled, which is a security risk.

## Problem

In `rest_api/main.py` (line 71):
```python
if __name__ == "__main__":
    app.run(debug=True)  # Security risk!
```

## Security Risk

Debug mode allows:
- Interactive code execution
- Detailed error exposure
- Should NEVER be in production

## Fix

Use environment variable:

```python
import os

if __name__ == "__main__":
    debug = os.environ.get("FLASK_DEBUG", "False").lower() == "true"
    app.run(debug=debug)
```

## Files
- `rest_api/main.py`

## Testing
```bash
cd rest_api
python main.py
# Should run with debug=False by default
```
