A = list(map(int,input().split()))
B = int(input())

def sums3(A,B):
	A.sort()
	min_diff = float("inf")
	ans = 99999999
	for i in range(len(A) - 2):
		j = i+1
		k = len(A) - 1
		while(j<k):
			num = A[i] + A[j] + A[k]
			if num == B:
				return B
			if abs(num - B) < min_diff:
					min_diff = abs(num - B)
					ans = num
			if(num < B):
				j+=1
			else:
				k-=1
	
	return ans
	

print(sums3(A,B))

