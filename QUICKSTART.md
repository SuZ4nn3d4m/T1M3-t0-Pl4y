# Quick Start Guide 🚀

Get started with the Coding Agent in just 5 minutes!

## Installation

```bash
# Clone the repository
git clone https://github.com/SuZ4nn3d4m/T1M3-t0-Pl4y.git
cd T1M3-t0-Pl4y

# No dependencies to install! Uses only Python standard library
```

## Run Your First Demo

```bash
# Run the built-in demo
python coding_agent.py
```

You'll see the agent in action with examples of:
- Writing Python code
- Validating syntax
- Building code
- Suggesting improvements
- Displaying statistics

## Try the Examples

```bash
# See comprehensive usage examples
python example_coding_agent.py
```

This demonstrates:
- Multi-language support
- Problem-solving assistance
- Code validation
- Error detection
- And more!

## Run the Tests

```bash
# Verify everything works
python test_coding_agent.py
```

All 18 tests should pass! ✅

## Your First Script

Create a file called `my_agent.py`:

```python
from coding_agent import CodingAgent

# Create your agent
agent = CodingAgent("MyBot")

# Ask for help thinking through a problem
print(agent.think("Build a REST API"))

# Write some Python code
code = """
def hello(name):
    return f"Hello, {name}!"

print(hello("World"))
"""

result = agent.write_code('python', code, 'hello.py')
print(result['message'])

# Validate it
validation = agent.validate_code('hello.py')
print(f"Valid: {validation['valid']}")

# Build it
build = agent.build('hello.py')
print(f"Build successful: {build['success']}")

# Get suggestions
suggestions = agent.suggest_improvements('hello.py')
for s in suggestions:
    print(s)
```

Run it:
```bash
python my_agent.py
```

## Try Different Languages

```python
from coding_agent import CodingAgent, create_sample_code

agent = CodingAgent("MultiLang")

# Python
python_code = create_sample_code('python')
agent.write_code('python', python_code, 'app.py')
agent.build('app.py')

# JavaScript
js_code = create_sample_code('javascript')
agent.write_code('javascript', js_code, 'app.js')
agent.build('app.js')

# C++
cpp_code = create_sample_code('cpp')
agent.write_code('cpp', cpp_code, 'app.cpp')
agent.build('app.cpp', 'app')

# Show what you've done
print(agent.get_stats())
```

## Common Use Cases

### 1. Quick Code Generation
```python
agent = CodingAgent("QuickGen")
agent.write_code('python', 'print("Hello!")', 'quick.py')
```

### 2. Code Validation Pipeline
```python
agent = CodingAgent("Validator")
agent.write_code('python', code, 'mycode.py')

if agent.validate_code('mycode.py')['valid']:
    agent.build('mycode.py')
else:
    print("Fix errors first!")
```

### 3. Multi-File Projects
```python
agent = CodingAgent("ProjectBot")

# Write multiple files
agent.write_code('python', main_code, 'main.py')
agent.write_code('python', utils_code, 'utils.py')
agent.write_code('python', tests_code, 'tests.py')

# Check statistics
print(agent.get_stats())
```

## Next Steps

- Read the [full documentation](CODING_AGENT.md)
- Explore [example_coding_agent.py](example_coding_agent.py) for more examples
- Run [test_coding_agent.py](test_coding_agent.py) to see all features tested
- Extend the agent with your own language support

## Supported Languages

✅ Python
✅ JavaScript
✅ TypeScript
✅ Java
✅ C
✅ C++
✅ Go
✅ Rust
✅ Ruby
✅ PHP

## Getting Help

- Check [CODING_AGENT.md](CODING_AGENT.md) for detailed documentation
- Run `python coding_agent.py` to see a demo
- Look at the test files for usage examples

## Tips

1. **Start Simple**: Begin with Python or JavaScript
2. **Validate First**: Always validate before building
3. **Use Suggestions**: The agent provides helpful improvement tips
4. **Track Progress**: Use `get_stats()` to see your activity
5. **Have Fun**: Enjoy the humor while coding! 😄

---

**Ready to code?** Start with `python coding_agent.py` and let the fun begin! 🎉
