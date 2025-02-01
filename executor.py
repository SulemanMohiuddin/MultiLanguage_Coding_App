import subprocess
import os

def run_code(user_code, language):
    if language == "python":
        return run_python(user_code)
    elif language == "cpp":
        return run_cpp(user_code)
    elif language == "java":
        return run_java(user_code)
    return "", "Unsupported language"

def run_python(user_code):
    filename = "user_script.py"
    with open(filename, "w") as f:
        f.write(user_code)

    try:
        result = subprocess.run(["python3", filename], capture_output=True, text=True, timeout=2)
        return result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return "", "Execution Timeout"

def run_cpp(user_code):
    cpp_filename = "user_code.cpp"
    exe_filename = "user_code"

    with open(cpp_filename, "w") as f:
        f.write(user_code)

    compile_result = subprocess.run(["g++", cpp_filename, "-o", exe_filename], capture_output=True, text=True)

    if compile_result.returncode != 0:
        return "", compile_result.stderr

    try:
        run_result = subprocess.run(["./" + exe_filename], capture_output=True, text=True, timeout=2)
        return run_result.stdout, run_result.stderr
    except subprocess.TimeoutExpired:
        return "", "Execution Timeout"

def run_java(user_code):
    java_filename = "UserCode.java"
    class_filename = "UserCode"

    # Ensure the class name matches the file
    user_code_wrapped = f"""
public class UserCode {{
    public static void main(String[] args) {{
        {user_code}
    }}
}}
"""

    with open(java_filename, "w") as f:
        f.write(user_code_wrapped)

    # Compile Java code
    compile_result = subprocess.run(
        ["javac", java_filename],
        capture_output=True,
        text=True
    )

    if compile_result.returncode != 0:
        return "", compile_result.stderr

    # Run compiled Java program
    try:
        run_result = subprocess.run(
            ["java", class_filename],
            capture_output=True,
            text=True,
            timeout=2
        )
        return run_result.stdout, run_result.stderr
    except subprocess.TimeoutExpired:
        return "", "Execution Timeout"

