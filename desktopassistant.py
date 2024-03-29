import pyttsx3
import speech_recognition as sr
import webbrowser
import pyaudio
import datetime
import wikipedia

def takeCommand():
    r = sr.Recognizer()


        with sr.Microphone() as source:
        speak('I am on the way to help you please tell I am listening')
        print("Waiting....")

        # seconds of non-speaking audio before
        # a phrase is considered complete
        r.pause_threshold = 0.9
        audio = r.listen(source)

        # Now we will be using the try and catch
        # method so that if sound is recognized
        # it is good else we will have exception
        # handling
        try:


            # for Listening the command in indian
            # english we can also use 'hi-In'
            # for hindi recognizing
            Query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", Query)

        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"

        return Query


def speak(audio):
    engine = pyttsx3.init()
    # getter method(gets the current value
    # of engine property)
    voices = engine.getProperty('voices')

    # setter method .[0]=male voice and
    # [1]=female voice in set Property.
    engine.setProperty('voice', voices[1].id)

    # Method for the speaking of the assistant
    engine.say(audio)

    # Blocks while processing all the currently
    # queued commands
    engine.runAndWait()


def tellDay():
    # This function is for telling the
    # day of the week
    day = datetime.datetime.today().weekday()+1

    # this line tells us about the number
    # that will help us in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)


'''def tellTime(self):
    # This method will give the time
    time = str(datetime.datetime.now())

    # 
    print(time)
    hour = time[11:13]
    min = time[14:16]
    self.speak(self, "The time is sir" + hour + "Hours and" + min + "Minutes")'''


def Hello():
    # This function is for when the assistant
    # is called it will say hello and then
    # take query
    speak("hello sir I am your desktop assistant. /Tell me how may I help you")


def Take_query():
    # calling the Hello function for
    # making it more interactive
    Hello()

    # This loop is infinite as it will take
    # our queries continuously until and unless
    # we do not say bye to exit or terminate
    # the program
    while (True):

        # taking the query and making it into
        # lower case so that most of the times
        # query matches and we get the perfect
        # output
        query = takeCommand().lower()
        if "open copy assignment.com" in query:
            speak("Opening Copy assignmnet ")

            # in the open method we just to give the link
            # of the website and it automatically open
            # it in your default browser
            webbrowser.open("www.copyassignment.com")
            continue

        elif "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue

        elif "what is the day" in query:
            tellDay()
            continue

        elif "tell me the time" in query:
            tellTime()
            continue

        # this will exit and terminate the program
        elif "bye-bye" in query:
            speak("Bye ,Have a nice day sir")
            exit()

        elif "open wikipedia" in query:

            # if any one wants to have a information
            # from wikipedia
            speak("Checking the wikipedia ")

            speak("According to wikipedia")
            webbrowser.open("www.wikipedia.com")


        elif "tell me your name" in query:
            speak("I am Marry. Your desktop Assistant")


if __name__ == '__main__':

    Take_query()
