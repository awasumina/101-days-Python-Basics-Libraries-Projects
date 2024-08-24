from time import *
import random

def mistakes(partest, usertest):
    error = 0
    min_length = min(len(partest), len(usertest))

    for i in range(min_length):
        if partest[i] != usertest[i]:
            error += 1

    # Handle cases where user input is longer or shorter than partest
    error += abs(len(partest) - len(usertest))

    return error


def speed_test(time_s, time_e, userinput) :
    
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    
    speed = len(userinput) / time_R
    return round(speed)
    
if __name__ == '__main__' :
    
    while True :
        check = input("Ready to test y/n? :")
        
        if check == "y" :
            
            test = [" As the stars began to twinkle in the darkening sky, the world settled into a peaceful slumber."," It was a perfect moment, a pause in time, where nature's beauty wrapped the world in a comforting embrace. ", "The sun dipped below the horizon, casting a warm, golden glow across the tranquil lake.", "Birds chirped in the nearby trees, serenading the evening with their melodious tunes. ", "A gentle breeze rustled the leaves, bringing with it the scent of blooming flowers."   
            ]
            
            test1 = random.choice(test)
            print("***** Typing Speed *****")
            print(test1)

            time_1 = time() # time before input
            test_input = input("Enter : ")
            time_2 = time() # time after input

            print('Speed :', speed_test(time_1, time_2 , test_input ), "letters/sec")
            print("Mistakes :", mistakes(test1, test_input))
            
        elif check == "n":
            
            print("Thankyou ")
            break
        
        
        else :
            print("Invalid Choice")