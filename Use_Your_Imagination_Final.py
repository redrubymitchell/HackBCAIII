print("Hello, and Welcome to \"Use Your Imagination\". I am"
      " a Text-based game that has absolutely NO images, videos, or graphics of any sort, so you get to ")
print("\"use your imagination\" to imagine the game! Good luck and have fun!")
print("Text commands will pop up as you go through your journey")
print( )
print( )
print("You open your eyes and you can feel the bumps in the road beneath you.")
print("Even though you open your eyes all you can see is black, and you are laying on a cold metal surface")
print("You feel a fabric covering your face, you struggle to breathe")
print("You try to roll on your side but you feel a sharp metal ring dig into the palm of your hand.")
print("The clang of the metal alerts the driver, you hear him tell another passenger to \"take care of it\"")
print("You feel the footsteps of the man near you")

input_3 = input("Type \"calm\" to stay calm, or type \"kick\" to try and kick the man: ")
while input_3 != "calm" and input_3 != "kick":
    print("That is not a valid answer, try again: ")
    input_3 = input()

if input_3 == "calm":
    print("you feel a pinch in your thigh and begin to lose consciousness")
elif input_3 == "kick":
    print(
        "Your foot launches out into thin air and you feel knuckles collide with your head, and a painful jab in the "
        "thigh"
        " and you begin to feel weak, and start to lose consciousness")
print("........")
print("You are awakened by a rough shove and proceed to stumble and fall to the wet ground")
print("the bag is forcefully ripped off your head, and your eyes take a moment or two to adjust to the dark lighting.")
print("You appear to be in a dark alley surrounded by 4 men and a boy no older than 16, and you are cornered in back")
print(" by a dumpster")
print("that smells like rotten corpse. Wet blood dripping from ")
print("your knees and the spot where you got stabbed with the")
print(" needle is still numb. The young boy advances at you as if he were going to hit you.")
input_2 = input("Type \"shout\" to shout at the boy to back off, or type \"punch\" to punch the kid in the face: ")
while input_2 != "punch" and input_2 != "shout":
    print("That is not a valid answer, try again: ")
    input_2 = input()

if input_2 == "punch":
    print("you step forward and catch the kid's punch, and you drive it back into his mouth, blood already coming ")
    print("from his nose. He attempts again and you grab his hair and mash his face into your knee.")
    print("The four other men all stand by, seemingly amused by the situation. Finally, you pick up the boy, and toss")
    print("him in the smelly dumpster.")
    print("After you have taken a couple of breaths, and you look at the remaining 4 men surrounding you, and you")
    print("recognize one of them from the local news, you remember that he was an escapee from a high securiy prison")
elif input_2 == "shout":
    print("You yell at the kid \"Don't come closer, I'm warning you\" and the boy keeps advancing. ")
    print("The strongest of the ")
    print("four other men yells to the boy to stop, but nevertheless, the boy still advances")
    print(" slowly, until he meets you")
    print("face to face, and you can smell his breath, emanating the stench of alcohol, as strong as ammonia.")
    print(" He slaps you ")
    print("across the face, but before you react, he is launched from his feet head first into the dumpster behind ")
    print("you. When you")
    print("recover from the slap, you see the strong muscular man standing in front of you, and he says, \"That's ")
    print("what happens ")
    print("when someone doesn't follow my directions, understand me? Remember that, and you wont end up like the "
          "dumb kid.\" ")
    print("As you stand there you recognize the man as he speaks to you, you have seen him in the newspaper, about ")
    print("a month ago, and you remember he was the only one to ever escape from the local high security prison.")
input_4 = input("Type \"talk\" to mention that you have recognized him, or type \"quiet\" to keep your mouth shut: ")
while input_4 != "talk" and input_4 != "quiet":
    print("That is not a valid answer, try again: ")
    input_4 = input()
if input_4 == "talk":
    print("\"Hey, you-\" you say staring at him, a disgusted look on your face, \"I heard you escaped from one")
    print(" of them high security prisons, that right?\" ")
    print("He looks at you and seems confused, and says \"yeah that's right, what's it to you?\"")
    print("You say \"Oh noth'n. Just that I don't like being kidnapped by an escapee.\" ")
    print("He says, \"you're out numbered 1 to 4, I don't think you should be trying to pick a fight.")
    print("You make a \"pff\" sound and he takes offense to your attitude. He comes closer and his muscles tighten.")
elif input_4 == "quiet":
    print("You keep your lips sewed shut but he catches you staring at him, and he asks \"Whatta you lookin at?\" ")
    print("You respond \"nothing. just seeing if I could kick your butt.\" ")
    print("He steps up to you as if accepting the challenge, and after a few moments his face tightens...")
    print("He throws the first punch, you block it with your forearm but ")
    print("you feel the bone break from the force of his arm")
input_5 = input("You have taken damage, Type \"back away\" to retreat or type \"slow\" to slow time: ")

while input_5 != "back away" and input_5 != "slow":
    print("That is not a valid answer, try again: ")
    input_5 = input()

if input_5 == "back away":
    print("You stumble back and hit the dumpster. He comes in for another punch and drives a fist into your stomach.")
    input_6 = input(
        "Type \"give up\" to beg for mercy, or type \"fight\" to continue fighting: ")

    while input_6 != "give up" and input_6 != "fight":
        print("That is not a valid answer, try again: ")
        input_6 = input()

    if input_6 == "give up":
        print("\"Please, I beg you to stop\" you plead. Weak fool, he replies, and puts his revolver to your forehead.")
        print("\Please-\" but the revolver fired and the shot rang out through the streets in the night.")
        print(" ")
        print(" ")
        print("FYI: you are NOT DEAD, instead, he shot the revolver right next to your head, with the intension of")
        print("scaring you, but instead, the loud noise and the intensity of the situation made you black out")
        print(" ")
        print(".....")

    elif input_6 == "fight":
        print("As he retracts his arm from your stomach, you grab it and twist it in 8 different ways, he screeches")
        print("and you knee him in the stomach.")
        print("You kick him in the stomach and it forces him back into the concrete wall, the concrete")
        print("cracks, in a sun shape around where his body collided with the wall.")
        print("You advance to the man, groaning on the concrete wall, and in the shadows, you see a faint")
        print("image of what appears to be a baseball bat or club and just as you start to turn around... ")
        print(" ")
        print(".....")

elif input_5 == "slow":
    print("You vision blurs and you feel like you have complete control over your actions. You leap in the air and ")
    print("leap over the strong man, and put him in a headlock, although you cannot see from the back, the mans face ")
    print("is frozen in shock and confusion. Your hands wrap around his neck into a headlock, and you twist with one")
    print("smooth motion, hearing the crack, and the body falls to the ground. You swing look down and there is a ")
    print("switchblade on his belt buckle, and you open it and turn around and drive it into the gut of another man,")
    print("charging at you with a fist hard as rock, as if he was nothing, you push his shoulder away and the blade")
    print("releases from his stomach covered in red. Two left, and you feel the effect of time as you move, slowing")
    print("your every step, but also making you react faster than your opponent, and you throw the knife at the throat")
    print("of one of the remaining men and it is so on target it sticks out the other side of his neck. He falls to")
    print("the blood covered ground, and you walk over and retrieve his .44 magnum and take aim at the very last man")
    print("running away in terror, and you fire the gun, and you watch the bullet fly in the time warp, and you see")
    print("it enter the back of his head, and his body flips around to face you and you watch him fall,")
    print(" with a red circle no bigger than a pencil tip, on the top of his forehead")
    print(" ")
    print(" ")
    print(" ")
    print("So now begins your life of crime.")

print("Now, four weeks later from the incident in the alleyway, you are a changed man, and you walk down the streets")
print("of New York, heading to the bar on the corner. The area you are in smells of urine and there are homeless")
print("people, women, men, and children, everywhere you look,=, there is garbage in the streets, on the sidewalks, and")
print("you turn into a bar on the corner. \"I'm here for the Boss\" you say")
print("The bartender answers you, \"he's not in\"")
input_7=input("Type \"lie\" if you think he's lying to you, or type \"walk\" to walk right into the boss's room")
while input_7 != "lie" and input_7 != "walk":
    print("That is not a valid answer, try again: ")
if input_7 == "lie":
    print("\"I bet you he is\" you say. The bartender replies, \"you callin' me a liar?\"")
    print("He approaches you with a bottle of Smirnoff still in his hand, and  he's wanting to pick a fight")
    print("Your next reaction is so automatic and sudden. You grab him by the head and slam it into the Bar counter")
    print("and slide it down knocking all the dishes off leaving a trail of blood, and you take the bottle of Smirnoff")
    print("and break it over his head and he falls to the floor. You walk past him on the floor with the entire rest")
    print("of the bar customers staring at you, with one woman being so drunk as to say \"look at him he's superman!\"")
    print("and you walk straight into the bosses office. ")
