A = list(map(str,input().split()))

print(A)
ary = [''.join(sorted(x)) for x in A ]
ans1 = []
s = set()
for i in range(0,len(ary)):
	ans2 = []
	ans2.append(i+1)
	if ary[i] not in s:
		s.add(ary[i])
		for j in range(i+1,len(ary)):
			if ary[i] == ary [j]:
				ans2.append(j+1)
		ans1.append(ans2)

print(ans1)