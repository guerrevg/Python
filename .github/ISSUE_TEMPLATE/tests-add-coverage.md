---
name: 💯 Add Unit Tests
about: Create comprehensive test suite for all examples
title: '[TESTS] Add unit tests for all Python modules'
labels: ['tests', 'enhancement', 'advanced']
assignees: ''
---

## 📋 Issue Description

The project has **zero test coverage**. No automated tests exist for:
- 150+ Python files
- 12 topic folders
- Multiple projects
- Web APIs

## 🔍 Current State

```bash
# No test files found
find . -name "*test*.py"  # Returns nothing
```

## ✅ Tasks

### Phase 1: Test Infrastructure

- [ ] Create `tests/` folder structure:
  ```
  tests/
  ├── __init__.py
  ├── conftest.py          # Pytest fixtures
  ├── test_basics/
  │   ├── test_introduction.py
  │   ├── test_variables.py
  │   └── ...
  ├── test_fastapi/
  │   └── test_api.py
  └── test_llm/
      └── test_architecture.py
  ```

- [ ] Add test dependencies to `requirements.txt`:
  ```txt
  pytest==7.4.0
  pytest-cov==4.1.0
  pytest-asyncio==0.21.0
  ```

- [ ] Create `pytest.ini`:
  ```ini
  [pytest]
  testpaths = tests
  python_files = test_*.py
  python_functions = test_*
  addopts = -v --cov --cov-report=html
  ```

### Phase 2: Write Tests

#### Basics Tests (Priority 1)

```python
# tests/test_basics/test_introduction.py
def test_hello_world(capsys):
    """Test hello world prints correctly"""
    from basics.01_introduction.01_hello_world import *
    captured = capsys.readouterr()
    assert "Hello World" in captured.out

def test_addition():
    """Test arithmetic addition"""
    from basics.02_variables_types.01_arithmetic import add
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```

#### API Tests (Priority 2)

```python
# tests/test_fastapi/test_api.py
from fastapi.testclient import TestClient
from fastapi.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Hello World" in response.json()["message"]

def test_list_campaigns():
    response = client.get("/campaigns")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
```

#### LLM Tests (Priority 3)

```python
# tests/test_llm/test_architecture.py
def test_transformer_forward():
    """Test transformer forward pass"""
    from llm_fundamentals.architecture import TransformerBlock
    # Test implementation
```

### Phase 3: CI/CD Integration

- [ ] Add GitHub Actions workflow:
  ```yaml
  name: Tests
  on: [push, pull_request]
  jobs:
    test:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v2
        - name: Set up Python
          uses: actions/setup-python@v2
          with:
            python-version: 3.10
        - name: Install dependencies
          run: pip install -r requirements.txt
        - name: Run tests
          run: pytest --cov
  ```

- [ ] Add coverage badge to README
- [ ] Require tests for PRs

## 🎯 Why This Matters

- **Quality**: Catch bugs early
- **Confidence**: Refactor safely
- **Learning**: Teach testing best practices
- **Professionalism**: Industry standard

## 📊 Coverage Goals

| Component | Target | Current |
|-----------|--------|---------|
| Basics | 80% | 0% |
| FastAPI | 90% | 0% |
| REST API | 80% | 0% |
| LLM | 70% | 0% |
| **Overall** | **80%** | **0%** |

## 💡 Implementation Tips

1. **Start Small**: Test one folder at a time
2. **Test Examples**: Use existing examples as test cases
3. **Mock External**: Mock APIs, files, databases
4. **Document**: Explain what each test covers

## ⚠️ Risk Assessment

**Medium Effort:**
- Large task (150+ files)
- Requires testing knowledge
- Time investment needed

## 📝 Difficulty

**Advanced** - Requires testing expertise

## 🔗 Related

- CI/CD setup: #25
- Code quality: #23
- Documentation: #21
