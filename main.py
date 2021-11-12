import discord
import os

client = discord.Client() 
@client.event 
async def on_ready():
  print("We Have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
  if message.author == client.user: 
    return


  if message.content.startswith('>greeting'):
    await message.channel.send("Hello, \nDear Friend :) ")
  

  if message.content.startswith('>google'):
    await message.channel.send('Go To https://google.com to solve all of your problems :D')
  
  if message.content.startswith('>timetable'):
    await message.channel.send('https://drive.google.com/file/d/1tcLkzaNXKHLwr-YueTFRvog73OB5Gzsz/view?usp=sharing \nThis is the link to 6G 2021 Online Class Timetable ')
  
  if message.content.startswith('>kill'):
    await message.channel.send('Well murder is ilegal bro so you might want to reconsider it')
  if message.content.startswith('>romantic'):
    await message.channel.send(file=discord.File('BGM.mp3'))



  if message.content.startswith('>help'):
    await message.channel.send(">greeting\n>timetable\n>google\n>feel-special\n>owner-info\n>secret\n>romantic\n>kill\n>help\n>nitro_free\n>pig\n>github\nThere are more secret commands, just discover it yourself or view the code on github !\nAnd also the bot is in beta stage so don't expect too much from it :D ") 
  

  if message.content.startswith('>secret'):
    await message.channel.send('try using Good Night Sweet Dreams\n try using Morning/ morning/Good Morning/good morning')

  if message.content.startswith('morning'):
    await message.channel.send('Good Morning My friend!\nHope you had a good sleep :D ')
  
  if message.content.startswith('Morning'):
    await message.channel.send('Good Morning My friend!\nHope you had a good sleep :D ')
  
  if message.content.startswith('Good Morning'):
    await message.channel.send('Good Morning My friend!\nHope you had a good sleep :D ')
  
  if message.content.startswith('good morning'):
    await message.channel.send('Good Morning My friend!\nHope you had a good sleep :D ')

  if message.content.startswith('>feel-special'):
    await message.channel.send(file=discord.File('FeelSpecial.mp3'))
  if message.content.startswith('>owner-info'):
    await message.channel.send('The Cool Dude that created me : Ze Zayne aka Sharky#8937\n I was create at 13th of October 2021\nAge of Sharky#8937 = 12')
  if message.content.startswith('>pig'):
    await message.channel.send('https://tenor.com/view/pig-wink-no-cute-smile-gif-12832481')
  if message.content.startswith('>nitro_free'):
    await message.channel.send('https://tenor.com/view/rick-roll-nitro-gif-21997352')
  if message.content.startswith('Good Night Sweet Dreams'):
    await message.channel.send('Good Night My Dear Friend\nSleep tight and dont let the bed bugs bite :D')
  if message.content.startswith('fuck'):
    await message.channel.send('Please Mind your language or your are going to get muted by the admin.Thank you for your cooperation.')

  if message.content.startswith('Fuck'):
    await message.channel.send('Please Mind your language or your are going to get muted by the admin.Thank you for your cooperation.')
  if message.content.startswith('Hey'):
    await message.channel.send('Hey ! Hi There my friend.')
  if message.content.startswith('hey'):
    await message.channel.send('Hey ! Hi There my friend.')

  if message.content.startswith('copemheimer'):
    await message.channel.send('Now I become death, the destroyer of worlds.')
  
   if message.content.startswith('>github'):
    await message.channel.send('https://github.com/zezayne/Sharky-Robot')
  
  

    
  


my_secret = os.environ['TOKEN']
client.run(my_secret) 

