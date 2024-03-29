# hack-a-thing-1-twentyqs

## Jerry Wang & Timothy Qiu

### CS98 19F



#### Short Description

​	Twenty questions is a old school game that encourages deductive reasoning and creativity. In the original version, one person chooses a subject and does not reveal it to the other person, while the other person tries to deduce who it might be by asking simple "Yes" or "No " questions. If the questioner deduces who the subject is within twenty questions, the questioner wins, and if he doesn't then the answerer wins.

​	In this short program we try to create an AI that plays this game, and communicates with the human player through speaker and microphones. In order to make the project doable and make the guessing computationally feasible, we have narrowed down the game universe to just male soccer players. The AI will ask questions about the soccer player's traits and the human player will answer.

​	The AI's knowledge is completely based on a soccer database <http://pesdb.net/pes2019/>, which we scrape after every few answers by the human player in order to ask the most relevant and informational questions.



#### Work Allocation

Jerry:

* Audio, Microphone, and Speech Recognition
* Web Scraping and Web Querying
* Readme



Timothy:

* Game Logic
* Player Data Analysis
* Question Optimization
* Testing



#### What We Learned

​	Computer interaction with users through the audio/microphone system was something we have always been interested in. In this project we were able to explore a few packages such as SpeechRecognition, Pyttsx3, and Pyaudio. These packages are very intriguing and powerful, and yet are very easy to use. We are heavily considering using these packages for interaction between the user and the program in our final project.

​	Web scaping was something we also thought was very important to know before we dive into our final project. The internet provides a plethora amount of information that we can utilize for our projects, so it is crucial that we have the toolbox to make the most out of it. In this project we tried using Beautiful Soup as well as some Pandas internal functions to parse through the HTML of the webpages and extract its data.

​	The last skill we have really honed up on through this project is Pandas. We have both been introduced to Pandas before, but we are no where close to being comfortable with its wide range of functionalities. With this small project, we got much more skilled at manipulating Dataframes that we extracted from websites to identify player characteristics and filter out the correct subject.



#### What didn't work

* No margin of error in player search - If any of the player attributes are answered incorrectly, the correct subject will not be found. Some player attributes are marginal, very close between good and bad, but we only have binary options for the answerer to pick. This sometimes leads to finding the wrong subject.
* Questions sometimes not optimized - We did not find a great algorithm for ordering the questions, so some of the questions asked may not be very efficient. For example, it may first ask if the player is a defender then ask again if he is good at defense.
* Microphone system not stable - It sometimes fails when the background noise varies a lot in volume. We could not find a robust function or package that always picks up the user's voice regardless of the background situation.