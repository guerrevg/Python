---
name: 🚀 Add Database Integration
about: Replace in-memory storage with real database
title: '[ENHANCEMENT] Add database support to FastAPI and Flask APIs'
labels: ['enhancement', 'advanced', 'feature']
assignees: ''
---

## 📋 Issue Description

Both APIs use in-memory storage:
- **FastAPI**: `campaigns_db: list[Campaign]`
- **Flask**: SQLite but no migrations

Data is lost on restart. Need proper database integration.

## 🔍 Current State

### FastAPI
```python
# In-memory storage (lost on restart)
campaigns_db: list[Campaign] = [...]
_next_id = 3
```

### Flask
```python
# SQLite but no migrations
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///travel.db"
```

## ✅ Tasks

### Option 1: SQLite with Migrations (Recommended)

#### FastAPI
- [ ] Add SQLAlchemy dependency
- [ ] Create models:
  ```python
  from sqlalchemy import Column, Integer, String, DateTime
  
  class Campaign(Base):
      __tablename__ = "campaigns"
      
      id = Column(Integer, primary_key=True)
      name = Column(String, nullable=False)
      due_date = Column(DateTime, nullable=False)
      created_at = Column(DateTime, default=datetime.now)
  ```

- [ ] Add Alembic migrations:
  ```bash
  alembic init alembic
  alembic revision --autogenerate -m "Initial"
  alembic upgrade head
  ```

- [ ] Update endpoints to use database
- [ ] Add connection pooling
- [ ] Add database session management

#### Flask
- [ ] Add Flask-Migrate
- [ ] Create initial migration
- [ ] Document migration commands
- [ ] Add seed data script

### Option 2: PostgreSQL (Production-Ready)

- [ ] Add PostgreSQL dependency
- [ ] Update connection strings
- [ ] Add environment variables for config
- [ ] Add Docker compose file
- [ ] Document setup

### Option 3: Multiple Database Support

- [ ] Support SQLite (development)
- [ ] Support PostgreSQL (production)
- [ ] Add database selector
- [ ] Document switching

## 📝 Implementation Example

```python
# Database session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./campaigns.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint with database
@app.post("/campaigns")
async def create_campaign(
    campaign: CampaignCreate,
    db: Session = Depends(get_db)
):
    db_campaign = Campaign(**campaign.dict())
    db.add(db_campaign)
    db.commit()
    db.refresh(db_campaign)
    return db_campaign
```

## 🎯 Why This Matters

- **Persistence**: Data survives restarts
- **Scalability**: Handle more data
- **Professionalism**: Production-ready
- **Learning**: Real-world patterns

## 💡 Additional Features

### Nice to Have
- [ ] Database backup script
- [ ] Seed data for testing
- [ ] Database admin interface
- [ ] Query optimization
- [ ] Index documentation

## ⚠️ Risk Assessment

**Medium Risk:**
- Database changes are permanent
- Need migration strategy
- Testing required

## 📝 Difficulty

**Advanced** - Requires database knowledge

## 🔗 Related

- API documentation: #24
- Testing: #20
- CI/CD: #25
