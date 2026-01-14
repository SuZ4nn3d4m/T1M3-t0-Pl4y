# Copilot Instructions for T1M3-t0-Pl4y

This repository contains a simple Python implementation of a startup business plan structure.

## Project Overview

This is a Python project that provides a `StartupPlan` class for organizing and tracking key elements of a startup business plan:
- Vision & Mission statements
- Milestones with target dates
- Team members with roles and skills
- Progress tracking

## Code Style and Conventions

- **Python Version**: Python 3.6 or higher
- **Type Hints**: Use type hints for function parameters and return values
- **Docstrings**: Use docstrings for all classes and functions
- **Imports**: Group imports by standard library, third-party, and local modules
- **No External Dependencies**: Use only Python standard library

## File Structure

- `startup_plan.py` - Main module with the StartupPlan class
- `example_usage.py` - Practical usage examples
- `test_startup_plan.py` - Test suite with unit tests
- `STARTUP_PLAN.md` - Documentation

## Build and Test

### Running Tests
```bash
python test_startup_plan.py
```

### Running Examples
```bash
# Run the built-in example
python startup_plan.py

# Run the practical usage example
python example_usage.py
```

### Expected Test Output
- Tests use simple assertions with print statements for pass/fail indicators
- Each test function should be prefixed with `test_`
- Use ✓ symbol for individual passed tests and ✅ emoji for final success message
- All 8 tests should pass

## Key Patterns

- Use `datetime` and `timedelta` for date handling
- Milestones and team members are stored as dictionaries in lists
- Methods return `bool` for success/failure operations
- Use `Optional` from typing for nullable return values

## When Making Changes

### General Guidelines
1. Maintain backward compatibility with existing methods
2. Add tests for new functionality
3. Update documentation in STARTUP_PLAN.md if needed
4. Keep the code simple and readable
5. Run tests after making changes to ensure nothing is broken

### Testing Requirements
- **Always** add tests for new methods or functionality
- Follow the existing test pattern in `test_startup_plan.py`
- Tests should have clear docstrings explaining what they test
- Use descriptive assertion messages when appropriate

### Documentation Updates
- Update STARTUP_PLAN.md if adding new features or changing behavior
- Update docstrings in the code when modifying methods
- Keep README.md in sync with any structural changes

## Suitable Tasks for Copilot

This repository is well-suited for:
- ✅ Bug fixes in the StartupPlan class
- ✅ Adding new methods to the StartupPlan class
- ✅ Improving test coverage
- ✅ Enhancing documentation
- ✅ Small feature additions (e.g., new milestone/team tracking features)
- ✅ Code refactoring for better readability
- ✅ Adding type hints where missing

Tasks that may need human review:
- ⚠️ Major architectural changes
- ⚠️ Changes to the core data structure
- ⚠️ Breaking changes to the public API

## Security and Safety

- Do not add external dependencies without explicit approval
- Keep data structures simple and avoid complex serialization
- Validate input data types in new methods
- No network calls or file system operations beyond what's already present
