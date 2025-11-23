"""
Tests for the coding_agent module
"""

import os
import tempfile
from coding_agent import CodingAgent, create_sample_code


def test_create_agent():
    """Test creating a coding agent"""
    agent = CodingAgent("TestBot")
    assert agent.name == "TestBot"
    assert len(agent.code_history) == 0
    assert len(agent.build_history) == 0
    print("✓ test_create_agent passed")


def test_think():
    """Test the think functionality"""
    agent = CodingAgent("ThinkBot")
    thoughts = agent.think("How to solve world hunger?")
    assert "thinking" in thoughts.lower()
    assert "How to solve world hunger?" in thoughts
    assert len(thoughts) > 50
    print("✓ test_think passed")


def test_get_funny_message():
    """Test humor generation"""
    agent = CodingAgent("FunnyBot")
    message1 = agent.get_funny_message()
    message2 = agent.get_funny_message()
    
    # Messages should exist and be strings
    assert isinstance(message1, str)
    assert isinstance(message2, str)
    assert len(message1) > 0
    
    # Should cycle through different messages
    messages = [agent.get_funny_message() for _ in range(15)]
    assert len(set(messages)) > 1  # At least some variety
    print("✓ test_get_funny_message passed")


def test_write_python_code():
    """Test writing Python code"""
    agent = CodingAgent("PyBot")
    
    code = "print('Hello, World!')\n"
    result = agent.write_code('python', code, 'test_output.py')
    
    assert result['success'] is True
    assert 'test_output.py' in result['filename']
    assert os.path.exists('test_output.py')
    assert len(agent.code_history) == 1
    
    # Cleanup
    os.remove('test_output.py')
    print("✓ test_write_python_code passed")


def test_write_javascript_code():
    """Test writing JavaScript code"""
    agent = CodingAgent("JSBot")
    
    code = "console.log('Hello, JavaScript!');\n"
    result = agent.write_code('javascript', code, 'test_js.js')
    
    assert result['success'] is True
    assert 'test_js.js' in result['filename']
    assert os.path.exists('test_js.js')
    
    # Cleanup
    os.remove('test_js.js')
    print("✓ test_write_javascript_code passed")


def test_unsupported_language():
    """Test handling of unsupported language"""
    agent = CodingAgent("TestBot")
    
    result = agent.write_code('klingon', 'Qapla!', 'test.kl')
    
    assert result['success'] is False
    assert 'error' in result
    assert 'klingon' in result['error'].lower()
    print("✓ test_unsupported_language passed")


def test_validate_code():
    """Test code validation"""
    agent = CodingAgent("ValidBot")
    
    # Write valid code
    code = "def hello():\n    print('Hi')\n"
    agent.write_code('python', code, 'valid_test.py')
    
    validation = agent.validate_code('valid_test.py')
    assert validation['success'] is True
    assert validation['valid'] is True
    
    # Cleanup
    os.remove('valid_test.py')
    print("✓ test_validate_code passed")


def test_validate_unbalanced_braces():
    """Test validation catches unbalanced braces"""
    agent = CodingAgent("ValidBot")
    
    # Write code with unbalanced braces
    code = "function test() {\n    console.log('test');\n"  # Missing closing brace
    agent.write_code('javascript', code, 'unbalanced_test.js')
    
    validation = agent.validate_code('unbalanced_test.js')
    assert validation['success'] is True
    assert validation['valid'] is False
    assert any('brace' in check.lower() for check in validation['checks'])
    
    # Cleanup
    os.remove('unbalanced_test.js')
    print("✓ test_validate_unbalanced_braces passed")


def test_validate_nonexistent_file():
    """Test validation of non-existent file"""
    agent = CodingAgent("ValidBot")
    
    validation = agent.validate_code('does_not_exist.py')
    assert validation['success'] is False
    assert 'error' in validation
    print("✓ test_validate_nonexistent_file passed")


def test_build_python():
    """Test building Python code"""
    agent = CodingAgent("BuildBot")
    
    # Write valid Python code
    code = "print('Hello from test')\n"
    agent.write_code('python', code, 'build_test.py')
    
    # Build it
    result = agent.build('build_test.py')
    assert result['success'] is True
    assert len(agent.build_history) == 1
    assert agent.build_history[0]['success'] is True
    
    # Cleanup
    os.remove('build_test.py')
    if os.path.exists('__pycache__'):
        import shutil
        shutil.rmtree('__pycache__')
    print("✓ test_build_python passed")


