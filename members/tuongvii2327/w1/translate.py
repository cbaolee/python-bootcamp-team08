# check the string have valid parentheses or not, return True if valid.
# Different with C++: Python not have stack type, so I use list with append and pop.
# Empty list is False, so "not stack" is used instead of st.empty().
def is_valid_parentheses(s: str) -> bool:
    stack: list[str] = []
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack
