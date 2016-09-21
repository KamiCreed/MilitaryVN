init:
    image bg des_city = "images/desolate_city.jpg"

label after_building:
    g1 "Let's get out of here now. They will probably find us eventually if we stay here."

    hide g1Img

    "Bam!"

    "The door explodes, and a person barges through all covered in blood."

    

    g3 "*gasp"

    g1 "I want to see your hands up. I don't recognize your uniform. Which side are you on?"

    $ ccc = g3Name
    g3 "U-um. My name is %(ccc)s, and this isn't a uniform. I w-wear it e-everyday."

    g1 "Stop stuttering! It's getting on my nerves!"

    g3 "Right!"

    g1 "Well, it doesn't seem like you mean us any harm. Are you hurt? Do you need first aid?"

    g3 "No, I'm fine. This isn't really my blood."

    g1 "OK. Well, my name is %(aaa)s, and this over here is %(main_char)s."

    g3 "%(aaa)s and %(main_char)s. I think I got it."

    g3 "What are we going to do, now?"

    g1 "Well, we were going to get out of this building before you suddenly barged in."

    g3 "Sorry about that..."

    g1 "Whatever. Let's just get out of here."

    "The group of three sneak out through the back door with %(aaa)s taking point followed by %(main_char)s and %(ccc)s."

    "There, they are greeted by the complete destruction of the city."

    g1 "Hmph. This was probably going to happen eventually."

    g3 "How could you say that? This city used be such a bright and happy place."

menu:
    "I would've liked to see such a place. Probably would've been a good place to live in.":
        g3 "Yes, I loved this city."

    "Yeah, right. No place can ever be bright and happy, when people are by nature absolutely greedy.":
        g3 "That's kind of mean. Not everyone is greedy by heart, you know. My neighbors were all such good people."

label outside:
    g1 "Cut the chitter-chatter we have to get moving."
