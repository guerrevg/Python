# ⚡ PERFORMANCE ISSUES - Priority: MEDIUM

---

## Issue #39: Inefficient Prime Checking Algorithm

### Title
[PERFORMANCE]: Optimize prime number checking algorithm

### Description

**What:** Prime checking uses O(n) algorithm instead of O(√n).

**Why it matters:** 
- Very slow for large numbers
- Teaches inefficient approach
- Unnecessary CPU usage

**Where:** `basics/03_control_flow/02_check_prime.py`, line 9

**Current behavior:**
```python
for i in range(2, int(num * 0.5) + 1):  # Checks up to n/2
    if((num % i) == 0):
        prime = False
        break
```

**Expected behavior:**
```python
import math

for i in range(2, int(math.sqrt(num)) + 1):  # Check only to √n
    if num % i == 0:
        return False
```

**Performance comparison:**
- For num=1000003 (prime):
  - Current: 500,000 iterations
  - Optimized: 1,000 iterations
  - **500x faster!**

**Suggested approach:**
```python
import math

def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    # Check using 6k±1 optimization
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
```

**Acceptance criteria:**
- [ ] Implement √n optimization
- [ ] Add early exit for even numbers
- [ ] Add docstring with complexity O(√n)
- [ ] Add performance comparison comment
- [ ] Test with large primes (>1M)

**Labels:** `performance`, `enhancement`, `good first issue`

---

## Issue #40: No Database Indexes in Flask API

### Title
[PERFORMANCE]: Add database indexes for frequently queried columns

### Description

**What:** Database tables have no indexes, causing full table scans.

**Why it matters:** 
- Queries slow down as data grows
- O(n) instead of O(log n) lookups
- Poor user experience

**Where:** `rest_api/main.py`, Destination model

**Current behavior:**
```python
class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Auto-indexed
    destination = db.Column(db.String(100), nullable=False)  # No index!
    country = db.Column(db.String(50), nullable=False)  # No index!
    rating = db.Column(db.Float, nullable=False)  # No index!
```

**Expected behavior:**
```python
class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(100), nullable=False, index=True)
    country = db.Column(db.String(50), nullable=False, index=True)
    rating = db.Column(db.Float, nullable=False, index=True)
    
    # Composite index for common queries
    __table_args__ = (
        db.Index('idx_country_rating', 'country', 'rating'),
    )
```

**Performance impact:**
- Without index: O(n) - scans all rows
- With index: O(log n) - binary search
- For 1M rows: 1,000,000 vs 20 operations

**Acceptance criteria:**
- [ ] Add index=True to searchable columns
- [ ] Add composite indexes for common queries
- [ ] Create migration script
- [ ] Test query performance before/after
- [ ] Document index strategy

**Labels:** `performance`, `database`, `priority: medium`

---

## Issue #41: N+1 Query Pattern in API

### Title
[PERFORMANCE]: Fix N+1 query pattern in list endpoints

### Description

**What:** List endpoints may trigger N+1 queries when serializing.

**Why it matters:** 
- Database overload
- Slow response times
- Doesn't scale

**Where:** `rest_api/main.py`, GET /destinations

**Current behavior:**
```python
@app.route("/destinations", methods=["GET"])
def get_destinations():
    destinations = Destination.query.all()  # 1 query
    return jsonify([destination.to_dict() for destination in destinations])
    # to_dict() might trigger additional queries!
```

**Suggested approach:**
```python
@app.route("/destinations", methods=["GET"])
def get_destinations():
    # Eager load all needed data
    destinations = Destination.query.all()
    
    # Use dictionary comprehension (faster than list comp)
    result = [
        {
            "id": d.id,
            "destination": d.destination,
            "country": d.country,
            "rating": d.rating
        }
        for d in destinations
    ]
    return jsonify(result)
```

For relationships:
```python
# Use joinedload for relationships
from sqlalchemy.orm import joinedload

destinations = Destination.query.options(
    joinedload(Destination.related_table)
).all()
```

**Acceptance criteria:**
- [ ] Audit all list endpoints
- [ ] Use eager loading for relationships
- [ ] Minimize queries in serialization
- [ ] Add query logging for debugging
- [ ] Test with EXPLAIN ANALYZE

**Labels:** `performance`, `database`, `priority: medium`

---

## Issue #42: No Caching Strategy

### Title
[PERFORMANCE]: Implement caching for frequently accessed data

### Description

**What:** No caching layer for read-heavy operations.

**Why it matters:** 
- Same data fetched repeatedly
- Unnecessary database load
- Slow response times

**Where:** Both API applications

**Suggested approach:**

For FastAPI with Redis:
```python
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

@app.get("/campaigns")
@cache(expire=60)  # Cache for 60 seconds
async def list_campaigns():
    return campaigns_db
```

For Flask with Flask-Caching:
```python
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'redis'})

@app.route("/destinations")
@cache.cached(timeout=60)
def get_destinations():
    destinations = Destination.query.all()
    return jsonify([d.to_dict() for d in destinations])
```

**Acceptance criteria:**
- [ ] Add Redis dependency
- [ ] Configure caching layer
- [ ] Cache GET endpoints (60s default)
- [ ] Invalidate cache on POST/PUT/DELETE
- [ ] Add cache headers to responses
- [ ] Document caching strategy

**Labels:** `performance`, `enhancement`, `priority: low`

---

## Issue #43: Inefficient File Reading

### Title
[PERFORMANCE]: Optimize file reading for large files

### Description

**What:** File handling examples read entire files into memory.

**Why it matters:** 
- Memory exhaustion with large files
- Slow for large datasets
- Doesn't scale

**Where:** `basics/07_file_handling/`

**Current behavior:**
```python
with open("large_file.txt", "r") as f:
    data = f.read()  # Loads entire file into memory!
```

**Suggested approach:**
```python
# Line by line (memory efficient)
with open("large_file.txt", "r") as f:
    for line in f:
        process(line)

# Or chunked reading
def read_in_chunks(file_path, chunk_size=8192):
    with open(file_path, "r") as f:
        while chunk := f.read(chunk_size):
            process(chunk)
```

**Acceptance criteria:**
- [ ] Update examples to use line-by-line reading
- [ ] Add chunked reading example
- [ ] Document memory implications
- [ ] Add benchmark comparing approaches
- [ ] Test with 1GB+ files

**Labels:** `performance`, `code quality`, `priority: low`

---

## Issue #44: No Connection Pooling

### Title
[PERFORMANCE]: Configure database connection pooling

### Description

**What:** Database connections created per-request without pooling.

**Why it matters:** 
- Connection overhead on every request
- Database resource exhaustion
- Slow response times

**Where:** `rest_api/main.py`

**Current behavior:**
```python
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///travel.db"
db = SQLAlchemy(app)
# Default pool settings may not be optimal
```

**Suggested approach:**
```python
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_size": 10,          # Number of connections to keep
    "pool_recycle": 3600,     # Recycle connections after 1 hour
    "pool_pre_ping": True,    # Verify connection before use
    "max_overflow": 20,       # Allow 20 extra connections
}
```

**Acceptance criteria:**
- [ ] Configure pool_size (10-20)
- [ ] Set pool_recycle (3600s)
- [ ] Enable pool_pre_ping
- [ ] Monitor connection usage
- [ ] Document pool tuning

**Labels:** `performance`, `database`, `priority: low`

---
