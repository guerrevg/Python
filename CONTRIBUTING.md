# Contributing to Python Mastery

Thank you for your interest in contributing! 🎉

## How to Contribute

### 1. Report Bugs
- Open an issue with `[BUG]` in the title
- Describe the problem clearly
- Include code examples if applicable

### 2. Suggest Features
- Open an issue with `[FEATURE]` in the title
- Explain what you'd like to see
- Describe why it would be helpful

### 3. Submit Code

**Step 1:** Fork the repository

**Step 2:** Create a branch
```bash
git checkout -b feature/your-feature-name
```

**Step 3:** Make your changes
- Follow the existing code style
- Add comments for complex logic
- Test your code

**Step 4:** Commit
```bash
git add .
git commit -m "feat: add your feature description"
```

**Step 5:** Push
```bash
git push origin feature/your-feature-name
```

**Step 6:** Open a Pull Request

---

## Code Style Guidelines

### Naming
- **Variables:** `lowercase_with_underscores`
- **Functions:** `lowercase_with_underscores`
- **Classes:** `PascalCase`
- **Constants:** `UPPERCASE`

### Comments
- Explain **why**, not just **what**
- Use `#` for inline comments
- Use docstrings for functions/classes

### Example
```python
# Good
def calculate_area(radius: float) -> float:
    """Calculate circle area from radius."""
    return 3.14159 * radius ** 2

# Bad
def calc(r):
    return 3.14159 * r * r
```

---

## Commit Message Format

```
type: short description

Optional longer description
```

**Types:**
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting)
- `refactor:` Code refactoring
- `test:` Test additions

**Examples:**
```
feat: add list comprehension examples
fix: correct typo in calculator.py
docs: update README with new sections
```

---

## Questions?

Open an issue or contact the maintainers.

Thanks for contributing! 🐍✨
