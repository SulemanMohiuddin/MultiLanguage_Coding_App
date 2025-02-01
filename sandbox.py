import json
from executor import run_code

def validate_solution(user_code, language, problem_id):
    with open("test_cases.json", "r") as f:
        test_cases = json.load(f)["problems"]

    for problem in test_cases:
        if problem["id"] == problem_id:
            visible_cases = problem["visible_test_cases"]
            hidden_cases = problem["hidden_test_cases"]

            for test in visible_cases + hidden_cases:
                input_data = test["input"]
                expected_output = str(test["expected_output"])

                user_output, error = run_code(user_code, language)
                if error:
                    return f"Error: {error}"
                if user_output.strip() != expected_output:
                    return "Wrong Answer"

            return "Correct"

    return "Problem not found"
