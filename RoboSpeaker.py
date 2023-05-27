# say cmd use in macOs
# import os

# if __name__ == '__main__':
#     print("Welcome to RoboSpeaker 1.0.1, Created by @rahul_jerthi")
    
#     x = input("Enter what do you wana to speak:")
#     command = f"say {x}"
#     os.system(command)
    
    
    
#for windows use this moduel q


import pyttsx3
print("Welcome to RoboSpeaker 1.0.1, Created by @rahul_jerthi")
    
engine = pyttsx3.init()
    
while True:
        x = input("Enter what do you want to speak (press 'q' to quit): ")
        
        if x.lower() == 'q':
            break
        
        engine.say(x)
        engine.runAndWait()
