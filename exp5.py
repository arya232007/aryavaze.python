tasks=[]

tasks.append("study")
tasks.append("exercise")
tasks.append("sleep")

tasks[1]="play"
tasks.remove("sleep")
tasks.sort()

tasks_tuple=tuple(tasks)

for t in tasks_tuple:
    print(t)
