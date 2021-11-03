"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

"""

# Time: O(n^4)
def letterCombinations(digits: str) -> List[str]:
    # Create dictionary to store mappings values
    mappings = {2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"]}
    
    # If digits is empty return an empty array
    if digits == "":
        return []
    
    # Set the out array to have the first digits characters.
    out = mappings[int(digits[0])]
    
    # Since we already have the first digit, we iterate from the 2nd digit onwards.
    for i in digits[1:]:
        chars = mappings[int(i)] # Store the chracters associated with this digit
        out = out * len(chars) # Increase the size of the output array to account for new possible character combinations
        count = 0 # Count will run from 0 to length of the output array
        mapVal = 0 # MapVal tells us which value from Char to add to the string. It will be between 0 and len(chars)
        mapCount = 0 # Map Count ensures we stay on the same character until ready to move on.
        while count < len(out):
            if mapCount == (len(out) / len(chars)): 
                mapVal += 1
                mapCount = 0
            out[count] = out[count] + chars[mapVal]
            mapCount += 1
            count += 1

    return out