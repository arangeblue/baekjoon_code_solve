# 입력은 여러 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 10,000이 넘지않는 두 자연수로 이루어져 있다. 마지막 줄에는 0이 2개 주어진다. 두 수가 같은 경우는 없다.
# 각 테스트 케이스마다 첫 번째 숫자가 두 번째 숫자의 약수라면 factor를, 배수라면 multiple을, 둘 다 아니라면 neither를 출력한다.
import sys


while 1:
    first, second = map(int,sys.stdin.readline().split())
    
    if first == 0 and second == 0:
        break
    
    if first<second and second % first == 0:
        print("factor")
    elif first > second and first % second == 0:
        print("multiple")
    else:
        print('neither')