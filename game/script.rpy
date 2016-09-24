# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
# define e = Character('Eileen', color="#c8ffc8")
init:
    define g1 = DynamicCharacter('aaa', color='#c8ffc8')
    define g2 = DynamicCharacter('bbb', color='#ff0505')
    define g3 = DynamicCharacter('ccc', color='#77e3ff')
    define t = Character('Generic Soldier', color='#850000')
    define mc = DynamicCharacter('main_char', color='#2b00ff')

    $_game_menu_screen = "navigation"
    $ flash = Fade(.25, 0, .75, color="#fff")

# The game starts here.
label start:
    $ aaa = bbb = ccc = '???'
    $ g1Name = 'AAA'
    $ g2Name = 'BBB'
    $ g3Name = 'CCC'
    $ main_char = ''
    $ revealed = False

    scene bg black

    "It all started when..."

    show aaa
    g1 "Watch out grenade!"
    hide aaa
    with dissolve

    pause .5

    with flash
    "BOOM!!!"

    show aaa
    with dissolve

    pause .5

    g1 "Are you OK?"

menu:
    "Yea, I'm fine.":
        g1 "Well, good."
        jump name

    "Are you stupid? I almost got blown away!":
        g1 "Well, if you can yell so loudly, you must be feeling fine."
        jump name

label name:
    g1 "Come on. Get up. Good."

    scene bg city
    show aaa
    with dissolve

    g1 "Watch out for the artillery shots!"
    with vpunch

    show aaa:
        linear .5 xzoom 1.1 yzoom .9
        pause .5
        linear .25 xzoom .9 yzoom 1.1
        linear .1 xzoom 1 yzoom 1

    g1 "Go! Go! Go!"

    hide aaa

    "The two soldiers barge into an abandoned building..."

    scene bg building
    with dissolve

    "Nobody is there..."

    show aaa

    g1 "Looks like we're safe for now."

    $ aaa = g1Name
    g1 "I haven't introduced myself. My name is %(aaa)s."

    g1 "And your name is?"

    $ main_char = renpy.input("What is your name?")

menu:
    "My name is %(main_char)s. Nice to meet you.":
        g1 "Nice to meet you too, %(main_char)s."
        jump after_building

    "I am %(main_char)s. You better remember it, a*****e":
        g1 "Well, f*** you too, %(main_char)s. But we need to work together if we are going to survive, OK? OK."
        jump after_building
