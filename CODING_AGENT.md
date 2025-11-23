# Coding Agent 🤖

A funny yet task-focused AI coding assistant that writes code in multiple languages, validates correctness, builds on command, and provides intelligent suggestions!

## Overview

The Coding Agent is a comprehensive coding assistant that combines humor with professionalism to help developers write, validate, and build code across multiple programming languages. It stays focused on tasks while keeping the development experience enjoyable.

## Features

### 🎯 Core Capabilities

1. **Multi-Language Support** - Write code in 10+ programming languages
2. **Code Validation** - Check syntax and common issues before building
3. **Build on Command** - Compile/build code with appropriate tools
4. **Smart Suggestions** - Get intelligent recommendations for code improvements
5. **Think Assistance** - Help analyze problems before coding
6. **Personality** - Funny but professional humor that doesn't distract

### 🌍 Supported Languages

- **Python** (.py)
- **JavaScript** (.js)
- **TypeScript** (.ts)
- **Java** (.java)
- **C** (.c)
- **C++** (.cpp)
- **Go** (.go)
- **Rust** (.rs)
- **Ruby** (.rb)
- **PHP** (.php)

Each language has proper build/compile commands and validation rules.

## Installation

No dependencies required! Uses only Python standard library.

```bash
# Clone the repository
git clone https://github.com/SuZ4nn3d4m/T1M3-t0-Pl4y.git
cd T1M3-t0-Pl4y

# Run the demo
python coding_agent.py
```

## Quick Start

```python
from coding_agent import CodingAgent

# Create an agent
agent = CodingAgent("MyBot")

# Think about a problem
thoughts = agent.think("How to build a web scraper?")
print(thoughts)

# Write some code
code = '''
def greet(name):
    return f"Hello, {name}!"
    
print(greet("World"))
'''

result = agent.write_code('python', code, 'greet.py')
print(result['message'])

# Validate the code
validation = agent.validate_code('greet.py')
print(f"Valid: {validation['valid']}")

# Build it
build_result = agent.build('greet.py')
print(f"Build: {build_result['success']}")

# Get suggestions
suggestions = agent.suggest_improvements('greet.py')
for suggestion in suggestions:
    print(suggestion)

# View statistics
print(agent.get_stats())
```

## API Reference

### CodingAgent Class

#### `__init__(name: str = "CodeBot")`
Create a new coding agent with the given name.

```python
agent = CodingAgent("SuperCoder")
```

#### `think(problem: str) -> str`
Analyze a problem and provide thinking framework.

```python
thoughts = agent.think("Build a REST API")
print(thoughts)
```

Returns a formatted string with problem-solving approach.

#### `write_code(language: str, code: str, filename: Optional[str] = None) -> Dict`
Write code in the specified language to a file.

```python
result = agent.write_code('python', 'print("hi")', 'hello.py')
# Returns: {'success': True, 'filename': 'hello.py', 'message': '...', 'humor': '...'}
```

**Parameters:**
- `language`: One of the supported languages (case-insensitive)
- `code`: The source code as a string
- `filename`: Optional filename (auto-generated if not provided)

**Returns:** Dictionary with success status, filename, message, and humor

#### `validate_code(filename: str) -> Dict`
Validate code syntax and check for common issues.

```python
validation = agent.validate_code('hello.py')
# Returns: {'success': True, 'valid': True, 'checks': [...], 'message': '...'}
```

**Checks for:**
- Empty files
- Unbalanced braces/brackets
- Unbalanced parentheses
- Basic syntax issues

**Returns:** Dictionary with validation results and checks performed

#### `build(filename: str, output_name: Optional[str] = None) -> Dict`
Build/compile the code file using appropriate tools.

```python
result = agent.build('hello.py')
# Returns: {'success': True, 'message': '...', 'output': '...', 'stdout': '...', 'stderr': '...'}
```

**Parameters:**
- `filename`: Path to the source file
- `output_name`: Optional output filename for compiled languages

**Returns:** Dictionary with build results, stdout, and stderr

#### `suggest_improvements(filename: str) -> List[str]`
Suggest code improvements based on heuristics.

```python
suggestions = agent.suggest_improvements('hello.py')
# Returns: ['📏 Consider splitting this file...', ...]
```

**Analyzes:**
- File length
- Line length
- TODO/FIXME comments
- Magic numbers
- Code duplication

**Returns:** List of suggestion strings

#### `get_stats() -> str`
Get agent statistics and activity summary.

```python
stats = agent.get_stats()
print(stats)
```

**Returns:** Formatted string with:
- Files created
- Lines written
- Build attempts
- Success rates
- Supported languages

#### `get_funny_message() -> str`
Get a humorous but professional message.

```python
msg = agent.get_funny_message()
print(msg)  # "🎯 Alright, let's code like there's no Stack Overflow!"
```

### Helper Functions

#### `create_sample_code(language: str) -> str`
Generate sample "Hello World" code for testing.

```python
from coding_agent import create_sample_code

python_code = create_sample_code('python')
js_code = create_sample_code('javascript')
```

## Usage Examples

### Example 1: Simple Python Script

```python
from coding_agent import CodingAgent

agent = CodingAgent("QuickBot")

# Write a simple script
code = '''
import sys

def main():
    print("Hello from Python!")
    print(f"Python version: {sys.version}")

if __name__ == "__main__":
    main()
'''

agent.write_code('python', code, 'version.py')
agent.validate_code('version.py')
agent.build('version.py')
```

### Example 2: Multi-Language Project

