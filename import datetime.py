import datetime
import webbrowser

def speak(text):
    print("giriGIRI:", text)

def take_command():
    return input("You: ").lower()

def tell_time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {time}")

def play_music(command):
    song = command.replace("play", "").strip()
    if song:
        speak(f"Opening YouTube for {song}")
        webbrowser.open(f"https://www.youtube.com/results?search_query={song}")
    else:
        speak("Please tell me what to play")

def search_anything(command):
    topic = command.replace("search", "").strip()
    if topic:
        speak(f"Searching for {topic}")
        webbrowser.open(f"https://www.google.com/search?q={topic}")
    else:
        speak("What do you want me to search?")

def open_apps(command):
    if "spotify" in command:
        speak("Opening Spotify")
        webbrowser.open("https://open.spotify.com")

    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    else:
        speak("I don't know that application")

def run_assistant():
    speak("Hello! I am giriGIRI. How can I help you?")

    while True:
        command = take_command()

        if "time" in command:
            tell_time()

        elif "play" in command:
            play_music(command)

        elif "search" in command:
            search_anything(command)

        elif "open" in command:
            open_apps(command)

        elif "hello" in command:
            speak("Hello! How can I assist you?")

        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break

        elif command.strip() != "":
            speak("I can help with time, music, search, or open apps")

# Run
run_assistant()