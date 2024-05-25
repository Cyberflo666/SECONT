#Smoke and Algorithms - Project 2024 SECont 




define PC = Character("[PN]", what_prefix='"', what_suffix='"')
default PN = "Robert Paulson"
default gender = "neutral"
default heshe = "they"
default himher = "them"
default hishers = "their"
define A = Character("Alex", what_prefix='"', what_suffix='"', color="7FFF00")
define F = Character("Felix", what_prefix='"', what_suffix='"', color="00008B")
define L = Character("Leoni", what_prefix='"', what_suffix='"', color="FF7F50")
define follow = False
define check = False
define ignore = False
image bg dogmeat = "dogfood.png"


label level_0_start:

    scene introduction and name
    "Buckle up for a journey where trust is a weapon, truth is a labyrinth, and the choices you make could unravel a conspiracy that reaches far beyond the walls of your imagination"

    $ PN = renpy.input("Enter your name.", "Robert Paulson", length=15, exclude=" 0123456789+=,.?!<>[]{}").strip() 
    menu:
        "Are you..."
        "A Boy":
            $ gender = "male"
            $ heshe = "he"
            $ himher = "him"
            $ hishers = "his"
        "A Girl":
            $ gender = "female"
            $ heshe = "she"
            $ himher = "her"
            $ hishers = "hers"
        "Non-Binary":
            $ gender = "neutral" 
    "Welcome [PN]. Let's get on with the story."




label dorm_1:

    scene dorm room

    scene A DORM ROOM - LATE AFTERNOON

    "The late afternoon sun filters through the blinds, casting long shadows across a cluttered dorm room. Books, papers, and empty snack wrappers are scattered haphazardly across the floor, a testament to the chaotic energy of finals week."
    
    "[PN], [hishers] dark hair pulled into a messy bun, sits hunched over [hishers] laptop, the glow of the screen illuminating the intricate henna tattoos on [hishers] left hand."

    PC "I can't focus. Complex systems theory is proving to be...well, complex. My eyes glaze over the lines of code and algorithms, and my mind starts to drift."

    "Alex, sprawled across the floor amidst a sea of open books, lets out a dramatic sigh."

    A "Okay, I officially surrender to the forces of academia. My brain is officially mush."

    "[PN] chuckles, a welcome distraction from [hishers] studies."

    PC "Don't worry, Alex. We're almost through this. Just a few more hours of this delightful torture."

    "Alex groans dramatically, then reaches for a half-eaten slice of pizza."

    A "If caffeine and sugar were the keys to academic success, we'd all be Nobel laureates by now."

    "A comfortable silence settles over the room, punctuated only by the rhythmic tapping of Leoni's keyboard from her beanbag chair in the corner."

    L "Hey, have either of you seen Felix today? He hasn't answered any of my texts."

    "Alex sits up, a mischievous glint in his eyes."

    A "Oh, you know Felix. He's probably off chasing UFOs or decoding secret messages in the cafeteria's meatloaf."

    "[PN] smiles, but the worry doesn't quite fade. Felix, their conspiracy-obsessed friend, had been acting strangely lately. His usual playful banter had taken on a darker tone, his excitement about his BioSyn internship replaced by a growing unease."

    A "Actually, now that you mention it... he seemed a little freaked out this morning. Almost like he was...scared"

    L "Scared? Of what?"

    A "I don't know. He was mumbling something about his internship at BioSyn, some experiment called NeuroMend... It was all very cryptic."

    "Suddenly, the dorm room door is thrown open, slamming against the wall with a resounding crash."

    "Felix bursts into the room, his eyes wide with terror, his chest heaving as if he'd been running for miles. His usually meticulously styled hair was a tangled mess, and his clothes were rumpled and stained."

    F "(Gasping for air, his voice barely a whisper) BioSyn! They're not what they seem. This... this is everything. Trust no one."

    "With trembling hands, he thrusts a battered flash drive into [PN]'s hand, then turns and flees, disappearing into the dimly lit hallway."

    "The air crackles with tension, and a million thoughts race through my mind. What was that all about? Why is Felix so scared? What's on this flash drive? The flash drive feels heavy in [PN]'s hand."

    "[PN] looks between Alex and Leoni, weighing her options."

