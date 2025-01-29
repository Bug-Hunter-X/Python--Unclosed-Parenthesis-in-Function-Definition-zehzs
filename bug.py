def function_with_unclosed_parentheses(a, b):
    result = a + b
    return result # Missing closing parenthesis

# Example usage (it might work without errors, but it's bad code):
print(function_with_unclosed_parentheses(5, 3))