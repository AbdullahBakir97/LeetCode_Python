class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Initialize the result and carry
        result = []
        carry = 0
        
        # Pointers for a and b
        i, j = len(a) - 1, len(b) - 1
        
        # Loop until both strings are processed or there's a carry left
        while i >= 0 or j >= 0 or carry:
            total_sum = carry
            
            if i >= 0:
                total_sum += int(a[i])
                i -= 1
            
            if j >= 0:
                total_sum += int(b[j])
                j -= 1
            
            # Compute the new bit and carry
            carry = total_sum // 2
            result.append(str(total_sum % 2))
        
        # The result is in reverse order, reverse it to get the final output
        return ''.join(result[::-1])