menu:
    "(Alex' breaking the silence, his voice filled with concern)) Do you think we should go after him?":
        $ follow = True
        jump choice0_done
    
    "(Leoni pushing up her glasses) Or maybe we should see what's on this drive first?":
        $ check = True
        jump choice0_done

    "This could be dangerous. Maybe we shouldn't get involved.":
        $ ignore = True
        jump choice0_done
        
label choice0_done:
    if ignore == True:
        jump choice0_ignore
    elif check == True:
        jump choice0_check
    elif follow == True:
        jump choice0_follow


label choice0_ignore:

        scene bg dogmeat

        A "(His eyes widening in disbelief) Are you serious? [PN], Felix is our friend. We can't just abandon him!"

        L "Besides, curiosity is killing me. I want to know what's on that drive."

        "[PN] hesitates, torn between caution and concern for [hishers] friend."

        A "Exactly! And that's why we need to find out. Come on, [PN], let's go after him."
   
        L "I'll stay here and see if I can find anything on the drive. Maybe it'll give us some clues."

        "[PN] hesitates, torn between caution and concern for [hishers] friend. But the weight of the unknown proves too heavy. [PN] sinks back onto [hishers] bed, a sense of unease settling in."

        A "(Frustration edging into his voice) Seriously? We're just going to let him disappear? What if he's in real trouble?"

        PC "I... I don't know what to do. I'm scared."

        "Leoni looks up from her laptop, her expression a mix of concern and determination."

        L "I'm not finding anything on this drive yet. It's encrypted. But I'll keep trying. In the meantime, maybe we should just... wait and see?"

        "Hours turn into days, and Felix remains missing. The unanswered questions gnaw at [PN], a constant reminder of their inaction. The flash drive remains a mystery, its secrets locked away."

        "Weeks later, a small article buried in a conspiracy theory tabloid catches [PN]'s eye. The headline reads: 'Shocking Discovery: Human DNA Found in Dog Food.'"

        "A chill runs down [PN]'s spine. The article details a bizarre finding at a local pet food factory, a trace of human genetic material amidst the meat and grains. The source of the DNA remains unknown, the investigation ongoing."

        "[PN] can't shake the feeling that this is somehow connected to Felix, to BioSyn, to the cryptic warning he delivered that fateful night. But without proof, it's just another unsolved mystery, a whisper in the wind."

        "The weight of regret settles heavily on [PN]'s shoulders. The choice to ignore Felix's plea, to prioritize safety over friendship, has left a bitter taste in [hishers] mouth. The story ends not with a bang, but with a whimper, a silent echo of what could have been."

        

        return
 
label choice0_check:

        PC "He said this was important. Maybe it has answers. Leoni, can you take a look?"
        
        "Leoni nods, taking the flash drive from [PN]. She plugs it into her laptop and begins examining its contents."

        "Her fingers fly across the keyboard, a series of complex commands appearing on the screen."

        L "It's encrypted...heavily. This isn't something I can crack easily. We'll need more information, maybe something in Felix's room can help."

        A "His room? You think he might have left something behind?"

        PC "It's worth a shot. Let's go check it out."

        "The three friends leave the dorm room, a sense of urgency propelling them towards Felix's room. The encrypted drive seems to be a dead end for now, but perhaps the answers they seek lie hidden elsewhere."

        jump level_1_start

label choice0_follow:
        
        PC "We can't just let him run off like that. He's obviously terrified. Something's wrong."

        "[PN] rushes out the door, following the direction Felix took. Alex and Leoni exchange a worried glance before hurrying after [himher]."

        "The hallway is dimly lit, the air heavy with the scent of stale pizza and disinfectant. Felix is nowhere to be seen. [PN] quickens [hishers] pace, [hishers] heart pounding in [hishers] chest."

        A "Felix! Where are you?"

        "Their voices echo down the empty corridor, but there's no response. They search every nook and cranny, every possible hiding spot, but Felix is gone."

        PC "Damn it! We lost him."

        "Defeated, they return to the dorm room, the silence amplifying their worry. Leoni picks up the flash drive Felix left behind, a sense of urgency washing over her."

        L "We have to figure out what's on this drive. Maybe it holds the answers to where Felix went and what he's so scared of."

        $ follow = False

        $ check = True

        jump choice0_done


return 