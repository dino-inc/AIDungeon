from story.story_manager import *
# from generator.web.web_generator import *
# from generator.ctrl.ctrl_generator import *
from generator.gpt2.gpt2_generator import *
import textwrap

CRED_FILE = "./AI-Adventure-2bb65e3a4e2f.json"


def console_print(text, width=75):
    last_newline = 0
    i = 0
    while i < len(text):
        if text[i] == "\n":
            last_newline = 0
        elif last_newline > width:
            text = text[:i] + "\n" + text[i:]
        else:
            last_newline += 1
        i += 1




def play_unconstrained():
    generator = GPT2Generator()
    prompt = get_story_start("knight")
    context = get_context("knight")
    story_manager = UnconstrainedStoryManager(generator)
    story_manager.start_new_story(prompt, context=context)

    print("\n")
    console_print(context)
    console_print(str(story_manager.story))
    while True:
        action = input("> ")

        if action != "":
            action = action.strip()

            action = action[0].upper() + action[1:]

            action = "\n> " + action + "\n"
            action = remove_profanity(action)
            #action = first_to_second_person(action)
        
        result = story_manager.act(action)
        if player_died(result):
            console_print(result + "\nGAME OVER")
            break
        else:
            console_print(result)


if __name__ == '__main__':
    play_unconstrained()

