"""
Example usage of the Coding Agent
Demonstrates how to use the funny yet task-focused coding assistant
"""

from coding_agent import CodingAgent, create_sample_code
import os


def main():
    """Demonstrate the coding agent capabilities"""
    
    print("="*70)
    print("🤖 Welcome to the Coding Agent Demo!")
    print("="*70)
    print()
    
    # Create our agent
    agent = CodingAgent("CodeWizard")
    
    # 1. Think about a problem
    print("📖 SCENARIO 1: Asking the agent to think about a problem")
    print("-"*70)
    thoughts = agent.think("Build a REST API for a todo list application")
    print(thoughts)
    
    # 2. Write code in Python
    print("\n📖 SCENARIO 2: Writing Python code")
    print("-"*70)
    
    python_code = '''#!/usr/bin/env python3
"""
Simple calculator program
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        return "Error: Division by zero!"
    return a / b

if __name__ == "__main__":
    print("Calculator Demo")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"5 - 3 = {subtract(5, 3)}")
    print(f"5 * 3 = {multiply(5, 3)}")
    print(f"5 / 3 = {divide(5, 3):.2f}")
'''
    
    result = agent.write_code('python', python_code, 'calculator.py')
    print(f"✨ {result['message']}")
    print(f"🎭 {result.get('humor', '')}")
    
    # 3. Validate the code
    print("\n📖 SCENARIO 3: Validating the code")
    print("-"*70)
    
    validation = agent.validate_code('calculator.py')
    print(f"Status: {validation['message']}")
    for check in validation['checks']:
        print(f"  {check}")
    
    # 4. Build/compile the code
    print("\n📖 SCENARIO 4: Building the code")
    print("-"*70)
    
    build_result = agent.build('calculator.py')
    if build_result['success']:
        print(f"✅ {build_result['message']}")
    else:
        print(f"❌ {build_result['error']}")
    
    # 5. Get improvement suggestions
    print("\n📖 SCENARIO 5: Getting code improvement suggestions")
    print("-"*70)
    
    suggestions = agent.suggest_improvements('calculator.py')
    print("💡 Suggestions:")
    for suggestion in suggestions:
        print(f"  {suggestion}")
    
    # 6. Write code in another language (JavaScript)
    print("\n📖 SCENARIO 6: Writing JavaScript code")
    print("-"*70)
    
    js_code = '''// Simple greeting function
function greet(name, time) {
    const greetings = {
        'morning': 'Good morning',
        'afternoon': 'Good afternoon',
        'evening': 'Good evening'
    };
    
    const greeting = greetings[time] || 'Hello';
    return `${greeting}, ${name}! 👋`;
}

// Test the function
console.log(greet('Alice', 'morning'));
console.log(greet('Bob', 'afternoon'));
console.log(greet('Charlie', 'evening'));
'''
    
    result = agent.write_code('javascript', js_code, 'greetings.js')
    print(f"✨ {result['message']}")
    
    # Validate JavaScript
    validation = agent.validate_code('greetings.js')
    print(f"Validation: {validation['message']}")
    
    # 7. Write code with intentional errors to show validation
    print("\n📖 SCENARIO 7: Detecting code issues")
    print("-"*70)
    
    buggy_code = '''function broken() {
    console.log("This has unmatched braces"
    // Missing closing parenthesis and brace
'''
    
    agent.write_code('javascript', buggy_code, 'buggy.js')
    validation = agent.validate_code('buggy.js')
    print(f"Validation result: {'✅ PASS' if validation['valid'] else '❌ ISSUES FOUND'}")
    for check in validation['checks']:
        print(f"  {check}")
    
    # 8. Show agent statistics
    print("\n📖 SCENARIO 8: Agent statistics and capabilities")
    print("-"*70)
    print(agent.get_stats())
    
    # 9. Demonstrate multiple language support
    print("📖 SCENARIO 9: Multi-language support")
    print("-"*70)
    
    # Write a simple Go program
    go_code = '''package main

import "fmt"

func main() {
    fmt.Println("Hello from Go! 🚀")
}
'''
    result = agent.write_code('go', go_code, 'hello.go')
    print(f"Go code: {result['message']}")
    
    # Write a simple C++ program
    cpp_code = '''#include <iostream>

int main() {
    std::cout << "Hello from C++! ⚡" << std::endl;
    return 0;
}
'''
    result = agent.write_code('cpp', cpp_code, 'hello.cpp')
    print(f"C++ code: {result['message']}")
    
    # 10. Cleanup demo files
    print("\n📖 SCENARIO 10: Cleanup")
    print("-"*70)
    
    demo_files = ['calculator.py', 'greetings.js', 'buggy.js', 'hello.go', 'hello.cpp']
    for file in demo_files:
        if os.path.exists(file):
            os.remove(file)
            print(f"🗑️  Removed {file}")
    
    # Clean up pycache if exists
    if os.path.exists('__pycache__'):
        import shutil
        shutil.rmtree('__pycache__')
        print("🗑️  Removed __pycache__")
    
    print("\n" + "="*70)
    print("🎉 Demo complete! The Coding Agent is ready to help you code!")
    print("="*70)


if __name__ == "__main__":
    main()
