### CRYPTO CRAB

## https://youtu.be/WSy72-tI8eU

 
## DIFFICULTIES
# First, we had some trouble getting basic commands running on the bot. We realized we needed to restart discord when 
# adding new commands. Then, we had to find packages that could get data and create graphs using the data. When then 
# figure out how to use the packages we found. We used yfinanace and plotly. Third, we had had to try to figure out how
# to predict the price of the crypto. We are unable to do this. I found a package that was supposed to help but I could 
# not figure out how to properly use it. I got a lot of errors and could not find much online to lead me in the right 
# direction. The package was autots. I then did some more reading, and it seemed as if crypto price prediction was 
# mostly a fifty-fifty shot in the dark. So, it seemed pointless. Instead, we focused on creating the price graph of 
# the cryptocurrency and making it as customizable as possible. This took a lot of trial and error but the plotly 
# documentation was helpful. Connecting the yfinance data and plotly was also a hassle, but it worked. Then, came the 
# issue of making it into a discord bot. I (Yuval) had previously worked on discord bots but never with slash commands.
# After figuring that out, we had to integrate the graphs with the command and allow the user to customize it. 
# The biggest issue was trying to figure out how to send the graph in the chat. Now, I (Yuval) spent three hours trying
# to understand why I could not download the plotly graph as a png and could not figure it out. This was important 
# since the discord chat can only show it if it is a png or other image format. So, I resorted to making into an HTML
# file and sending into the discord chat, downloaded-able by the members. This worked out since the graph is somewhat 
# interactive when opened in a browser. Setting the file as a new file name each time chosen by the user was also hard.
# We had to use OS to join path names, and we had no idea what that was. The spinning randomize wheel took a while to 
# figure out, and we suffered multiple setbacks there. We attempted to use pygame to animate a spinning wheel, but 
# struggled to figure out how we would combine the discord bot and the animation, so we scrapped it for an easier 
# representation of the wheel. Then, we decided to use just straight up text, symbols like "/", "_" and "|" to make the
# discord bot send an image of a wheel in text, and then edit the text to make the wheel look like it was turning, but 
# we scrapped that idea also because the wheel looked really bad represented in text. We then tried to artificially 
# make a gif of the wheel, because we thought making a gif would be too hard, by having the bot repeatedly edit 
# pictures of a wheel, to make it look like it was turning. This didn't work in a sort of mysterious way, so we finally 
# settled on the idea of making a gif, which turned out to be not even that hard. Then, all the way after the entire 
# project had been totally completed, we realized that at the very start (Ian) had misheard (Yuval) and had made the 
# gif using a cryptocurrency named "BTH", which doesn't exist, (Ian) should have used "ETH". So we had to redo the gif 
# completely, which was surprisingly not that hard. In terms of coding the wheel, it was difficult to send pictures and 
# gifs, to edit text, and to delete text (or pictures), because it took a long time to search for the correct code.
