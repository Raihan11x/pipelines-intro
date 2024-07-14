import pytest
from math_quiz import generate_problem, OPERATORS, MIN_OPERAND, MAX_OPERAND

def test_generate_problem():
    expr, answer = generate_problem()
    
    # Check that the expression is a string and the answer is an int or float
    assert isinstance(expr, str)
    assert isinstance(answer, (int, float))
    
    # Check that the expression contains a valid operator
    assert any(op in expr for op in OPERATORS)
    
    # Extract operands from the expression
    left, operator, right = expr.split()
    
    # Check that operands are within the correct range
    assert MIN_OPERAND <= int(left) <= MAX_OPERAND
    assert MIN_OPERAND <= int(right) <= MAX_OPERAND
    
    # Verify that the evaluated expression matches the returned answer
    assert eval(expr) == answer
