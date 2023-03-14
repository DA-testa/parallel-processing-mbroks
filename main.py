# python3
import heapq
def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    threads = []
    for worker in range(n):
        heapq.heappush(threads,(0,worker))
    for j in range(m):
        time,worker=heapq.heappop(threads)

        output.append(str(str(worker)+" "+str(time)))

        heapq.heappush(threads,(time+data[j],worker))
        #print(threads)

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0
    nm = input()
    nm = nm.split()
    n = int(nm[0])
    m = int(nm[1])
    arr = input()
    data = map(int,arr.split())
    data = list(data)
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    print(*result, sep='\n')



if __name__ == "__main__":
    main()
