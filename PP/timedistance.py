# def timeToMins(time):
#     # Convert "HH:MM" format to total minutes
#     hours, minutes = map(int, time.split(':'))  # Split on colon, not whitespace
#     return hours * 60 + minutes

# def find(timeList):
#     # Step 1: Convert all times to minutes
#     minsList = [timeToMins(time) for time in timeList]
    
#     # Step 2: Sort the list of times in minutes
#     minsList.sort()
    
#     # Step 3: Initialize the minimum difference with infinity
#     min_diff = float('inf')
    
#     # Step 4: Compute differences between consecutive time points
#     for i in range(1, len(minsList)):
#         min_diff = min(min_diff, minsList[i] - minsList[i - 1])
    
#     # Step 5: Compute the wrap-around difference (last and first time points)
#     wrapAroundDiff = (1440 + minsList[0] - minsList[-1]) % 1440
#     min_diff = min(min_diff, wrapAroundDiff)
    
#     return min_diff

# # Example usage:
# timeList = ["23:59", "00:00", "12:34"]
# print(find(timeList))  # Output should be 1

def time_to_minutes(time):
    hours, minutes = map(int, time.split(':'))
    return hours * 60 + minutes

def find_min_difference(time_points):
    minutes_list = [time_to_minutes(time) for time in time_points]
    minutes_list.sort()
    
    min_diff = float('inf')
    
    for i in range(1, len(minutes_list)):
        min_diff = min(min_diff, minutes_list[i] - minutes_list[i - 1])
    
    wrap_around_diff = (1440 + minutes_list[0] - minutes_list[-1]) % 1440
    min_diff = min(min_diff, wrap_around_diff)
    
    return min_diff

time_points = ["23:59", "00:00", "12:34"]
print(find_min_difference(time_points))  # Output: 1
