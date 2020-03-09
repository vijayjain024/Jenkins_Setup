"""
You are given a list of jobs to be done, where each job is represented by a start time and end time. 
Two jobs are compatible if they don't overlap. Find the largest subset of compatible jobs.

For example, given the following jobs (there is no guarantee that jobs will be sorted):

[(0, 6),
(1, 4),
(3, 5),
(3, 8),
(4, 7),
(5, 9),
(6, 10),
(8, 11)]
Return:

[(1, 4),
(4, 7),
(8, 11)]

Test case 2:

[(1,3),
(3,5),
(3,8),
(6,8),
(9, 12)
]
Return:

[
]


#What do you mean by overlap? would (1,3) and (3,5) be classified as overlapping? ans - no
#what do you mean by largest subset? Is it the maximum number of jobs that can be finished or the maximum time range covered
#for eg is [(0,6),(6,9)] a larger subset than [(1,3),(3,5),(5,7)]

Sort the jobs in the order of start time
start with each job and find the next job which has a start time greater than or equal to current job end time. 


jobs1 = [(1,3), (3,5), (3,7), (6,8),(7,9), (9, 12)] # multiple options
jobs2 = [(1,5), (2,3), (3,4), (4,6), (4,8), (6,9), (8,9)] #
jobs3 = [(1,3), (3,5), (3,7), (6,10),(7,9), (9, 12)] # multiple options
jobs4 = [(1,3), (3,5), (3,7), (6,10),(7,9), (9, 12)] # multiple options


"""
jobs = [(0, 6), (1, 4), (3, 8), (3, 5), (4, 7), (5, 9), (6, 10), (8, 11)]
sorted_jobs = sorted(jobs, key=lambda element: (element[0], element[1]))

#print(sorted_jobs)

jobs_dict = {}


for i in range(len(sorted_jobs)-1):
	start = sorted_jobs[0]
	count = 1
	largest = sorted_jobs	


for i in range(len(sorted_jobs)-1):
	count = 1
	largest = []
	largest.append(sorted_jobs[i])
	#start = sorted_jobs[i]
	#start = sorted_jobs[0]
	#print('element {} - largest is {} and start is {}'.format(i, largest, start))
	for j in range(i + 1, len(sorted_jobs)):
		#print(sorted_jobs[j][0])
		if start[1] <= sorted_jobs[j][0]:
			count += 1
			largest.append(sorted_jobs[j])
			start = sorted_jobs[j]
	#		print(start)
		else:
			continue
	#print('For {} th element: {} is the largest'.format(i, largest))
	#need to find a way to story multiple values for duplicate keys
	#jobs_dict[count] = largest
	if count in jobs_dict:
		jobs_dict[count].append(largest)
	else:
		jobs_dict[count] = largest

for key, value in jobs_dict.items():
	print('{} - {}'.format(key, value))				

print('Answer is : {}'.format(jobs_dict[max(jobs_dict)]))







