# secretofgreeksbot
Twitter bot which creates fake secret meanings to random greek organizations

Use whatever text file you desire to create fake meanings. I hard coded the randomly selected words from my text
file based on the first letter of the randomly selected greek letter. Use the counter_function(f) to determine the number
of words beginning with different keys. Then change the keyed letters and random.randint() in the generateRandomWord(letter)
function.

To connect to your twitter account make sure to include your Consumer Key, Consumer Secret, Access Token Key and Access Token
Secret to the areas indicated. 

I looked to Allison Parrish's github worksho for some help programming: https://github.com/aparrish/gen-text-workshop
and used this tutorial to help with the setup of tweepy: http://www.dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/

When calling the file in the command line used:
python greekbot.py text2.txt


