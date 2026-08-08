import speech_recognition as sr
import pyttsx3


class SpeechManager:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

        self.engine.setProperty("rate", 170)
        self.engine.setProperty("volume", 1.0)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):

        with sr.Microphone() as source:

            print("Listening...")

            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            try:
                audio = self.recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=10
                )

                text = self.recognizer.recognize_google(audio)

                print("You:", text)

                return text

            except sr.WaitTimeoutError:
                return ""

            except sr.UnknownValueError:
                return ""

            except sr.RequestError:
                return ""
