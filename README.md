# KnowYourMeme Bot

A simple discord bot used to inform individuals about memes using www.knowyourmeme.com


## Description

![image](https://user-images.githubusercontent.com/19597915/150350220-9f474b45-e833-4235-9964-001640d5c215.png)
Install this bot into any discord channel and you can invoke its command using `!knowyourmeme meme_name_here`

## Getting Started


### Dependencies

* Python 3.9
* Discord Token and Guild ID
* Docker
* Make

### Installing

I loosely followed this tutorial to get the Discord bot up and running

https://realpython.com/how-to-make-a-discord-bot-python/


![image](https://user-images.githubusercontent.com/19597915/150350936-86a8a8ed-5a0d-4afc-a7dd-4e65b8dbdaa9.png)
Go here and copy the Discord Token

Install all of the python dependencies using
```
pip3 install -r requirements.txt
```

### Executing program

I've created a Makefile to spin up the bot in one command. 
Once you have updated the .env with the correct credentials you can utilize

```
make
```
To display all of the possible commands


```
make develop
```
Will run it locally on your machine

```
make runtime
```
Will compile it into a Docker container

## Acknowledgments

Inspiration, code snippets, etc.
* [Discord Bot Tutorial](https://realpython.com/how-to-make-a-discord-bot-python/)
* [Know Your Meme Search API](https://github.com/andrija1213/KYMA)
* [Discord Bot Documentation](https://discordpy.readthedocs.io/en/stable/)
