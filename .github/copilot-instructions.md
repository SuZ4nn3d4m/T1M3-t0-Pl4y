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

## Testing

- Run tests with: `python test_startup_plan.py`
- Tests use simple assertions with print statements for pass/fail indicators
- Each test function should be prefixed with `test_`
- Use ✓ symbol for individual passed tests and ✅ emoji for final success message

## Key Patterns

- Use `datetime` and `timedelta` for date handling
- Milestones and team members are stored as dictionaries in lists
- Methods return `bool` for success/failure operations
- Use `Optional` from typing for nullable return values

## When Making Changes

1. Maintain backward compatibility with existing methods
2. Add tests for new functionality
3. Update documentation in STARTUP_PLAN.md if needed
4. Keep the code simple and readable
