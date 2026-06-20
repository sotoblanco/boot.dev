import ast
import inspect
from incomplete_main import track_goblin_rooms

run_cases = [
    (["goblin", "empty", "chest", "goblin"], [0, 3]),
    (["empty", "empty", "dragon"], []),
    (["goblin", "goblin", "goblin"], [0, 1, 2]),
]

submit_cases = run_cases + [
    ([], []),
    (["orc", "goblin", "troll", "goblin", "chest"], [1, 3]),
    (["goblin"], [0]),
]


def test_syntax():
    print("-" * 40)
    try:
        source = inspect.getsource(track_goblin_rooms)
        tree = ast.parse(source)
        
        has_enumerate = False
        has_manual_range_len = False
        
        for node in ast.walk(tree):
            if isinstance(node, ast.For):
                if isinstance(node.iter, ast.Call) and isinstance(node.iter.func, ast.Name):
                    if node.iter.func.id == 'enumerate':
                        has_enumerate = True
                    elif node.iter.func.id == 'range':
                        for arg in node.iter.args:
                            if isinstance(arg, ast.Call) and isinstance(arg.func, ast.Name):
                                if arg.func.id == 'len':
                                    has_manual_range_len = True
                                    
        if not has_enumerate:
            print("Actual:\nNo call to enumerate found in the loop.")
            print("Fail")
            return False
        if has_manual_range_len:
            print("Actual:\nUsed range(len(...)) instead of enumerate.")
            print("Fail")
            return False
            
        print("Actual:\nEnumerate used correctly!")
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
        result = track_goblin_rooms(input1)
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
