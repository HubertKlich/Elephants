#values
pom,result,count_of_elephants=0,0,0
cycle,elephant_mass,start,end=[],[],[],[]
minimal_weight_elephant = 6600 #Because max is 6500kg
#read data
with open('zadanie_B/slo1.in') as f:
    count=int(f.readline())
    target=[0] * count
    elephant_mass=f.readline().split()
    start=f.readline().split()
    end=f.readline().split()
    
for ele in end:
        target[int(ele)-1]=start[pom]
        pom+=1

for ele in range(count):
    cycle.append(False)
    minimal_weight_elephant = min(minimal_weight_elephant, int(elephant_mass[ele]))
    start[ele]=int(start[ele])-1
    
for ele in range(count):
    if cycle[ele]==False:
        sum_of_mass = 0
        after_change = ele
        minimum_weight = 6600
        pom = 0
        while True:
            minimum_weight=min(minimum_weight,int(elephant_mass[after_change]))
            sum_of_mass+=int(elephant_mass[after_change])
            after_change=int(target[after_change])-1
            cycle[after_change]=True
            pom+=1
            if after_change==ele:
                break
        result+=min(sum_of_mass+(pom-2)*minimum_weight, sum_of_mass + minimum_weight + (pom + 1) * minimal_weight_elephant)
        
print(result)
