# T40-Crewmates

Official Repository for DotSlash 4.0 Submission of Team 40: Crewmates.

## Winners of DotSlash 4.0 😃✌️💥

**Team Members:** 

    * Gaurav Kumar 
    * Shankhanil Borthakur
    * Anshoo Rajput

## Inspiration

We faced difficulty ourselves during the online semester and were able to think about what problems a differently-abled person might face during online education and hence we came up with this hack. We intend to make it easier for a person with any challenge of sight, hearing, or physical amputation to attend online classes, webinars, or courses. We also hope that interactive software games which can be played with slight body movements, will keep children engaged who cannot played physically demanding games.

## What it does

It captures audio and screenshots during any online class or conference etc. The screenshots of different slides are captures to avoid an excess of the same one accumulating. The audio is converted to text and a file containing its summary in .txt file as well as braille scripted file is saved. The braille file can be given as an input to refreshable braille display (rbd) machines. The audio files can also be used by a blind person for taking note of what happened during class. The screenshots are stored in a .docx file and can be used by a deaf person or even another person for revisiting concepts they might miss during classes. We also made a TicTacToe game that can be played with slight eye movements. 

## How we built it

- Capturing distinct screenshots for different slides, and avoiding clicking many screenshots for slight changes in slides, for e.g. professors writing additional information on slides.
- Converting audio files to Text using speech_recognition with google_speech_api, then summarising them using NLP and saving them offline.
- Converting text obtained to braille readable script.
- Using Opencv we also made a short game Tictactoe which can be played by controlling the cursor with facial gestures and closing eyes for 2 sec leads to click. Hence making it easier for people who have amputations or are facing some kind of paralysis are able to control their system themselves without difficulty.

## Tech Stacks

- Python
- Tkinter
- NLP
- Pyaudio
- google-speech-api

## Challenges we ran into

- Planning about how to implement the frontend was a problem. We never made a desktop app or any such GUI and hence we had to stick with Tkinter.
- Summarization is a problem that exists for us as we were unable to improve its accuracy after a point.

## Accomplishments that we're proud of

- We made a GUI using Tkinter for the first time, we had used it earlier just for plotting purposes and it was good for us.
- Full-fledged Hackathon experience and close to 48 hours of continuous coding was something we never thought if we could do.
- Although we faced many chalenges in building what we planned, we still qualified for the judging round.

## What we learned

- A simple phase of ideation about how great it is to discuss your ideas with team-mates and mentors.
- Research is a necessary phase and include reading blog, research papers, and discussing what things can be implemented.

## Presentation Video

[![Watch the video](https://img.youtube.com/vi/qgMU8F1QX5g/maxresdefault.jpg)](https://youtu.be/qgMU8F1QX5g)


## What's next for Edu_Help | T40: CREWMATES

- Shifting GUI to a desktop app using Electron.js so that it is better to use.
- Using a different speech to conversion module to avoid latency issues. Currently, it takes close to 7 minutes to process 1 hour of video due to several requests it sends to google_api.
- Improving summarization with a different algorithm and we need to study in more depth.
- The Gesture control needs to be more calibrated and we wish to integrate it to provide more use case to people with amputation.
