import ast
import inspect
from incomplete_main import find_powerful_sword

run_cases = [
    ([1, 2, 3, 4, 5, 6], [5, 6]),
    ([5, 10, 2, 8, 3], [5, 10, 8]),
    ([1, 2, 3, 4], []),
]

submit_cases = run_cases + [
    ([], []),
    ([10, 20, 30], [10, 20, 30]),
    ([0, 4, 5, 4, 6], [5, 6]),
]


def test_syntax():
    print("-" * 40)
    print("Checking if list comprehension is used...")
    print("Expected:\nFunction should be implemented using a list comprehension and no traditional for-loops.")
    try:
        source = inspect.getsource(find_powerful_sword)
        tree = ast.parse(source)
        
        has_list_comp = False
        has_for_loop = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ListComp):
                has_list_comp = True
            elif isinstance(node, ast.For):
                has_for_loop = True
                
        if not has_list_comp:
            print("Actual:\nNo list comprehension found in the function definition.")
            print("Fail")
            return False
        if has_for_loop:
            print("Actual:\nTraditional for-loop found in the function definition.")
            print("Fail")
            return False
            
        print("Actual:\nList comprehension used correctly!")
        print("Pass")
        return True
    except Exception as e:
        print(f"Actual:\nError checking code structure: {e}")
        print("Fail")
        return False


def test(input1, expected_output):
    print("-" * 40)
    print(f"Input:\n{input1}")
    print(f"Expected:\n{expected_output}")
    try:
        result = find_powerful_sword(input1)
    except Exception as e:
        print(f"Error: {e}")
        return False
    print(f"Actual:\n{result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    
    # Run syntax/AST check first
    if test_syntax():
        passed += 1
    else:
        failed += 1
        
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
            
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