```python
from coding_agent import CodingAgent, create_sample_code

agent = CodingAgent("MultiLang")

# Create files in different languages
for lang in ['python', 'javascript', 'go']:
    code = create_sample_code(lang)
    result = agent.write_code(lang, code)
    print(result['message'])
    
# Show what we've done
print(agent.get_stats())
```

### Example 3: Code Review Workflow

```python
from coding_agent import CodingAgent

agent = CodingAgent("Reviewer")

# Write code with potential issues
buggy_code = '''
def process_data(items):
    result = []
    for item in items:
        # TODO: optimize this loop
        if item > 1000:  # magic number
            result.append(item * 2)
    return result
'''

agent.write_code('python', buggy_code, 'process.py')

# Validate
validation = agent.validate_code('process.py')
print(f"Valid: {validation['valid']}")

# Get suggestions
suggestions = agent.suggest_improvements('process.py')
for s in suggestions:
    print(s)
```

### Example 4: Build Pipeline

```python
from coding_agent import CodingAgent

agent = CodingAgent("BuildMaster")

# Write code
code = "print('Build me!')"
agent.write_code('python', code, 'app.py')

# Validate before building
if agent.validate_code('app.py')['valid']:
    # Build
    result = agent.build('app.py')
    if result['success']:
        print("✅ Ready to deploy!")
    else:
        print(f"❌ Build failed: {result['stderr']}")
```

## Testing

Run the comprehensive test suite:

```bash
# Run all tests
python test_coding_agent.py

# Run with verbose output
python -v test_coding_agent.py
```

The test suite includes 18 tests covering:
- Agent creation and initialization
- Code writing in multiple languages
- Validation functionality
- Build processes
- Error handling
- Statistics tracking
- Multi-language support

## Example Output

Run the example demo:

```bash
python example_coding_agent.py
```

You'll see output like:

```
🤖 Welcome to the Coding Agent Demo!
======================================================================

📖 SCENARIO 1: Asking the agent to think about a problem
🤔 CodeWizard is thinking...
Problem: Build a REST API for a todo list application
💡 Here's what I'm thinking:
1. Break it down: Split the problem into smaller, manageable chunks
...

📖 SCENARIO 2: Writing Python code
✨ Code written successfully! File: calculator.py
🎭 💻 Time to turn coffee into code... and bugs into features!
...
```

## Humor Philosophy

The Coding Agent balances humor with professionalism:

✅ **Do:**
- Use emoji for visual appeal
- Include witty but relevant comments
- Celebrate successes enthusiastically
- Keep humor light and universal

❌ **Don't:**
- Distract from the task
- Use offensive or inappropriate humor
- Overwhelm with too many jokes
- Compromise code quality for humor

## Architecture

```
CodingAgent
├── Language Support
│   ├── Language configurations
│   ├── File extensions
│   ├── Build commands
│   └── Comment styles
│
├── Core Functions
│   ├── think() - Problem analysis
│   ├── write_code() - Code generation
│   ├── validate_code() - Syntax checking
│   ├── build() - Compilation
│   └── suggest_improvements() - Code review
│
└── State Management
    ├── code_history - Track all code written
    ├── build_history - Track all builds
    └── humor_index - Cycle through messages
```

## Requirements

- Python 3.6 or higher
- No external dependencies
- Optional: Language compilers/interpreters for building
  - `python` for Python
  - `node` for JavaScript
  - `javac` for Java
  - `gcc`/`g++` for C/C++
  - `go` for Go
  - `rustc` for Rust
  - etc.

## Extending the Agent

### Adding a New Language

```python
# Add to CodingAgent.LANGUAGES dictionary
'kotlin': {
    'extension': '.kt',
    'build_cmd': 'kotlinc {file}',
    'run_cmd': 'kotlin {classname}',
    'comment': '//'
}
```

### Adding New Humor Messages

```python
# Add to CodingAgent.HUMOR_MESSAGES list
"🎪 Another day, another semicolon!"
```

### Custom Validation Rules

Extend the `validate_code()` method with language-specific checks:

```python
def validate_code(self, filename: str) -> Dict:
    # ... existing code ...
    
    # Add custom check
    if language == 'python':
        if 'eval(' in content:
            issues.append("⚠️ Using eval() can be dangerous!")
    
    # ... rest of code ...
```

## Files in This Project

- `coding_agent.py` - Main agent implementation
- `test_coding_agent.py` - Comprehensive test suite (18 tests)
- `example_coding_agent.py` - Practical usage examples
- `CODING_AGENT.md` - This documentation

## Contributing

This is a fun learning project! Feel free to:
- Add support for more languages
- Improve validation logic
- Add more humor (keep it professional!)
- Enhance build commands
- Add more code suggestions

## License

MIT License - See LICENSE file for details

## FAQ

**Q: Can the agent actually write production code?**
A: The agent helps you write code by providing structure, validation, and building. You provide the logic and implementation details.

**Q: Does it require internet?**
A: No! It's completely offline and uses only Python standard library.

**Q: Why is it funny?**
A: Because coding should be enjoyable! The humor helps keep spirits up during long debugging sessions.

**Q: Can I disable the humor?**
A: You can ignore the humor messages, but where's the fun in that? 😄

**Q: What if my language isn't supported?**
A: Add it! See "Extending the Agent" section above.

## Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing tests for usage examples
- Run `python coding_agent.py` for a quick demo

---

Built with ❤️ and ☕ by developers, for developers!

**Remember:** The best code is code that works AND makes you smile! 😊
