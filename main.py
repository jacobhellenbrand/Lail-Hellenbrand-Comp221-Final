from math import sin,cos,pi

# This is a FFT function that computes DFT of a sequence of numbers
# Input is a list of numbers and using FFT, will return their DFT outputs
def fft(a):
	n = len(a)
    #check base case
	if n == 1:
		return [a[0]]
	# Make our complex unity numbers
	theta = -2*pi/n
	w = list( complex(cos(theta*i), sin(theta*i)) for i in range(n) ) 
	# make even and odd parts 
	a_Even = a[0::2]
	a_Odd = a[1::2]
	# Recursive calls on n/2 size
	f_even = fft(a_Even) 
	f_Odd = fft(a_Odd)
	# Initialize output array
	F = [0]*n
	middle = n//2
	for k in range(n//2):
        #store even and odd parts 
		w_f_Oddk = w[k] * f_Odd[k]
		f_even_k = f_even[k]
		#compute values for out put array
		F[k]		 = f_even_k + w_f_Oddk
		F[k + middle] = f_even_k - w_f_Oddk
        
	F = [val.real if val.imag == 0 else val for val in F]
	return F


# Test cases
def run_test(input_data, expected_output):
    output = fft(input_data)
    print("Input:", input_data)
    print("Expected Output:", expected_output)
    print("Actual Output:", output)
    print("Test Passed:", output == expected_output)
    print()


if __name__ == '__main__':
    # Test cases
    #10, 0+4J, 0+2J, 0+4J, -10, 0+-4J, 0+-2J, 0+-4J
    test_cases = [
        #Check base input
        ([1, 2, 3, 4], [10.0, (-2.0+2.0j), -2.0, (-2.0-2.0j)]),
        #check sparse array
        ([1, 0, 0, 0, 2, 0, 0, 0], [3.0, (-1), (3), (-1), 3.0, (-1), (3), (-1)]),
        #check all 0
        ([0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]),
        #check all same number
        ([1, 1, 1, 1], [4.0] + [0.0j] * 3),
        #check negatives
        ([-1,-2,-3,-4], [-10, 2+-2J, 2, 2+2J])
    ]

    # Run test cases
    for idx, (input_data, expected_output) in enumerate(test_cases, start=1):
        print("Test Case", idx)
        run_test(input_data, expected_output)