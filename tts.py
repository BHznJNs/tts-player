import requests, json

TOKEN = "ttsmaker_demo_token"
URL = "https://api.ttsmaker.cn/v1/create-tts-order"

MAIN_URL = "https://s2p1.tts-file.com/file/"
ALTERNATE_URL = "https://tts-file2.com/s2p1/file/"

HEADERS = {'Content-Type': 'application/json; charset=utf-8'}

def req(text: str):
    res = requests.post(URL, headers=HEADERS, data=json.dumps({
        'token': TOKEN,
        'text': text,
        'voice_id': 1501,
        'audio_format': 'mp3',
        'audio_speed': 1,
        'audio_volume': 0,
        'text_paragraph_pause_time': 0
    }))

    res_obj = json.loads(res.content)
    if res_obj["status"] == "success":
        audio_url = res_obj["audio_file_url"]
        print("[TTS logging] Succeeded requested, Audio url: {}.".format(audio_url))

        res = requests.get(audio_url.replace(MAIN_URL, ALTERNATE_URL))
        # save audio file
        with open("audio.mp3", "wb") as f:
            print("[TTS logging] Audio downloaded.")
            f.write(res.content)
    else:
        print("[TTS error] Request error.")


