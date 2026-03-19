import random
def guess_number_game():
    secret_number = random.randint(1, 20)
    print("1부터 20 사이의 숫자를 하나 생각했습니다. 맞춰보세요!")
    while True:
        try:
            guess = int(input("숫자 입력: "))
            
            if guess < secret_number:
                print("UP! (더 큰 숫자입니다)")
            elif guess > secret_number:
                print("DOWN! (더 작은 숫자입니다)")
            else:
                print(f"정답입니다! 숫자는 {secret_number} 였습니다.")
                break # 정답을 맞추면 반복문을 빠져나옵니다.
        except ValueError:
            print("잘못된 입력입니다. '숫자'만 입력해 주세요.")
if __name__ == "__main__":
    guess_number_game()

