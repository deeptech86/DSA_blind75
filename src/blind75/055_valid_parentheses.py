"""
Problem: Valid Parentheses
Technique: Stack
"""

def valid_parentheses(s):
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.
    
    Args:
        s: str - String of parentheses
        
    Returns:
        bool - True if the input string is valid, False otherwise
    """
    # TODO: Implement solution
    slst=[]
    for char in s:
        if char in ['(',  '{',  '[' ]:
            slst.append(char)
        else:
            # if char in [')',  '}',  ']' ]:
                if len(slst) >0 :
                    if slst[-1]=='(' and char == ')' or slst[-1]=='{' and char == '}' or slst[-1]=='[' and char == ']' :
                        slst.remove( slst[-1])
    if len(slst)!=0:
        return False
    return True



# Example 1
# Input: s = "()"
# Output: True
# Explanation: The parentheses are matched and in the correct order

# Example 2
# Input: s = "()[]{}"
# Output: True
# Explanation: All types of parentheses are matched and in the correct order

s = "()[]{"
print(valid_parentheses(s))