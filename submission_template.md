# AI Code Review Assignment (Python)

## Candidate

- Name:Osama Seid
- Approximate time spent:80min

---

# Task 1 — Average Order Value

## 1) Code Review Findings

### Critical bugs

-The function divides by the total number of orders, including cancelled ones.
-This causes an incorrect average.
-If all orders are cancelled, the function will crash due to division by zero.

### Edge cases & risks

-Orders may miss the status or amount key.
-Order amounts may not be valid numbers.
-Empty input or all cancelled orders are not handled safely.

### Code quality / design issues

-The count variable does not match the filtered data.
-The logic in code does not match the explanation.

## 2) Proposed Fixes / Improvements

### Summary of changes

-Count only non-cancelled orders.
-Safely read order fields.
-Prevent division by zero.
-Convert amounts to numbers safely.

### Corrected code

See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

### Testing Considerations

If you were to test this function, what areas or scenarios would you focus on, and why?
-Orders with mixed statuses (active and cancelled).
-All orders cancelled.
-Missing keys in order data.
-Invalid or non-numeric amounts.
-Empty input list.
Why:
To make sure the function calculates the correct average, handles bad data safely, and does not crash.

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation

-Cancelled orders are still included in the divisor.
-The explanation does not describe the real behavior of the code.

### Rewritten explanation

-This function calculates the average order value by adding the amounts of non-cancelled orders and dividing by the number of valid orders, and it returns 0.0 if no valid orders are found.

## 4) Final Judgment

- Decision: Request Changes
- Justification: The original code gives wrong results and can crash in edge cases.
- Confidence & unknowns: High confidence after fixing logic and safety issues.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings

### Critical bugs

-The function treats any string containing @ as a valid email.
-This allows many invalid emails to pass.

### Edge cases & risks

-Non-string values may be counted incorrectly.
-Inputs like "@", "user@", or "@site" are invalid but accepted.
-The function does not clearly define what “valid” means.

### Code quality / design issues

-Validation logic is too weak.
-The explanation overstates correctness.

## 2) Proposed Fixes / Improvements

### Summary of changes

-Check that each value is a string.
-Ensure both parts of the email exist before and after @.
-Keep validation simple and honest.

### Corrected code

See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`.

### Testing Considerations

If you were to test this function, what areas or scenarios would you focus on, and why?
-Valid emails like user@example.com.
-Invalid emails with missing parts.
-Non-string inputs (None, numbers).
-Empty input list.
Why:
To confirm only proper email-like strings are counted and invalid inputs are ignored.

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation

-The function does not truly validate emails.
-It only checks for the presence of @.

### Rewritten explanation

-This function counts email-like strings by checking that the value is a string and contains text on both sides of @, and it performs only a basic check, not full email validation.

## 4) Final Judgment

- Decision: Request Changes
- Justification: The original logic is misleading and too permissive.
- Confidence & unknowns: Confident for basic validation use cases.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings

### Critical bugs

-The function divides by the full list length instead of valid values only.
-This leads to incorrect averages.
-Division by zero is possible.

### Edge cases & risks

-Values may be None or non-numeric.
-Converting invalid values to float can raise errors.
-All invalid values are not handled safely.

### Code quality / design issues

-Count variable does not match filtered values.
-Error handling is missing.

## 2) Proposed Fixes / Improvements

### Summary of changes

-Count only valid numeric values.
-Safely convert values to float.
-Return 0.0 if no valid values exist.

### Corrected code

See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations

If you were to test this function, what areas or scenarios would you focus on, and why?
-Mixed valid and invalid values.
-All values None.
-Non-numeric strings.
-Empty input list.
Why:
To ensure the function calculates the correct average, skips invalid data, and avoids division by zero.

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation

-The average is not accurate due to incorrect division.
-Error handling is not actually implemented.

### Rewritten explanation

-This function calculates the average using only valid numeric values by skipping None and non-numeric inputs, and it returns 0.0 if no valid values are found.

## 4) Final Judgment

- Decision: Request Changes
- Justification: The original implementation gives wrong results and may fail.
- Confidence & unknowns: High confidence after adding validation and safety checks.
