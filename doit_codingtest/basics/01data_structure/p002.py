# 002 문제 : 평균 구하기

## <입력>
# 1번째 줄에 시험을 본 과목의 개수 N이 주어진다. 해당 값은 1,000보다 작거나 같다.
# 2번째 줄에 세준이의 현재 성적이 주어진다.
# 해당 값은 100보다 작거나 같은, 음이 아닌 정수이고, 적어도 1개의 값은 0보다 크다.

## <출력>
# 1번째 줄에 새로운 평균을 출력한다. 실제제 정답과 출력값의 절대 오차 또는 상대 오차가 10 -2승 이하이면 정답이다.

n = input()
mylist = list(map(int, input().split()))
mymax = max(mylist)
sum = sum(mylist)

print(sum * 100 / mymax / int(n))