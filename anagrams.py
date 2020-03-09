"""
Given an array of strings, group anagrams together.

For example, given the following array:

['eat', 'ate', 'apt', 'pat', 'tea', 'now']
Return:

[['eat', 'ate', 'tea'],
 ['apt', 'pat'],
 ['now']]


"""

l = ['eat', 'ate', 'apt', 'pat', 'tea', 'now', 'ateate']
ans = {}
for index, item in enumerate(l):
	temp = ''.join(sorted(item))
	if temp in ans:
		ans[temp].append(item)

	else:
		ans[temp] = [item]	
			
print(ans)

lans = []

for k,v in ans.items():
	lans.append(v)

print(lans)	