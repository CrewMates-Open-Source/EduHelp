import timeit
import speech_recognition as sr 
import moviepy.editor as mp
import librosa
# class common_utils:
def text_det(fn):
    # clip = mp.VideoFileClip(r"bvideo.mp4") 
    # clip.audio.write_audiofile(r"baudio.wav")
    text = ""
    r = sr.Recognizer()
    duration = librosa.get_duration(filename=fn)
    loop = int(duration/60)
    rem = duration%60
    audio = sr.AudioFile(fn)

    for i in range(0, loop):
        with audio as source:
            audio_file = r.record(source, offset=i*60, duration=60)
        print(i)
        result = r.recognize_google(audio_file)

        text = text+" "+result

    with audio as source:
        audio_file = r.record(source, offset=loop*60, duration=rem)

    result = r.recognize_google(audio_file)

    text = text+" "+result
    return text