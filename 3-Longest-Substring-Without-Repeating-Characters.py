class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize a set to store unique characters in the current window
        char_set = set()
        
        # Initialize the start pointer and the variable to store the maximum length
        start = 0
        max_length = 0
        
        # Iterate through the string using the end pointer
        for end in range(len(s)):
            # If the character at the end pointer is already in the set, it means there is a repetition
            while s[end] in char_set:
                # Remove the character at the start pointer from the set
                char_set.remove(s[start])
                # Move the start pointer to the right
                start += 1
            
            # Add the current character to the set
            char_set.add(s[end])
            # Update the maximum length with the size of the current window
            max_length = max(max_length, end - start + 1)
        
        # Return the maximum length of the substring without repeating characters
        return max_length