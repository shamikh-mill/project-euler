# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# O(n^2) solution (rip)

m = 0
for a in range(100, 1000): 
	for b in range(100, 1000): 
		num = a * b
		if (str(num) == str(num)[::-1]): 
			if num > m: 
				m = num 


print(m)
