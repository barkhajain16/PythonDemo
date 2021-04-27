a = [1,2,3,4,5,6,1,1,1,2,2,23,3,3,3]
a.sort()
print(a)
count = 0
i = 0
while i < len(a):
	print(a[i],a.count(a[i]))
	i = i + a.count(a[i])

	