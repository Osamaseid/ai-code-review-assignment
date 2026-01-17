# Notes

## Assumptions

- Input data may be imperfect and come from external sources.
- Functions should fail safely instead of raising errors.
- Returning `0.0` for empty or invalid input is acceptable for these tasks.

## Known Limitations

- Email validation is intentionally basic and does not follow full email standards.
- Order and measurement validation focuses on safety, not strict data enforcement.
- These functions prioritize correctness and clarity over performance optimizations.

## Alternative Approaches Considered

- Using regular expressions for email validation, but avoided to keep logic simple.
- Raising exceptions instead of returning `0.0`, but chose safer defaults for general use.
- Using list comprehensions, but kept loops for readability and clearer error handling.
