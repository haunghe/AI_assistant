import speech_recognition as sr
import pyttsx3
import openai

openai.api_key = "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"

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

conversation = ""
user_name = "HauNghe"
bot_name = "HonQue"

while True:
    with mic as source:
        print("Hon Que: I'm listening to you...")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
    print("I've heard your question.Wait for me...")

    try:
        user_input = r.recognize_google(audio)
    except:
        continue

    prompt = user_name + ":" + user_input + "\n" + bot_name + ":"
    conversation += prompt

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=conversation,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    response_str = response["choices"][0]["text"].replace("\n", "")
    response_str = response_str.split(
        user_name + ":", 1)[0].split(bot_name + ":", 1)[0]

    conversation += response_str + "\n"
    print(response_str)

    engine.say(response_str)
    engine.runAndWait()
