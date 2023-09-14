import requests, youtube_dl, openai
from time import sleep

yt_link = "https://www.youtube.com/watch?v=VXSPKjypoO8"

assembly_auth = "2a685c477946418eabb2006deb31508f"
openai_auth = "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"

def download_yt(link):
    headers = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
            'preferredquality': '192',
            }],
        'ffmpeg-location': './',
        'outtmpl': "./%(id)s.%(ext)s",
    }
    _id = link.strip()
    meta = youtube_dl.YoutubeDL(headers).extract_info(_id)
    save_location = meta['id'] + ".m4a"
    return save_location

def upload(loc):
    url = "https://api.assemblyai.com/v2/upload"
    headers = {'authorization': assembly_auth}
    def read_file(loc):
        with open(loc, 'rb') as f:
            while True:
                data = f.read(5242880)
                if not data: 
                    break 
                yield data

    upload_response = requests.post(url, headers=headers, data=read_file(loc) )
    print("upload_url:", upload_response.json()["upload_url"]) 
    return upload_response.json()["upload_url"]

def submit_request(url):
    endpoint = "https://api.assemblyai.com/v2/transcript"
    json = {
        "audio_url": url
    }
    headers = {
        "authorization": assembly_auth,
    }

    response = requests.post(endpoint, json=json, headers=headers)
    print("id:", response.json()["id"])
    return response.json()["id"]

def get_request(vid_id):
    status = ""
    while status != "completed":
        sleep(5)
        endpoint = f"https://api.assemblyai.com/v2/transcript/{vid_id}"
        headers = {
            "authorization": assembly_auth,
        }
        response = requests.get(endpoint, headers=headers)
        status = response.json()["status"]
        print("status:", response.json()["status"])
        
    with open("lecture.txt", "w") as f:
        f.write(response.json()["text"])

def summarize(text):
    openai.api_key = openai_auth
    completion = openai.Completion.create(engine="text-davinci-003", prompt = f"summarize this: {text}", max_tokens = 1000)
    return completion.choices[0].text

def summarize_chunkify():
    with open("lecture.txt") as f:
        lecture = f.read()

    summary = ""
    lecture = lecture.split(" ")

    for i in range(len(lecture) // 1500):
        chunk = lecture[i * 1500:i * 1500 + 1500]
        chunk = " ".join(chunk)
        summary += summarize(chunk)
    chunk = lecture[i * 1500 + 1500:]
    chunk = " ".join(chunk)
    summary += summarize(chunk)

    with open("summary.txt", "w") as f:
        f.write(summary)
        

def answer_questions():
    with open("summary.txt") as f:
        summary = f.read()
    
    with open("questions.txt") as f:
        questions = f.read()
        
    openai.api_key = openai_auth
    completion = openai.Completion.create(engine="text-davinci-003", prompt = f"given this text: \"{summary}\" answer these questions: {questions}", max_tokens = 1000)
    
    with open("answers.txt", "w") as f:
        f.write(completion.choices[0].text)

def main():    
    # loc = input("recording number: ")
    # url = upload("./New Recording " + loc + ".m4a")
    loc = download_yt(yt_link)
    url = upload(loc)
    vid_id = submit_request(url)
    get_request(vid_id)
    summarize_chunkify()
    answer_questions()
    
if __name__ == "__main__":
    main()