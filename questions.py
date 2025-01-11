"""
Define a Clue dictionary
"""

# Question_store Format: Question index: [Question text, Answer string, Incorrect guess string, ...
#                               ...Question answered status, Output information]

question_store = {
    "question1": [
        """Ten has three, in Jordan, Jamaica and Japan. T<i>w</i>enty-six 
                  has only two. Find them, and tell me w<i>h</i>at lies between them.""",
        "Lake Kariba",
        "Incorrect", 0,
        {
            "type": "link",
            "content": "None",
            "text": "Correct!",
            "url": "https://youtu.be/BAweCowDVBo",
        }
    ],
    "question2": [
        """Take the surn<i>a</i>me of answer #1 and add a .commercial .United Kingdom. 
                  Here you'll find drummer Chris' firs<i>t</i> band.""",
        "Jabberwocky",
        "Incorrect", 0,
        {
            "type": "string",
            "content": "Bee, desk, hill = island. Jar, house = lake.",
            "text": None,
            "url": None,
        }
    ],
    "question3": [
        "A Filipino bee sits in a jar on a desk in a house on a hill. What's his name?",
        "Vulcan Point",
        "Incorrect", 0,
        {
            "type": "string",
            "content": "Verse 2, line 4, word 3.",
            "text": None,
            "url": None,
        }
    ],
    "question4": [
        """The bearded theorists met in 2023 at Catton hall. 
                  Investigate how the men in the meadow at midnight on Sunday 
                  are familiar with the second to grace the palleton Friday - 
                  though you'll have to lose the team. What is the name of the man in 
                  the waistcoat who wishes luck to us all?""",
        "Gene Kranz",
        "Incorrect", 0,
        {
            "type": "string",
            "content": """********__________********
                                *******/**********\*******
                                *******|****|>****|*******
                                *******\__________/*******
                                **************************
                                *************/************
                                **************************
                                *1:*51.665124,-3.033762***
                                *2:*-44.045750,-65.226751*
                                *3:*-62.595876,-59.899048*
                                *4:*-21.203962,-159.837051
                                *5:*51.758933,-1.213131***
                                *6:*-2.948052,-60.630932**
                                *7:*39.941679,-75.149634**
                                *8:*-0.443651,-91.092365**
                                *9:*44.414800,-73.124304**
                                10:*0.214835,37.460390****
                                11:*-10.474103,105.558866*""",
            "text": None, # Ensure that this one doesn't format in these lines, just wraps around.
            "url": None,
        }
    ],
    "question5": [
        """Did you follow the old man's directions? A string of this many 100 metres, 
                  held at one end by our Filipino friend, traces a circle. Where 
                  blue meets green to the West, 
                  you'll find a prison. Its name is the ans<i>w</i>er to this clue.""",
        "Khuk khi kai",
        "Incorrect", 0,
        {
            "type": "image",
            "content": "periodic.png",
            "text": None,
            "url": None,
        }
    ],
    "question6": [
        """Pluck the first three and last two of our chicken house, and mix them up until
                   you get something with a rhythm to it. Look around in the hunt for Mr X, 
                  can you find one? It may help to remember fr<i>o</i>m where 
                  they originate. If you look 
                  hard enough, the first line's fifth and the second 
                  line's sixth looks a little like
                  the icon of a constellation called...""",
        "Sagittarius",
        "Incorrect", 0,
        {
            "type": "string",
            "content": "-17.786245, 23.338469",
            "text": None,
            "url": None,
        }
    ],
    "question7": [
        "Before Everest was discovered, what was the highest mountain on Earth?", 
        "Everest", 
        "Incorrect", 0,
        {
            "type": "string",
            "content": """11111110010000101001101111111<br>
                                10000010110111101101001000001<br>
                                10111010011101011111101011101<br>
                                10111010110110111000101011101<br>
                                10111010001010011001001011101<br>
                                10000010101011110110001000001<br>
                                11111110101010101010101111111<br>
                                00000000000011001111100000000<br>
                                11111011111001110100010101010<br>
                                10010100010100101001101111010<br>
                                11001110010111100101010101100<br>
                                11010100111110101001011111001<br>
                                00110010010001111000001100000<br>
                                00000100001000011000111111010<br>
                                00011110111011110100100101111<br>
                                01001001101100001001101110011<br>
                                10100110010000111110110100000<br>
                                10101000111110101000011111001<br>
                                10000111010011110101000101101<br>
                                10111000001100101011111110011<br>
                                10101010101001011000111111110<br>
                                00000000111010111000100010010<br>
                                11111110101010111100101011100<br>
                                10000010001101101001100010111<br>
                                10111010100011111110111110111<br>
                                10111010100010111010100100000<br>
                                10111010111001110111000100110<br>
                                10000010100100101110000001101<br>
                                11111110110001011101011011100""",
            "text": None, # This one should probably format in lines, otherwise it'd be impossible
            "url": None,
        }
    ],
    "question8": [
        """Follow Eugene through the free encyclopedia and he'll 
                  take you somewhe<i>r</i>e sunny. Where are you?""",
        "Havana", 
        "Incorrect", 0,
        {
            "type": "string",
            "content": "54.006100, -2.224289",
            "text": None,
            "url": None,
        }
    ],
    "question9": [
        """You've met the four-legged man already. Drop a shark, or a penguin if you're 
                  shouting, and if you stir him up just right, you'll turn this one man into many. 
                  Say their name and they might play you a song.""",
        "Guitarists", 
        "Incorrect", 0,
        {
            "type": "link",
            "content": None,
            "text": "Correct!",
            "url": "https://youtube.com/shorts/gCR7V-HH9_w",
        }
    ],
    "question10": [
        """Clue 7's giant holds the crown for being the highest, but a taller woman 
                   standing alone in the calm, waist deep in water, begs to differ. Visit her, 
                   and find the man who stands atop her head looking beyond Wakea. What are his 
                   three names?""",
        "James Clerk Maxwell", 
        "Incorrect", 0,
        {
            "type": "string",
            "content": "IATA: Scotland, Namibia, England",
            "text": None,
            "url": None,
        }
    ],
    "question11": [
        """Our mountaintop scientist travels Northwest out of his birth city. 
On his journey he:<br><br>
  - travels forth on the second syllable of his second university,<br>
  - passes the lake eleven that has no head,<br>
  - passes the most remote of cities, continuing North,<br>
  - passes the battleground that marked the end of the Napoleonic wars,<br>
  - passes the muddled up chirpy lot<br>
  - follows Garry until he can go no further.<br><br>
When the two roads converge once more, he starts counting the metal men on his right, 
up to his house number as a baby.
Then he looks to his left for a sign.
You'll need two more signs to lead you to an airport in which city?""",
        "Dubai",
        "Incorrect", 0,
        {
            "type": "string",
            "content": "Caballo Blanco",
            "text": None,
            "url": None,
        }
    ],
    "question12": [
        """Eugene showed you a city. This is where we travel to pick up the trail 
                   of Mr X's henchman. What did you learn from clue 11 that could narrow you 
                   down to a specific spot? Here you'll find an icon of the city, but when 
                   was it erected? (<i>d</i>d/mm/yyyy format please)""",
        "29/05/1948",
        "Incorrect", 0,
        {
            "type": "twelve",
            "content": "walls.png", # Need to display text as well as image for this one
            "text": """Having learned about Mr X’s henchman’s presence in Havana,
              you travel there to track him down. You follow his trail to the 
Caballo Blanco statue, as it’s believed he is laying low in an adjacent house,
 owned by his mistress. Excited at the 
prospect of apprehending a henchman and coming one step closer to capturing Mr X, 
you surround the house with your 
men and bust down the doors. However, much to your disappointment, no henchman 
in sight. All you find is a note 
hidden in a cabinet’s false bottom, presumably from the criminal, addressed to 
his mistress. It reads:<br><br><br>


Mi Amor,<br><br>

They have come looking for me, so I must run. I have already made my way to my 
first stop, from here I’ll fly to my final 
destination airport, the location of which you already know. I am to fly there 
as straight as an arrow, however, I fear they 
will be waiting for me when I land, so I have a plan. I will never arrive at my
 destination airport. I will just out of the plane 
during the flight and parachute to freedom, just like the movie stars. They’ll
 never know where I end up. <br><br>

I don’t think they’ll find this letter but just in case they do, I can’t say here
 how where I’m flying from, or how far into the 
flight I’ll make my daring escape. Instead, use your little trick to find it on
 the very walls of this room. <br><br>

After I jump, I’ll travel Southwest until I hit the coast, then catch a short ferry
 to the outer of the two small islands there. 
That’s where I’ll take my refuge.<br><br>

I hope to see you there soon mi amor, come find me.<br><br>

H<br><br><br>


Confused, you look at the walls, which simply show a colourful floral pattern, but 
on closer inspection you find the hidden message. Other clues have given you the henchman's destination airport
, so you piece together his path and find the island on which he is hiding.<br><br>

WHAT IS HIS NAME? ENTER IN MISSION BRIEF UNDER DESCRIPTIONS
""",
            "url": None,
        }
    ],
    "question13": [
        """The elements have shown you the trail of one of the men we seek. They 
                   have told you of the African port town to which he fled, and now we travel 
                   there to track him down. What i<i>s</i> the town called?""",
        "Walvis Bay",
        "Incorrect", 0,
        {
            "type": "string",
            "content": """You arrive in Walvis Bay to search for Mr X's henchman. You 
                                can feel that he is close now, and that you'll soon have him 
                                captured. Your plan is to search slowly around the city, keeping a 
                                low profile while you gather clues on his whereabouts. Unfortunately, 
                                your presence in the small city is not going unnoticed, and despite 
                                your best efforts to remain incognito, word seems to be spreading of 
                                MI6 business in Walvis Bay. You try to speed up the investigation, as 
                                you feel it’s only a matter of time before the henchman is alerted of 
                                your presence and flees once again. <br><br>

                                The following day, your fears are confirmed. A petrol station clerk 
                                comes to you with an account of an encounter they had with a 
                                suspicious individual. They say: <br><br><br>


                                'Hallo spioen. ’n Ou het so halfuur gelede met sy 4x4 by my vulstasie ingery. Hierdie idioot 
                                het sy vragmotor tot op die rand vol petrol gevul en toe weggejaag sonder om te betaal, kan jy my help?'<br><br>

                                'Jy kan na my kringtelevisie kyk as jy wil, dit wys hy het suidoos na die duinlyn gegaan. 
                                Gelukkig het ek daarin geslaag om sy baster kar met my geweer te skiet, en ek het sy brandstoftenk getref. 
                                Sy motor het gesteelde brandstof gepis toe hy weggejaag het. Ek sou sê met 
                                die koers dat dit uitkom, sal hy gelukkig wees om 'n uur se ry te kry voor hy sonder petrol opraak.'<br><br>

                                'Sterkte spioen, ek hoop jy vang die ou. Sê vir hom ek het gesê hy kan in die Kaap gaan kak.' <br><br>


                                You thank the clerk for their help and repay them for the stolen petrol. You follow their instructions 
                                and find that they were correct to make the assumptions they did, as you soon find the henchman. <br><br><br>

                                WHAT IS HIS NAME? ENTER IN MISSION BRIEF UNDER DESCRIPTIONS""",
            "text": None,
            "url": None,
        }
    ],
    "question14": [
        """Our tuneless musicians have taken you to China. A short walk north 
        there is a fishing park. What is it called?""",
        "huaifang",
        "Incorrect", 0,
        {
            "type": "string",
            "content": """You’ve successfully located Jiang Zupeng, the cousin of 
                                one of our fugitives. <br><br>He sits in the park hunched over his phone, not knowing that 
                                you’ve hacked into it. He's unaware that you watch him through his camera, and see his 
                                correspondence with his cousin. He will be the key to find Mr X’s henchman. <br><br>

                                You see that conversation they’ve had so far, as well as Mr Zupeng’s files, which tell 
                                you he is proud of his Chinese zodiac birth animal, <b>the dragon</b>. Unfortunately, you see from their 
                                conversation that the henchman knows better than to outright reveal his location: <br><br><br>


                                                        I don’t understand, how come you’re in hiding again?<br><br>

                                Boss is in trouble, they’re gonna come after me and the boys
                                and try and make us talk<br><br>

                                                                    You okay? Need me to get anything to you?<br><br>

                                Yeah just gotta hide out here for a while. But yea I
                                need someone I can trust on the outside<br><br>

                                                                        Yea I’ve got you. How do I find you?<br><br>

                                Can’t really say here, too risky if they get into your 
                                devices<br><br>

                                                                            …You remember our old code though?<br><br>

                                You think it’s secure enough?<br><br>

                                                                            No one knows how it works but us<br><br>

                                Okay yeah hold on…<br><br>

                                <b>I’m 1906 1905 2019 1970 2009 South of 1963
                                2008 1993 2000 1920 1902</b><br>

                                                    Got you. I can be there this week. I can bring stuff to
                                                    help you get properly off the map. They’ll never find you.<br>

                                Perfect, don’t tell anyone<br>

                                                                                        You got it, sit tight<br><br><br>

                                Reading this, you realise you need to act fast, and get to the henchman before his cousin does. 
                                By the sounds of things, if he beats you to it, you might lose all chance of getting to him, and 
                                without the capture of all three, any chance of finding Mr X are gone. You work 
                                through the night to crack the code and finally manage to find his location, capturing the henchman. <br><br>

                                WHAT IS HIS NAME? ENTER IN MISSION BRIEF UNDER DESCRIPTIONS""",
            "text": None,
            "url": None,
        }
    ],
}
