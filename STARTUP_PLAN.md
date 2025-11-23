# Startup Plan Code

This repository contains a simple implementation of a startup business plan structure in Python.

## Overview

The `startup_plan.py` module provides a `StartupPlan` class that helps organize and track key elements of a startup business plan:

- **Vision & Mission**: Define the company's vision and mission statements
- **Milestones**: Track important goals and deadlines
- **Team**: Manage team members and their roles
- **Progress Tracking**: Monitor milestone completion

## Features

### Core Components

1. **Vision & Mission Statements**
   - Set clear direction for the company
   - Define the purpose and goals

2. **Milestone Management**
   - Add milestones with target dates
   - Track completion status
   - Identify next priorities

3. **Team Structure**
   - Add team members with roles
   - Track skills and expertise
   - Record joining dates

## Usage

### Basic Example

```python
from startup_plan import StartupPlan
from datetime import datetime, timedelta

# Create a new startup plan
plan = StartupPlan("MyStartup", "Founder Name")

# Set vision and mission
plan.set_vision("To make the world a better place")
plan.set_mission("Building solutions that solve real problems")

# Add milestones
today = datetime.now()
plan.add_milestone(
    "Launch MVP",
    "Release minimum viable product",
    today + timedelta(days=90)
)

# Add team members
plan.add_team_member(
    "Alice Developer",
    "Lead Engineer",
    ["Python", "JavaScript", "DevOps"]
)

# Get summary
print(plan.get_summary())
```

### Running Examples

```bash
# Run the built-in example
python startup_plan.py

# Run the practical usage example
python example_usage.py

# Run the test suite
python test_startup_plan.py
```

These commands will demonstrate the various features and capabilities of the startup plan module.

## Structure

The `StartupPlan` class provides these main methods:

- `set_vision(vision: str)` - Set the company vision
- `set_mission(mission: str)` - Set the company mission
- `add_milestone(title, description, target_date)` - Add a new milestone
- `complete_milestone(title)` - Mark a milestone as complete
- `add_team_member(name, role, skills)` - Add a team member
- `get_summary()` - Get a formatted summary
- `get_next_milestone()` - Get the next uncompleted milestone

## Files in This Project

- `startup_plan.py` - Main module with StartupPlan class implementation
- `STARTUP_PLAN.md` - This documentation file
- `example_usage.py` - Practical usage example demonstrating real-world scenarios
- `test_startup_plan.py` - Comprehensive test suite (8 tests)

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Testing

Run the test suite to verify the implementation:

```bash
python test_startup_plan.py
```

All tests should pass with ✅ indicators.

## License

MIT License - See LICENSE file for details
