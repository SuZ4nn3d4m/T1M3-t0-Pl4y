"""
Coding Agent - A funny yet task-focused AI coding assistant
Writes code in multiple languages, builds on command, validates correctness, and thinks for you!
"""

import subprocess
import re
import os
from typing import Dict, List, Optional, Tuple
from datetime import datetime


class CodingAgent:
    """
    A humorous but professional coding agent that writes, validates, and builds code
    in multiple programming languages.
    """
    
    # Supported languages with their file extensions and build commands
    LANGUAGES = {
        'python': {
            'extension': '.py',
            'build_cmd': 'python -m py_compile {file}',
            'run_cmd': 'python {file}',
            'comment': '#'
        },
        'javascript': {
            'extension': '.js',
            'build_cmd': 'node --check {file}',
            'run_cmd': 'node {file}',
            'comment': '//'
        },
        'java': {
            'extension': '.java',
            'build_cmd': 'javac {file}',
            'run_cmd': 'java {classname}',
            'comment': '//'
        },
        'cpp': {
            'extension': '.cpp',
            'build_cmd': 'g++ -o {output} {file}',
            'run_cmd': './{output}',
            'comment': '//'
        },
        'c': {
            'extension': '.c',
            'build_cmd': 'gcc -o {output} {file}',
            'run_cmd': './{output}',
            'comment': '//'
        },
        'go': {
            'extension': '.go',
            'build_cmd': 'go build {file}',
            'run_cmd': 'go run {file}',
            'comment': '//'
        },
        'rust': {
            'extension': '.rs',
            'build_cmd': 'rustc {file}',
            'run_cmd': './{output}',
            'comment': '//'
        },
        'ruby': {
            'extension': '.rb',
            'build_cmd': 'ruby -c {file}',
            'run_cmd': 'ruby {file}',
            'comment': '#'
        },
        'php': {
            'extension': '.php',
            'build_cmd': 'php -l {file}',
            'run_cmd': 'php {file}',
            'comment': '//'
        },
        'typescript': {
            'extension': '.ts',
            'build_cmd': 'tsc {file}',
            'run_cmd': 'node {jsfile}',
            'comment': '//'
        }
    }
    
    # Funny but professional messages
    HUMOR_MESSAGES = [
        "🎯 Alright, let's code like there's no Stack Overflow!",
        "💻 Time to turn coffee into code... and bugs into features!",
        "🚀 Deploying awesomeness in 3... 2... 1...",
        "🔧 Warning: This code is so good, your compiler might cry tears of joy!",
        "⚡ Coding at the speed of light (or at least the speed of my processor)!",
        "🎨 Painting the canvas of logic with the brush of syntax!",
        "🧠 Engaging big brain mode... standby for genius!",
        "🎪 Step right up! Watch me juggle semicolons and curly braces!",
        "🏗️ Building digital empires, one line at a time!",
        "🌟 Making the impossible merely improbable!"
    ]
    
    def __init__(self, name: str = "CodeBot"):
        self.name = name
        self.code_history: List[Dict] = []
        self.build_history: List[Dict] = []
        self.created_at = datetime.now()
        self.humor_index = 0
        
    def get_funny_message(self) -> str:
        """Get a funny but professional message"""
        message = self.HUMOR_MESSAGES[self.humor_index % len(self.HUMOR_MESSAGES)]
        self.humor_index += 1
        return message
    
    def think(self, problem: str) -> str:
        """
        "Think" about a problem and provide suggestions
        """
        thoughts = f"""
🤔 {self.name} is thinking...

Problem: {problem}

💡 Here's what I'm thinking:
1. Break it down: Split the problem into smaller, manageable chunks
2. Pick the right tool: Choose the best language/framework for the job
3. Plan first, code second: Outline the logic before typing
4. Test early, test often: Catch bugs before they catch you
5. Keep it simple: Complexity is the enemy of reliability

{self.get_funny_message()}
"""
        return thoughts
    
    def write_code(self, language: str, code: str, filename: Optional[str] = None) -> Dict:
        """
        Write code in the specified language
        """
        language = language.lower()
        
        if language not in self.LANGUAGES:
            return {
                'success': False,
                'error': f"Oops! I don't speak '{language}' yet. Try one of these: {', '.join(self.LANGUAGES.keys())}",
                'filename': None
            }
        
        # Generate filename if not provided
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"code_{timestamp}{self.LANGUAGES[language]['extension']}"
        
        # Ensure proper extension
        if not filename.endswith(self.LANGUAGES[language]['extension']):
            filename += self.LANGUAGES[language]['extension']
        
        try:
            with open(filename, 'w') as f:
                f.write(code)
            
            # Record in history
            record = {
                'language': language,
                'filename': filename,
                'timestamp': datetime.now(),
                'lines': len(code.split('\n')),
                'size': len(code)
            }
            self.code_history.append(record)
            
            return {
                'success': True,
                'filename': filename,
                'message': f"✨ Code written successfully! File: {filename}",
                'humor': self.get_funny_message()
            }
        except Exception as e:
            return {
                'success': False,
                'error': f"Uh-oh! Something went wrong: {str(e)}",
                'filename': None
            }
    
    def validate_code(self, filename: str) -> Dict:
        """
        Validate code syntax and basic correctness
        """
        if not os.path.exists(filename):
            return {
                'success': False,
                'error': f"File not found: {filename}",
                'valid': False
            }
        
        # Determine language from extension
        ext = os.path.splitext(filename)[1]
        language = None
        for lang, config in self.LANGUAGES.items():
            if config['extension'] == ext:
                language = lang
                break
        
        if not language:
            return {
                'success': False,
                'error': f"Unknown file type: {ext}",
                'valid': False
            }
        
        # Basic syntax checks
        validation_results = {
            'success': True,
            'language': language,
            'filename': filename,
            'checks': []
        }
        
        with open(filename, 'r') as f:
            content = f.read()
            lines = content.split('\n')
        
        # Check for common issues
        issues = []
        
        # Check for empty file
        if not content.strip():
            issues.append("⚠️ File is empty!")
        
        # Check for balanced braces/brackets (for C-style languages)
        if language in ['javascript', 'java', 'cpp', 'c', 'go', 'rust', 'php', 'typescript']:
            open_braces = content.count('{')
            close_braces = content.count('}')
            if open_braces != close_braces:
                issues.append(f"⚠️ Unbalanced braces: {open_braces} open vs {close_braces} close")
        
        # Check for balanced parentheses
        open_parens = content.count('(')
        close_parens = content.count(')')
        if open_parens != close_parens:
            issues.append(f"⚠️ Unbalanced parentheses: {open_parens} open vs {close_parens} close")
        
        validation_results['checks'] = issues if issues else ["✅ Basic syntax checks passed!"]
        validation_results['valid'] = len(issues) == 0
        
        if validation_results['valid']:
            validation_results['message'] = f"🎉 Code looks good! {self.get_funny_message()}"
        else:
            validation_results['message'] = "Found some issues that need attention!"
        
        return validation_results
    
    def build(self, filename: str, output_name: Optional[str] = None) -> Dict:
        """
        Build/compile the code file
        """
        if not os.path.exists(filename):
            return {
                'success': False,
                'error': f"File not found: {filename}",
                'output': None
            }
        
        # Determine language
        ext = os.path.splitext(filename)[1]
        language = None
        for lang, config in self.LANGUAGES.items():
            if config['extension'] == ext:
                language = lang
                break
        
        if not language:
            return {
                'success': False,
                'error': f"Unknown file type: {ext}",
                'output': None
            }
        
        # Prepare build command
        lang_config = self.LANGUAGES[language]
        build_cmd = lang_config['build_cmd']
        
        # Handle output name for compiled languages
        if not output_name:
            output_name = os.path.splitext(filename)[0]
        
        # Replace placeholders
        build_cmd = build_cmd.replace('{file}', filename)
        build_cmd = build_cmd.replace('{output}', output_name)
        
        if language == 'java':
            # Extract class name from filename
            classname = os.path.splitext(os.path.basename(filename))[0]
            build_cmd = build_cmd.replace('{classname}', classname)
        
        print(f"🔨 Building {filename}...")
        print(f"📋 Command: {build_cmd}")
        
        try:
            result = subprocess.run(
                build_cmd,
                shell=True,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            build_record = {
                'language': language,
                'filename': filename,
                'command': build_cmd,
                'timestamp': datetime.now(),
                'success': result.returncode == 0,
                'stdout': result.stdout,
                'stderr': result.stderr
            }
            self.build_history.append(build_record)
            
            if result.returncode == 0:
                return {
                    'success': True,
                    'message': f"✅ Build successful! {self.get_funny_message()}",
                    'output': output_name,
                    'stdout': result.stdout,
                    'stderr': result.stderr
                }
            else:
                return {
                    'success': False,
                    'error': "Build failed!",
                    'output': None,
                    'stdout': result.stdout,
                    'stderr': result.stderr
                }
        except subprocess.TimeoutExpired:
            return {
                'success': False,
                'error': "Build timed out (>30s)",
                'output': None
            }
        except Exception as e:
            return {
                'success': False,
                'error': f"Build error: {str(e)}",
                'output': None
            }
    
    def suggest_improvements(self, filename: str) -> List[str]:
        """
        Suggest code improvements (simple heuristics)
        """
        if not os.path.exists(filename):
            return ["❌ File not found!"]
        
        suggestions = []
        
        with open(filename, 'r') as f:
            content = f.read()
            lines = content.split('\n')
        
        # Check file length
        if len(lines) > 500:
            suggestions.append("📏 Consider splitting this file - it's getting pretty long!")
        
        # Check for long lines
        long_lines = [i+1 for i, line in enumerate(lines) if len(line) > 100]
        if long_lines:
            suggestions.append(f"📐 Lines {long_lines[:3]} are quite long. Consider breaking them up!")
        
        # Check for TODO comments
        todos = [i+1 for i, line in enumerate(lines) if 'TODO' in line or 'FIXME' in line]
        if todos:
            suggestions.append(f"📝 Found TODO/FIXME comments on lines: {todos}")
        
        # Check for magic numbers (simple check)
        if re.search(r'\b\d{3,}\b', content):
            suggestions.append("🔢 Consider using named constants instead of magic numbers!")
        
        # Check for duplicated code patterns
        if len(lines) > 10:
            line_set = set(line.strip() for line in lines if line.strip())
            if len(line_set) < len([l for l in lines if l.strip()]) * 0.8:
                suggestions.append("♻️ Looks like there might be some duplicated code. DRY it up!")
        
        if not suggestions:
            suggestions.append(f"🌟 Code looks great! {self.get_funny_message()}")
        
        return suggestions
    
    def get_stats(self) -> str:
        """
        Get agent statistics
        """
        total_lines = sum(record['lines'] for record in self.code_history)
        successful_builds = sum(1 for build in self.build_history if build['success'])
        
        stats = f"""
📊 {self.name} Statistics
{'='*50}
⏰ Active since: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}
📝 Files created: {len(self.code_history)}
📏 Total lines written: {total_lines}
🔨 Build attempts: {len(self.build_history)}
✅ Successful builds: {successful_builds}
🎯 Build success rate: {(successful_builds/len(self.build_history)*100) if self.build_history else 0:.1f}%

Supported languages: {', '.join(sorted(self.LANGUAGES.keys()))}

{self.get_funny_message()}
"""
        return stats


def create_sample_code(language: str) -> str:
    """
    Generate sample code for different languages
    """
    samples = {
        'python': '''#!/usr/bin/env python3
"""Hello World in Python"""

def greet(name):
    """Greet someone"""
    return f"Hello, {name}! 🐍"

if __name__ == "__main__":
    print(greet("World"))
    print("Python is awesome!")
''',
        'javascript': '''// Hello World in JavaScript

function greet(name) {
    return `Hello, ${name}! 🚀`;
}

console.log(greet("World"));
console.log("JavaScript is awesome!");
''',
        'java': '''public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World! ☕");
        System.out.println("Java is awesome!");
    }
}
''',
        'cpp': '''#include <iostream>
#include <string>

int main() {
    std::string greeting = "Hello, World! ⚡";
    std::cout << greeting << std::endl;
    std::cout << "C++ is awesome!" << std::endl;
    return 0;
}
''',
        'go': '''package main

import "fmt"

func main() {
    fmt.Println("Hello, World! 🎯")
    fmt.Println("Go is awesome!")
}
''',
        'rust': '''fn main() {
    println!("Hello, World! 🦀");
    println!("Rust is awesome!");
}
'''
    }
    
    return samples.get(language, f"// Sample code for {language}\nprint('Hello, World!');\n")


if __name__ == "__main__":
    # Demo the agent
    print("🤖 Coding Agent Demo\n")
    
    agent = CodingAgent("CodeMaster3000")
    
    # Think about a problem
    print(agent.think("How to write a web scraper?"))
    print("\n")
    
    # Write some Python code
    python_code = create_sample_code('python')
    result = agent.write_code('python', python_code, 'demo_hello.py')
    print(result['message'])
    if 'humor' in result:
        print(result['humor'])
    print("\n")
    
    # Validate the code
    validation = agent.validate_code('demo_hello.py')
    print(f"Validation: {validation['message']}")
    for check in validation['checks']:
        print(f"  {check}")
    print("\n")
    
    # Build the code
    build_result = agent.build('demo_hello.py')
    print(build_result['message'] if build_result['success'] else f"Error: {build_result['error']}")
    print("\n")
    
    # Get suggestions
    suggestions = agent.suggest_improvements('demo_hello.py')
    print("💡 Suggestions:")
    for suggestion in suggestions:
        print(f"  {suggestion}")
    print("\n")
    
    # Show stats
    print(agent.get_stats())
    
    # Cleanup demo file
    import os
    if os.path.exists('demo_hello.py'):
        os.remove('demo_hello.py')
        print("🧹 Cleaned up demo files!")
