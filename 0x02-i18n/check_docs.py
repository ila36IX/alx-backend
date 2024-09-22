#!/bin/env python3
import ast
import sys
import importlib.util

def check_docstrings(filename):
    with open(filename, 'r') as file:
        node = ast.parse(file.read())

    module_name = filename.replace('.py', '')
    spec = importlib.util.spec_from_file_location(module_name, filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    issues = []

    # Check module docstring
    if not ast.get_docstring(node):
        issues.append(f"Module '{module_name}' is missing a docstring")

    for item in node.body:
        if isinstance(item, ast.ClassDef):
            class_name = item.name
            class_obj = getattr(module, class_name)

            # Check class docstring
            if not ast.get_docstring(item):
                issues.append(f"Class '{class_name}' is missing a docstring")

            for method in item.body:
                if isinstance(method, ast.FunctionDef):
                    method_name = method.name
                    method_obj = getattr(class_obj, method_name)

                    # Check method docstring
                    if not ast.get_docstring(method):
                        issues.append(f"Method '{class_name}.{method_name}' is missing a docstring")

        elif isinstance(item, ast.FunctionDef):
            func_name = item.name
            func_obj = getattr(module, func_name)

            # Check function docstring
            if not ast.get_docstring(item):
                issues.append(f"Function '{func_name}' is missing a docstring")

    return issues

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python documentation_checker.py <python_file>")
        sys.exit(1)

    filename = sys.argv[1]
    issues = check_docstrings(filename)

    if issues:
        print("Documentation issues found:")
        for issue in issues:
            print(f"- {issue}")
    else:
        print("All items are properly documented!")
