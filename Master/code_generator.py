import random 

def run_man():
    print('5 digit code has been set. Digits in range 1 to 8. You have 5 turns to break it.')

    code = set()
    while len(code) < 5:
        code.add(random.randint(1, 8))

        code = list(code)




    think = 5
    while think >=1:
        correct = 0
        incorrect = 0
        User_input = input('Input 5 digit code: ')
        think -= 1

        if len(User_input) !=5 or not (User_input.isdigit()) or '9' in User_input or '0' in User_input:
            print('Please enter exactly 5 digits.')
        else:
                
            for i in range(0,len(code)):
                code_int = int(User_input[i])

                if code_int in code:
                    if code_int == code[i]:
                        correct += 1
                    else:
                        incorrect += 1

            print(f"Number of correct digits in correct place:     {correct}")
            print(f"Number of correct digits not in correct place: {incorrect}")

            if correct == 5:
                print('Congratulations! You are a codebreaker!')
                response = list(map(str,code))
                print(f"The code was: {''.join(response)}")
                break
            else:
                print(f"Turns left: {think}")
            if think == 0:
                response = list(map(str,code))
                print(f"The code was: {''.join(response)}")

if __name__ == "__main__":
    run_man()
