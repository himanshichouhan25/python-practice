#question 2 : install an external module and use it to perform an operation. (use pip to install the module)
import pyttsx3
engine = pyttsx3.init()
engine.say("Hello, How are you?")
engine.runAndWait()
