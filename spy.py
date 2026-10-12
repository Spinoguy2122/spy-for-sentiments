

import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

print(f'{Fore.CYAN}Welcome to the Sentiment Spy Tool!{Style.RESET_ALL}')

user_name= input(f'{Fore.RED}Please enter your name: {Style.RESET_ALL}').strip()
if not user_name:
    user_name = "Incognito"
conversation_history = []

print(f"\n{Fore.MAGENTA}Hello Agent {user_name}!")
print(f"Type a sentence and I shall analyze it for you!")
print(f"type {Fore.YELLOW}reset{Fore.LIGHTMAGENTA_EX}, {Fore.YELLOW}History{Fore.LIGHTMAGENTA_EX}, or {Fore.YELLOW}exit{Fore.LIGHTMAGENTA_EX}{Style.RESET_ALL} ")
while True:
    user_input = input(f"{Fore.GREEN}>>{Style.RESET_ALL} ").strip()
    if not user_input:
        print(f"{Fore.RED}Please enter a valid sentence.{Style.RESET_ALL}")
        continue
    if user_input.lower() == "exit":
        print(f"{Fore.CYAN}Goodbye, Agent {user_name}!{Style.RESET_ALL}")
        break
    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.YELLOW}Conversation history has been reset.{Style.RESET_ALL}")
        continue
    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history available.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}Conversation History:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                print(f"{idx}. {text} - Sentiment: {sentiment_type}")

                if sentiment_type == "Positive":
                    color == Fore.GREEN
                    emoji == "😊"
                elif sentiment_type == "Negative":
                    color == Fore.RED
                    emoji == "😞"
                else:
                    color == Fore.YELLOW
                    emoji == ":O"    
                print(f"{idx}. {color}{emoji} {text}"
                      f" Polarity: {polarity:.2f},{sentiment_type}{Style.RESET_ALL}")
        continue

    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
                sentiment_type = "Positive"
                color = Fore.GREEN
                emoji = "😊"
    elif polarity < -0.25:
                sentiment_type = "Negative"
                color = Fore.RED
                emoji = "😞" 
    else:
                sentiment_type = "Neutral"
                color = Fore.YELLOW
                emoji = ":O"
    conversation_history.append((user_input, polarity, sentiment_type))
    print(f"{color}{emoji} {sentiment_type}sentiment detected"
                  f" with a polarity of {polarity:.2f}.{Style.RESET_ALL}")
             
                