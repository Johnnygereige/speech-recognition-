import speech_recognition as sr

def main():
    # Initialize recognizer class (for recognizing speech)
    recognizer = sr.Recognizer()

    # Using the microphone as the audio source
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source)  # Adjusts for ambient noise
        print("Please say something...")
        audio = recognizer.listen(source)  # Listens for the first phrase and extracts it into audio data

        try:
            print("Recognizing...")
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            print("You said: {}".format(text))
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")

if __name__ == "__main__":
    main()
