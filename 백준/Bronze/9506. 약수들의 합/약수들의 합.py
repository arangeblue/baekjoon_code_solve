import sys

def measure(n):
    lists = [i for i in range(1, n//2 + 1) if n%i==0]
    return lists
        

while 1:
    n = int(sys.stdin.readline())
    if n == -1:
        break
    
    lists = measure(n)
    if n != sum(lists):
        print(f"{n} is NOT perfect.")
    
    else:
        last_str = " + ".join(map(str,lists))
        print(f"{n} = {last_str}")
    