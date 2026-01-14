# Copilot Instructions for T1M3-t0-Pl4y

This repository contains a simple Python implementation of a startup business plan structure.

## Project Overview

This is a Python project that provides a `StartupPlan` class for organizing and tracking key elements of a startup business plan:
- Vision & Mission statements
- Milestones with target dates
- Team members with roles and skills
- Progress tracking

## Code Style and Conventions

### Python Standards
- **Python Version**: Python 3.6 or higher
- **Type Hints**: Always use type hints for function parameters and return values
  - Example: `def add_milestone(self, title: str, description: str, target_date: datetime) -> None:`
- **Docstrings**: Use docstrings for all classes and functions
  - Format: Simple one-line or multi-line docstrings
  - Example: `"""Add a milestone to the startup plan"""`
- **Imports**: Group imports in this order:
  1. Standard library imports (e.g., `datetime`, `typing`)
  2. Third-party imports (none currently used)
  3. Local module imports
- **No External Dependencies**: Use only Python standard library - do not add external packages

### Naming Conventions
- **Classes**: PascalCase (e.g., `StartupPlan`)
- **Functions/Methods**: snake_case (e.g., `add_milestone`, `get_next_milestone`)
- **Variables**: snake_case (e.g., `company_name`, `target_date`)
- **Constants**: UPPER_SNAKE_CASE (if needed)

## File Structure

- `startup_plan.py` - Main module with the StartupPlan class
- `example_usage.py` - Practical usage examples
- `test_startup_plan.py` - Test suite with unit tests
- `STARTUP_PLAN.md` - Documentation

## Testing

- **Run tests with**: `python test_startup_plan.py`
- Tests use simple assertions with print statements for pass/fail indicators
- Each test function should be prefixed with `test_`
- Use ✓ symbol for individual passed tests and ✅ emoji for final success message
- **Testing Requirements**:
  - Add tests for all new functionality
  - Test both success and failure cases
  - Verify edge cases (e.g., empty lists, None values, missing items)
  - Example pattern:
    ```python
    def test_feature():
        """Test description"""
        # Setup
        plan = StartupPlan("TestCo", "Founder")
        # Execute
        result = plan.some_method()
        # Assert
        assert result is True
        print("✓ test_feature passed")
    ```

## Key Patterns

### Data Structures
- **Milestones**: Stored as dictionaries in a list with keys:
  - `title` (str): Milestone name
  - `description` (str): Details
  - `target_date` (datetime): Due date
  - `completed` (bool): Status
  - `completed_date` (datetime | None): Completion timestamp
- **Team Members**: Stored as dictionaries in a list with keys:
  - `name` (str): Person's name
  - `role` (str): Job title
  - `skills` (List[str]): List of skills
  - `joined_date` (datetime): When they joined

### Date Handling
- Always use `datetime` and `timedelta` from the standard library
- Store dates as `datetime` objects, not strings
- Format dates for display using `strftime('%Y-%m-%d')` or similar

### Return Values
- Methods that modify state return `None` (e.g., `add_milestone`)
- Methods that perform operations return `bool` for success/failure (e.g., `complete_milestone`)
- Use `Optional[Type]` from typing for methods that may return `None` (e.g., `get_next_milestone`)

### Error Handling
- Use simple, direct error handling
- Return `False` for operations that fail (e.g., completing non-existent milestone)
- Don't raise exceptions for expected failure cases
- Keep error handling minimal and intuitive

## When Making Changes

### Guidelines
1. **Maintain backward compatibility** with existing methods - don't break existing functionality
2. **Add tests for new functionality** before implementing or immediately after
3. **Update documentation** in STARTUP_PLAN.md if adding new features or changing behavior
4. **Keep the code simple and readable** - this is an educational/example project
5. **Don't add external dependencies** - stick to Python standard library only

### Code Review Checklist
Before submitting changes, verify:
- [ ] Type hints are present on all new functions
- [ ] Docstrings are added for new classes/methods
- [ ] Tests are added and passing
- [ ] Code follows existing naming conventions
- [ ] No external dependencies added
- [ ] Documentation updated if needed

## Common Tasks

### Adding a New Method to StartupPlan
1. Add the method with proper type hints and docstring
2. Follow the existing pattern (e.g., storing data in lists/dicts)
3. Add a test in `test_startup_plan.py`
4. Update `STARTUP_PLAN.md` if it's a user-facing feature
5. Consider adding an example to `example_usage.py` if relevant

### Example: Adding a New Field
```python
# In __init__:
self.new_field: List[Dict] = []  # Dictionary structure documented below

# Add a method to populate it:
def add_new_item(self, name: str, details: str) -> None:
    """Add a new item to the new field"""
    # Create dictionary with consistent key structure
    item = {
        'name': name,          # str: Item name
        'details': details,    # str: Item details
        'created_at': datetime.now()  # datetime: Creation timestamp
    }
    self.new_field.append(item)
```

**Note**: Use `List[Dict]` to match existing codebase style. While more specific types like `TypedDict` could be used, the current codebase prioritizes simplicity. Document the expected dictionary keys in comments as shown above.

## Security Considerations

- Don't store sensitive data (passwords, API keys) in the code
- Validate input data types where appropriate
- Use safe date parsing if accepting date strings from users
- Keep the code simple to avoid security vulnerabilities
