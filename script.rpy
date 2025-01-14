# The script of the game goes in this file.

# The game starts here.

label start:
    play music "audio/background.mp3" volume 0.5 loop

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_image with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    #Intro
    "You wake up in the middle of the street, rubbing your eyes. It's a perfectly normal Monday..."

    show gojo stand
    play audio "audio/vine-boom.mp3" volume 0.8
    play audio "audio/footsteps.mp3" volume 0.4
    "Suddenly, a figure in a stylish blindfold walks up to you."
    "It's Gojo Satoru, wearing his signature smirk."

    g "Ah, great. Another lost soul."
    g "You're probably wondering how you ended up here."
    g "Don't bother. I don't even know."

    show saitama stand at right with moveinright
    play sound "audio/vine-boom.mp3"
    queue sound "audio/yawn.mp3"
    "Before you can respond, there's a loud boom, and Saitama, the bald hero of the world, casually strolls by, yawning."
    st "Hey, kid."
    st "You look like you could use a nap."
    st "This world's weird, but punching stuff seems to help."

    show sukuna stand at left with moveinleft
    play audio "audio/vine-boom.mp3"
    play audio "audio/fingers-cracking.mp3" volume 1.15
    "And just as you think things couldn't get crazier, Sukuna, the cursed king, appears out of nowhere, his cursed fingers cracking ominously."
    sk "Pathetic humans, always so confused."
    sk "Careful, little one, or I might just make you my next snack"
    "You blink."
    "Yep. You're definitely not in your old world anymore."
    # This ends the game.

    return
