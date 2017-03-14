# This program minimizes the weighted sum of completion times
# for a series of jobs each with a weight and length

def calcWeightedSum(filename, scoring_function):
	job_list = getJobList(filename)
	sortByScore(job_list, scoring_function)
	weighted_sum = getWeightedSum(job_list)
	return weighted_sum

# get job list from file where each job is in the form
# (job_weight, job_length)
def getJobList(filename):
	f = open(filename, 'r')
	list_by_line = f.read().split('\n')
	job_list = []
	for line in list_by_line[1:]:
		line_as_list = line.split(' ')
		job = (int(line_as_list[0]), int(line_as_list[1]))
		job_list.append(job)
	return job_list

# sort list according to score in descending order
def sortByScore(job_list, scoring_function):
	job_list.sort(key=lambda t: (scoring_function(t[0], t[1]), t[0]), reverse=True)

# find out the weighted sum of completion times
# plucking out one element at a time for heap
def getWeightedSum(job_list):
	current_completion_time = 0
	weighted_sum = 0
	for job in job_list:
		current_completion_time += job[1]
		weighted_sum += current_completion_time * job[0]
	return weighted_sum

# bad
def getScoreAsWeightMinusLength(weight, length):
	return weight - length

# good
def getScoreAsWeightOverLength(weight, length):
	return weight / length

# TESTING
print(calcWeightedSum('jobs.txt', getScoreAsWeightOverLength))
# test = [[5,3],[11,8],[4, 0],[20,17]]
# sort = sorted(test, key=lambda t: (getScoreAsWeightMinusLength(t[0], t[1]), t[0]), reverse=True)
# print(sort)
