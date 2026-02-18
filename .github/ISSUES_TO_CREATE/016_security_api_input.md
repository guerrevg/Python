---
title: "SECURITY: Add input validation to API endpoints"
labels: ["security", "enhancement", "priority: high"]
---

## Issue

API endpoints accept any input without validation, which could lead to security issues.

## Problems

### FastAPI (`fastapi/main.py`)
```python
class CampaignCreate(BaseModel):
    name: str  # No length limit
    due_date: datetime
```

### Flask (`rest_api/main.py`)
```python
data = request.get_json()
new_destination = Destination(
    destination=data["destination"],  # No validation
    country=data["country"],
    rating=data["rating"]
)
```

## Risks

- SQL injection (Flask + SQLAlchemy)
- XSS attacks
- Data integrity issues
- No input sanitization

## Fix

### FastAPI - Add Pydantic validation
```python
class CampaignCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    due_date: datetime = Field(..., description="Campaign due date")
    
    @field_validator('name')
    @classmethod
    def name_alphanumeric(cls, v):
        if not v.replace(' ', '').isalnum():
            raise ValueError('Name must be alphanumeric')
        return v
```

### Flask - Add manual validation
```python
@app.route("/destinations", methods=["POST"])
def add_destination():
    data = request.get_json()
    
    # Validate
    if not data.get('destination') or len(data['destination']) > 100:
        return jsonify({"error": "Invalid destination"}), 400
    
    if not isinstance(data.get('rating'), (int, float)) or not 0 <= data['rating'] <= 5:
        return jsonify({"error": "Rating must be 0-5"}), 400
    
    # Then create
    new_destination = Destination(...)
```

## Files to Update
- `fastapi/main.py`
- `rest_api/main.py`