def test_build_invalid_python():
    """Test building invalid Python code"""
    agent = CodingAgent("BuildBot")
    
    # Write invalid Python code
    code = "print('Missing closing quote)\n"
    agent.write_code('python', code, 'invalid_test.py')
    
    # Try to build it
    result = agent.build('invalid_test.py')
    assert result['success'] is False
    
    # Cleanup
    os.remove('invalid_test.py')
    print("✓ test_build_invalid_python passed")


def test_build_nonexistent_file():
    """Test building non-existent file"""
    agent = CodingAgent("BuildBot")
    
    result = agent.build('does_not_exist.py')
    assert result['success'] is False
    assert 'error' in result
    print("✓ test_build_nonexistent_file passed")


def test_suggest_improvements():
    """Test code improvement suggestions"""
    agent = CodingAgent("SuggestBot")
    
    # Write code
    code = "def test():\n    x = 12345  # TODO: fix this\n    print(x)\n"
    agent.write_code('python', code, 'suggest_test.py')
    
    suggestions = agent.suggest_improvements('suggest_test.py')
    assert isinstance(suggestions, list)
    assert len(suggestions) > 0
    
    # Cleanup
    os.remove('suggest_test.py')
    print("✓ test_suggest_improvements passed")


def test_get_stats():
    """Test getting agent statistics"""
    agent = CodingAgent("StatsBot")
    
    # Generate some activity
    agent.write_code('python', "print('test')", 'stat_test1.py')
    agent.write_code('javascript', "console.log('test')", 'stat_test2.js')
    agent.build('stat_test1.py')
    
    stats = agent.get_stats()
    assert "StatsBot" in stats
    assert "Files created: 2" in stats
    assert "Build attempts: 1" in stats
    
    # Cleanup
    os.remove('stat_test1.py')
    os.remove('stat_test2.js')
    if os.path.exists('__pycache__'):
        import shutil
        shutil.rmtree('__pycache__')
    print("✓ test_get_stats passed")


def test_create_sample_code():
    """Test sample code generation"""
    python_sample = create_sample_code('python')
    assert isinstance(python_sample, str)
    assert len(python_sample) > 0
    assert 'def' in python_sample or 'print' in python_sample
    
    js_sample = create_sample_code('javascript')
    assert isinstance(js_sample, str)
    assert 'console.log' in js_sample or 'function' in js_sample
    
    unknown_sample = create_sample_code('unknown_language')
    assert isinstance(unknown_sample, str)
    assert len(unknown_sample) > 0
    
    print("✓ test_create_sample_code passed")


def test_language_support():
    """Test that agent supports multiple languages"""
    agent = CodingAgent("MultiLingualBot")
    
    supported = agent.LANGUAGES.keys()
    assert 'python' in supported
    assert 'javascript' in supported
    assert 'java' in supported
    assert 'cpp' in supported
    assert 'go' in supported
    assert 'rust' in supported
    
    assert len(supported) >= 10  # Should support at least 10 languages
    print("✓ test_language_support passed")


def test_automatic_file_extension():
    """Test that file extensions are added automatically"""
    agent = CodingAgent("ExtBot")
    
    # Write code without extension
    code = "print('test')"
    result = agent.write_code('python', code, 'no_ext')
    
    assert result['success'] is True
    assert result['filename'].endswith('.py')
    
    # Cleanup
    if os.path.exists(result['filename']):
        os.remove(result['filename'])
    print("✓ test_automatic_file_extension passed")


def test_code_history():
    """Test that code history is tracked"""
    agent = CodingAgent("HistoryBot")
    
    # Write multiple files
    agent.write_code('python', "print('1')", 'hist1.py')
    agent.write_code('javascript', "console.log('2')", 'hist2.js')
    agent.write_code('python', "print('3')", 'hist3.py')
    
    assert len(agent.code_history) == 3
    assert agent.code_history[0]['language'] == 'python'
    assert agent.code_history[1]['language'] == 'javascript'
    
    # Cleanup
    os.remove('hist1.py')
    os.remove('hist2.js')
    os.remove('hist3.py')
    print("✓ test_code_history passed")


def run_all_tests():
    """Run all tests"""
    print("\nRunning coding_agent tests...\n")
    test_create_agent()
    test_think()
    test_get_funny_message()
    test_write_python_code()
    test_write_javascript_code()
    test_unsupported_language()
    test_validate_code()
    test_validate_unbalanced_braces()
    test_validate_nonexistent_file()
    test_build_python()
    test_build_invalid_python()
    test_build_nonexistent_file()
    test_suggest_improvements()
    test_get_stats()
    test_create_sample_code()
    test_language_support()
    test_automatic_file_extension()
    test_code_history()
    print("\n✅ All coding_agent tests passed!\n")


if __name__ == "__main__":
    run_all_tests()
