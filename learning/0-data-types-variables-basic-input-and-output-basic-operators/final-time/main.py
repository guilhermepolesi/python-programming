# Your task is to prepare a simple code capable of evaluating the end time of a period of time
# given as a number of minutes (it can be arbitrarily large).
# The initial time is given as a pair of hours (0.. 23) and minutes (0.. 59).
# The result must be printed to the console.

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

init_mins = hour * 60 + mins

final_mins = (init_mins + dura) % (24 * 60)

end_time = final_mins // 60
end_mins = final_mins % 60

print(str(end_time) + ":" + str(end_mins))