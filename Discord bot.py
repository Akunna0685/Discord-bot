#import discord
from discord.ext import commands
import random
import asyncio


#import time
tocken = "OTY2MzMzODcxNTMwNTc3OTIw.YmAOjA.RkS6WWHmwjP33eXGWQjB_3Oe1Fo"

bot = commands.Bot(command_prefix='!')
#Client = 435933988641832980
#bot logs into the chat
@bot.event
async def on_ready():
    print(f'{bot.user} succedfully logged in')
#the author has to  send in Chat the activation code to take the test
@bot.event
async def on_message(message):
    if message.content == "CT":
        await message.channel.trigger_typing()
        await asyncio.sleep(2)
        await message.channel.send('Enter the name of the participants: ')
#praticipans are enterd to take the test
        #ramndom number generated and gives you resolts

        def Test_now (Message):
            return Message.author == message.author and Message.channel == message.channel
        Message = await bot.wait_for("message", check=Test_now)
        await message.channel.trigger_typing()
        await asyncio.sleep(2)
        respond = ('The test shows that ',Message.content,' have a ', random.randint(0, 100), "% compatibility"
                   ' Is this bad or good?')
        await message.channel.send(respond)


        #asking you your opinion on the results

        def checkforanswer(msg):
            return msg.author == message.author and msg.channel == message.channel and msg.content.lower() in ["bad",
                                                                                                               "good"]

        age = await bot.wait_for("message", check=checkforanswer)
#if you like the awnser then it is over

        if age.content == "good":
            await message.channel.trigger_typing()
            await asyncio.sleep(2)
            await age.channel.send('yay!! Bye then')

#if the answer is bad the bot tries to cheer you up by you playing with copy cat

        if age.content == "bad":
            await message.channel.trigger_typing()
            await asyncio.sleep(2)
            await age.channel.send('OH sorry. :( Do you want to play with copy cat to make you feel better')

#you can chooes to play with it or not it just copies your word

            def yeahnah(MSG):
                return MSG.author == message.author and MSG.channel == message.channel and MSG.content.lower() in ["yes",
                                                                                                               "no"]
            MSG = await bot.wait_for("message", check=yeahnah)
            
            if MSG.content == 'yes':
                await message.channel.trigger_typing()
                await asyncio.sleep(2)
                await age.channel.send('Enter anything now and Copy Cat will copy it.')


                def copy_cat(mess):
                    return mess.author == message.author and mess.channel == message.channel

                mess = await bot.wait_for("message", check=copy_cat)
                await message.channel.send(mess.content)
                await message.channel.trigger_typing()
                await asyncio.sleep(2)
#askes if you are better
                repond = 'do you feel better now'
                await mess.channel.send(repond)
                await age.channel.send("yes or no")

                def ndansercheck(msg):
                    return msg.author == message.author and msg.channel == message.channel and msg.content.lower() in [
                        "yes", "no"]

                msg = await bot.wait_for("message", check=ndansercheck)

                if msg.content == "yes":
                    await msg.channel.trigger_typing()
                    await asyncio.sleep(2)
                    backmsg = 'Yay!! XD Bye,bye for now then'
                    await msg.channel.send(backmsg)


                if msg.content == "no":
                    await msg.channel.trigger_typing()
                    await asyncio.sleep(2)
                    end = 'Sorry!! :(I cant help more then this. Bye now'
                    await msg.channel.send(end)


            if MSG.content == "no":
                await MSG.channel.trigger_typing()
                await asyncio.sleep(2)
                await MSG.channel.send('OH :( , well sorry i cant help more. bye then')


bot.run(tocken)