elif input_7 == "walk":
    print("The bar tender tries to stop you but you shove past him into the bosses room.")

print("You see the boss sitting in his brown leather chair smoking a cigar, puffing smoke into the room.\"Didnt't the ")
print("bartender tell you to stay out?\"? he asked. I replied: ")
if input_7 == "lie":
    print("yeah, he did, and you may wanna find a new bar tender.")
if input_7 == "walk":
    print("yeah, but do you think I'd believe that?")
print("\"What are you doing here\" he asked in that groany voice.")
print("\"coming to see why you put 4 guys and a kid on me, and had me kidnapped.\"")
print("\"kidnapped, no. they were coming to teach you a lesson. Teach you to pay me on time for the last shipment.\"")
print("\"Maybe if you gave me the right amount I'd pay you. Good business you know.\"")
print("\"I don't think you should be tellin me what to do\" as he waves his gun in the air")
input_8=input("Type \"leave\" to leave or \"shoot\" to shoot the boss")
while input_8 != "leave" and input_8 != "shoot":
    print("That is not a valid answer, try again: ")
if input_8== "leave":
    print("As you turn to walk to the door, two gaurds stand in your way, saying \"The Boss isn't "
          "finished with you yet\"")
    print("Without even turning around, you pull out a berretta and shoot the Boss right in the chest.")
    print("\"I think he's done with me now.\" You say, and walk out. The guards, still in shock, are unable to move.")
elif input_8=="shoot":
    print("You look at the boss and slowly pull out your gun. He smiles, and the guards immediately take aim at you")
    print("You shoot both of them, but not before The Boss gets out his own Desert Eagle handgun.")
    print("He puts his feet up on the desk an he says \"This is how this is gonna work. You're gonna put your gun"
          "down and-")
    print("Bang. The Bosses blood all over the wall and you turn and walk out.")
print( )
print( )
print(".....")
print( )
print("You are now in Mexico, and you just got off the plane, and you are here for one thing and one thing only,")
("money, at least in the long run. You are now self employed after the incident with the Boss.")
print("You arrive at the nearest hospital that has scrappy security at best, and you slip through the back door to")
print("the doctors lounge. You quickly steal doctors clothes and disguise yourself as a doctor. You walk to room 113")
print("and you read the sign that says: Specialist Surgeon: Dr. Sanjo - Kidney Transplant")
print("You wait for doctor Sanjo to arrive, and when he does you lead him to room 113. As he preps for surgery,")
print("he washes his hands and he feels an arm come around his neck seconds later he is dead, blood flowing down the")
print("sink drain. Once the body is disposed of you take the scalpel and get to work on the patient. Kidney Transplant")
print("...simple. But as you cut down the patients chest, in comes the nurse and doctor's assistant.")
print("They question you as to why you have started the operation before they arrived.")
input_9=input("Type \"kill\" to attempt to kill all of them, or type \"explain\" to attempt to explain the situation.")
while input_9 != "kill" and input_9 != "explain":
    print("That is not a valid answer, try again: ")
if input_9 == "kill":
    print("You take the nearest nurse and slice her neck with the scalpel, and you kick the doctor's assistant into")
    print("the operating table and you throw him on the ground and stick the scalpel in his neck.")
    print("Just then another nurse walks in carrying IVs and she goes out the window and let her fall 4 stories")
elif input_9 == "explain":
    print("\"I didn't know I needed to be babysat to start an operation, may we proceed\" you say.")
    print("Yes doctor, let's proceed.")

print("You continue with your incision and you reveal the patients inside.")
if input_9 == "explain":
    print("To clear the room, I take the pulse measurers off the patient's body to produce a flat line warning, and")
    print("all the other medical staff raced out of the office to get defibrillators and other equipment.")
    print("This leaves you some time so now")
print("you slice open the patients gut and stash small white packs of cocaine in side him")
print( )
print( )
print(".....")
print( )
print("Back in the US, you have tracked down your patient and naturally, psychopathically killed him too, extracted")
print("your goods, and Lived Happilly Ever After! THE END.")