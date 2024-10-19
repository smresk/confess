import time
import sys
import os

def type_text(text, delay=0.07):
    """Simulate a human typing the message."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear_console():
    """Clear the console for a cleaner look."""
    os.system('cls' if os.name == 'nt' else 'clear')

def animated_heart():
    """Animate a growing heart."""
    hearts = [
        "      *        ",
        "     ***       ",
        "    *****      ",
        "   *******     ",
        "  *********    ",
        " ***********   ",
        "*************  ",
        " ***********   ",
        "  *********    ",
        "   *******     ",
        "    *****      ",
        "     ***       ",
        "      *        "
    ]
    for heart in hearts:
        print("\n" + heart + "\n")
        time.sleep(0.2)
        clear_console()

def love_confession():
    """A heartfelt love confession with animation."""
    print("\n" + "=" * 30)
    print("💖  A Special Message for You 💖")
    print("=" * 30 + "\n")
    
    type_text("Hii... boleh aku nak cakap sikit?", delay=0.1)
    time.sleep(1.5)
    type_text("aq ade fikir bende ni sometimes")
    time.sleep(2)
    type_text("aq rse ko dah tau ape aq nk ckp skrg ni susah aq nk ckp dpn ii psl ni... lgi ii bende ni psl ko")
    time.sleep(2)
    type_text("tpi tula aq tkle thn perasaan ni lama ii aq gak sket.")
    time.sleep(2)
    type_text("sng cite I feel something different, something amazing bile aq dkt ngan ko")
    time.sleep(2)
    type_text("kau buat aq ketawa, kau buat aq rse selesa borak ngan ko, and honestly... kau ubah hidup aq")
    time.sleep(2)
    type_text("and yea aq sedar bende ni bkn sbb ko kwn aq semata ii tpi ko idk...someone special")
    time.sleep(2)
    type_text("and you always running on my mind")
    time.sleep(2)
    type_text("EVERYTIME")
    time.sleep(2)
    type_text("So... pendek cite aq nk ckp")
    time.sleep(2)
    type_text("I lOVE YOU")
    time.sleep(2)
    type_text("aq tk berharap ko akan balas perasaan ni")
    time.sleep(2)
    type_text("thats all from me thankyou sbb dgr confession aq😉")
    
    print("\n")
    time.sleep(3)

    print("Sending my love with a growing heart...\n")
    animated_heart()  # Show animated heart after confession
    print("\n")

    print("=" * 30)
    print("💖  End of Message  💖")
    print("=" * 30 + "\n")

love_confession()
