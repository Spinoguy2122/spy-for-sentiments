
import re
import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init(autoreset=True)

conversation_history = []

positive_words = {
    "happy", "love", "great", "good", "excellent", "amazing",
    "wonderful", "awesome", "joy", "excited", "fantastic",
    "beautiful", "kind", "enjoy", "success", "hope"
}

negative_words = {
    "sad", "hate", "bad", "terrible", "awful", "angry",
    "upset", "horrible", "disappointed", "fear", "worried",
    "annoyed", "failure", "pain", "lonely", "unhappy"
}

print(f"{Fore.CYAN}Welcome to the Sentiment Spy Tool!{Style.RESET_ALL}")

user_name = input(
    f"{Fore.RED}Please enter your name: {Style.RESET_ALL}"
).strip()

if not user_name:
    user_name = "Incognito"

print(f"\n{Fore.MAGENTA}Hello Agent {user_name}!")
print("Type a sentence and I shall analyze it for you!")
print(f"""
{Fore.YELLOW}Available commands:
- Type a sentence to analyze its sentiment
- history: View your analysis history
- reset: Clear your history
- stats: View sentiment statistics
- report: Generate a spy report
- scan: Scan a sentence for emotional keywords
- help: Show all commands
- exit: Close the tool
{Style.RESET_ALL}""")


def analyze_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity

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
        emoji = "😐"

    return polarity, sentiment_type, color, emoji


def show_history():
    if not conversation_history:
        print(f"{Fore.YELLOW}No conversation history available.")
        return

    print(f"\n{Fore.CYAN}=== Conversation History ===")

    for idx, (text, polarity, sentiment_type) in enumerate(
        conversation_history, start=1
    ):
        if sentiment_type == "Positive":
            color = Fore.GREEN
            emoji = "😊"
        elif sentiment_type == "Negative":
            color = Fore.RED
            emoji = "😞"
        else:
            color = Fore.YELLOW
            emoji = "😐"

        print(
            f"{idx}. {color}{emoji} {text} | "
            f"Polarity: {polarity:.2f} | {sentiment_type}"
            f"{Style.RESET_ALL}"
        )


def show_statistics():
    if not conversation_history:
        print(f"{Fore.YELLOW}No data available. Analyze some sentences first.")
        return

    total = len(conversation_history)

    positive = sum(
        1 for item in conversation_history if item[2] == "Positive"
    )
    negative = sum(
        1 for item in conversation_history if item[2] == "Negative"
    )
    neutral = sum(
        1 for item in conversation_history if item[2] == "Neutral"
    )

    print(f"\n{Fore.CYAN}=== Sentiment Statistics ===")
    print(f"Total sentences analyzed: {total}")
    print(f"{Fore.GREEN}Positive: {positive} ({positive / total * 100:.1f}%)")
    print(f"{Fore.RED}Negative: {negative} ({negative / total * 100:.1f}%)")
    print(f"{Fore.YELLOW}Neutral: {neutral} ({neutral / total * 100:.1f}%)")


def generate_report():
    if not conversation_history:
        print(f"{Fore.YELLOW}No data available to generate a report.")
        return

    total = len(conversation_history)
    average_polarity = sum(
        item[1] for item in conversation_history
    ) / total

    positive = sum(
        1 for item in conversation_history if item[2] == "Positive"
    )
    negative = sum(
        1 for item in conversation_history if item[2] == "Negative"
    )
    neutral = sum(
        1 for item in conversation_history if item[2] == "Neutral"
    )

    if average_polarity > 0.25:
        overall = "Mostly Positive"
        color = Fore.GREEN
        emoji = "😊"
    elif average_polarity < -0.25:
        overall = "Mostly Negative"
        color = Fore.RED
        emoji = "😞"
    else:
        overall = "Mostly Neutral or Mixed"
        color = Fore.YELLOW
        emoji = "😐"

    print(f"\n{Fore.CYAN}=== CLASSIFIED SPY REPORT ===")
    print(f"Agent: {user_name}")
    print(f"Total sentences analyzed: {total}")
    print(f"Positive sentences: {positive}")
    print(f"Negative sentences: {negative}")
    print(f"Neutral sentences: {neutral}")
    print(f"Average polarity: {average_polarity:.2f}")
    print(f"Overall result: {color}{emoji} {overall}{Style.RESET_ALL}")

    strongest = max(conversation_history, key=lambda item: abs(item[1]))

    print(f"\nMost emotionally strong sentence: {strongest[0]}")
    print(f"Polarity: {strongest[1]:.2f}")
    print("Report complete.")


def keyword_scanner():
    sentence = input(
        f"{Fore.GREEN}Enter a sentence to scan: {Style.RESET_ALL}"
    ).strip()

    if not sentence:
        print(f"{Fore.RED}Please enter a sentence to scan.")
        return

    words = re.findall(r"\b[\w']+\b", sentence.lower())

    found_positive = sorted(set(words) & positive_words)
    found_negative = sorted(set(words) & negative_words)

    print(f"\n{Fore.CYAN}=== Keyword Scanner Results ===")

    if found_positive:
        print(
            f"{Fore.GREEN}Positive keywords: "
            + ", ".join(found_positive)
        )
    else:
        print(f"{Fore.GREEN}No selected positive keywords detected.")

    if found_negative:
        print(
            f"{Fore.RED}Negative keywords: "
            + ", ".join(found_negative)
        )
    else:
        print(f"{Fore.RED}No selected negative keywords detected.")

    if found_positive and found_negative:
        print(f"{Fore.YELLOW}Mixed emotional keywords detected.")
    elif found_positive:
        print(f"{Fore.GREEN}Positive keywords detected.")
    elif found_negative:
        print(f"{Fore.RED}Negative keywords detected.")
    else:
        print(f"{Fore.YELLOW}No matching emotional keywords found.")

    print(
        f"{Fore.CYAN}Note: This scanner matches a limited word list. "
        "It does not understand context, sarcasm, or negation."
    )


def show_help():
    print(f"\n{Fore.MAGENTA}=== Agent Command Center ===")
    print(f"{Fore.GREEN}Enter a sentence - Analyze sentiment")
    print(f"{Fore.GREEN}history - View conversation history")
    print(f"{Fore.GREEN}reset - Clear conversation history")
    print(f"{Fore.GREEN}stats - Show sentiment statistics")
    print(f"{Fore.GREEN}report - Generate a spy report")
    print(f"{Fore.GREEN}scan - Scan emotional keywords")
    print(f"{Fore.GREEN}help - Show commands")
    print(f"{Fore.GREEN}exit - End the session")


while True:
    user_input = input(
        f"\n{Fore.GREEN}>> {Style.RESET_ALL}"
    ).strip()

    if not user_input:
        print(f"{Fore.RED}Please enter a valid sentence.")
        continue

    command = user_input.lower()

    if command == "exit":
        print(f"{Fore.CYAN}Goodbye, Agent {user_name}!")
        break

    elif command == "reset":
        conversation_history.clear()
        print(f"{Fore.YELLOW}Conversation history has been reset.")

    elif command == "history":
        show_history()

    elif command == "stats":
        show_statistics()

    elif command == "report":
        generate_report()

    elif command == "scan":
        keyword_scanner()

    elif command == "help":
        show_help()

    else:
        polarity, sentiment_type, color, emoji = analyze_sentiment(
            user_input
        )

        conversation_history.append(
            (user_input, polarity, sentiment_type)
        )

        print(
            f"{color}{emoji} {sentiment_type} sentiment detected "
            f"with a polarity of {polarity:.2f}."
            f"{Style.RESET_ALL}"
        )

                
