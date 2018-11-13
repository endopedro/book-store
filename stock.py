from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Genre, Book, User

engine = create_engine('sqlite:///book_store.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create bot user
User1 = User(name="BookBot", email="bookbot@bookstore.fake",
             picture='https://imbot-one.mybluemix.net/image/bot-1-b.png')
session.add(User1)
session.commit()

# Create genre Fiction
genre1 = Genre(user_id=1, name="Fiction")

session.add(genre1)
session.commit()

book1 = Book(user_id=1,
             title="The Storyteller's Secret: A Novel",
             author="Sejal Badani",
             price="$9.99",
             genre=genre1,
             cover="https://images-na.ssl-images-amazon.com/images/I/51GC3g1S"
                   "SXL._SY346_.jpg",
             synopsis="From the bestselling author of Trail of Broken Wings c"
                      "omes an epic story of the unrelenting force of love, t"
                      "he power of healing, and the invincible desire to drea"
                      "m.")

session.add(book1)
session.commit()

book2 = Book(user_id=1,
             title="The Outsider: A Novel",
             author="Stephen King",
             price="$17.23",
             genre=genre1,
             cover="https://images-na.ssl-images-amazon.com/images/I/51h%2BIh"
                   "txG3L._SX327_BO1,204,203,200_.jpg",
             synopsis="An unspeakable crime. A confounding investigation. At "
                      "a time when the King brand has never been stronger, he"
                      " has delivered one of his most unsettling and compulsi"
                      "vely readable stories.")

session.add(book2)
session.commit()

book3 = Book(user_id=1,
             title="Crazy Rich Asians",
             author="Kevin Kwan",
             price="$96.98",
             genre=genre1,
             cover="https://images-na.ssl-images-amazon.com/images/I/410tUCg8"
                   "-dL.jpg",
             synopsis="When New Yorker Rachel Chu agrees to spend the summer "
                      "in Singapore with her boyfriend, Nicholas Young, she e"
                      "nvisions a humble family home and quality time with th"
                      "e man she hopes to marry.")

session.add(book3)
session.commit()

book4 = Book(user_id=1,
             title="The Royal Nanny: A Novel",
             author="Karen Harper",
             price="$20.78",
             genre=genre1,
             cover="https://images-na.ssl-images-amazon.com/images/I/51fK71fN"
                   "zLL.jpg",
             synopsis="Based on a seldom-told true story, this novel is perfe"
                      "ct for everyone who is fascinated by Britain's royal f"
                      "amily-a behind the scenes look into the nurseries of l"
                      "ittle princes and the foibles of big princes.")

session.add(book4)
session.commit()

book5 = Book(user_id=1,
             title="Small Town Rumors",
             author="Carolyn Brown",
             price="$8.00",
             genre=genre1,
             cover="https://images-na.ssl-images-amazon.com/images/I/51hAbuSp"
                   "opL.jpg",
             synopsis="Everyone is talking about Jennie Sue Baker and the mes"
                      "s she made of her life in New York. The former high sc"
                      "hool queen bee-and wealthy darling of Bloom, Texas-has"
                      " returned home after all these years, riding on a comm"
                      "on bus and bearing two bounced alimony checks")

session.add(book5)
session.commit()

book6 = Book(user_id=1,
             title="Texas Ranger",
             author="James Patterson",
             price="$18.49",
             genre=genre1,
             cover="https://images-na.ssl-images-amazon.com/images/I/51oTpO5m"
                   "PcL.jpg",
             synopsis="In James Patterson's white-hot Western thriller, a Tex"
                      "as Ranger fights for his life, his freedom, and the to"
                      "wn he loves as he investigates his ex-wife's murder. ")

session.add(book6)
session.commit()


# Create genre Absurdist
genre2 = Genre(user_id=1, name="Absurdist")

session.add(genre2)
session.commit()


book1 = Book(user_id=1,
             title="The Master and Margarita ",
             author="Mikhail Bulgakov",
             price="$69.99",
             genre=genre2,
             cover="https://images-na.ssl-images-amazon.com/images/I/41NSZENd"
                   "bFL._SX322_BO1,204,203,200_.jpg",
             synopsis="The underground masterpiece of twentieth-century Russi"
                      "an fiction, this classic novel was written during Stal"
                      "in's regime and could not be published until many year"
                      "s after its author's death.")

session.add(book1)
session.commit()


book2 = Book(user_id=1,
             title="Eleanor, or, The Rejection of the Progress of Love",
             author="Anna Moschovakis",
             price="$11.85",
             genre=genre2,
             cover="https://images-na.ssl-images-amazon.com/images/I/61R2OjuO"
                   "6oL._SX336_BO1,204,203,200_.jpg",
             synopsis="A novel about a woman writing a novel about a woman wh"
                      "o writes-Eleanor, or, The Rejection of the Progress of"
                      " Love is a sexy, earthy, bracingly intelligent examina"
                      "tion of the vicissitudes of grief, ambition, aging, in"
                      "formation overload, compassion fatigue, and a data-cen"
                      "tric understanding of self; the relative merits of giv"
                      "ing up or giving in; the seductive myth of progress; a"
                      "nd the condition of being a thinking and feeling (gend"
                      "ered, raced) inhabitant of an unthinkable, numbing wor"
                      "ld.")

session.add(book2)
session.commit()


book3 = Book(user_id=1,
             title="Gilda Trillim: Shepherdess of Rats",
             author="Steven L. Peck",
             price="$15.00",
             genre=genre2,
             cover="https://images-na.ssl-images-amazon.com/images/I/51KHuwDJ"
                   "cDL.jpg",
             synopsis="Steven L. Peck's intriguing, literary narrative follow"
                      "s Gilda Trillim's many adventures; from her origins on"
                      " a potato farm in Idaho, to an Orthodox Convent in the"
                      " Soviet Union, to her life as a badminton champion... "
                      "When Gilda is taken prisoner during the Vietnam war, s"
                      "he finds comfort in the company of the rats who cohabi"
                      "t her cell. Follow Gilda as she struggles to comprehen"
                      "d the meaning of life in this uncanny, philosophical n"
                      "ovel which explores Mormonism, spirituality and what i"
                      "t means to be human.")

session.add(book3)
session.commit()


book4 = Book(user_id=1,
             title="Spaceman of Bohemia",
             author="Jaroslav Kalfar",
             price="$9.99",
             genre=genre2,
             cover="https://images-na.ssl-images-amazon.com/images/I/51CFZ%2B"
                   "0O7sL._SX331_BO1,204,203,200_.jpg",
             synopsis="Orphaned as a boy, raised in the Czech countryside by "
                      "his doting grandparents, Jakub Prochazka has risen fro"
                      "m small-time scientist to become the country's first a"
                      "stronaut. When a dangerous solo mission to Venus offer"
                      "s him both the chance at heroism he's dreamt of, and a"
                      " way to atone for his father's sins as a Communist inf"
                      "ormer, he ventures boldly into the vast unknown. But i"
                      "n so doing, he leaves behind his devoted wife, Lenka, "
                      "whose love, he realizes too late, he has sacrificed on"
                      " the altar of his ambitions. ")

session.add(book4)
session.commit()


book5 = Book(user_id=1,
             title="The Invoice: A Novel",
             author="Jonas Karlsson",
             price="$9.99",
             genre=genre2,
             cover="https://images-na.ssl-images-amazon.com/images/I/51hTIzXy"
                   "AyL.jpg",
             synopsis="Hilarious, profound, and achingly true-to-life, Jonas "
                      "Karlsson's new novel explores the true nature of happi"
                      "ness through the eyes of hero you won't soon forget. A"
                      " passionate film buff, our hero's life revolves around"
                      " his part-time job at a video store, the company of a "
                      "few precious friends, and a daily routine that more of"
                      "ten than not concludes with pizza and movie in his tre"
                      "asured small space in Stockholm. When he receives an a"
                      "stronomical invoice from a random national bureaucrati"
                      "c agency, everything will tumble into madness as he ca"
                      "lls the hotline night and day to find out why he is th"
                      "e recipient of the largest bill in the entire country.")

session.add(book5)
session.commit()


book6 = Book(user_id=1,
             title="Las Cronicas de Narnia (Spanish Edition)",
             author="C. S. Lewis",
             price="$9.95",
             genre=genre2,
             cover="https://images-na.ssl-images-amazon.com/images/I/51F3eBwY"
                   "WbL.jpg",
             synopsis="Durante mas de cincuenta anos, Las Cronicas de Narnia "
                      "han transcendido el genero de la fantasia, formando pa"
                      "rte del canon de la literatura clasica. Cada uno de lo"
                      "s siete libros es una obra maestra, que sumerge a los "
                      "lectores en un terreno donde la magia es realidad, y e"
                      "l resultado es un mundo ficticio cuyo ambito ha fascin"
                      "ado a generaciones.")

session.add(book6)
session.commit()


# Create genre Romance
genre3 = Genre(user_id=1, name="Romance")

session.add(genre3)
session.commit()

book1 = Book(user_id=1,
             title="Two Weeks Notice",
             author="Whitney G.",
             price="$2.96",
             genre=genre3,
             cover="https://images-na.ssl-images-amazon.com/images/I/51rlfmnj"
                   "1fL.jpg",
             synopsis="That's the version of my two weeks' notice I should've"
                      " sent to my boss, because the more professional versio"
                      "n--the one where I said I was \"grateful for all the o"
                      "pportunities,\" and \"honored by all the rewarding exp"
                      "eriences\" over the years?")

session.add(book1)
session.commit()

book2 = Book(user_id=1,
             title="Not So Nice Guy",
             author="R.S. Grey ",
             price="$14.99",
             genre=genre3,
             cover="https://images-na.ssl-images-amazon.com/images/I/41iEr215"
                   "2yL.jpg",
             synopsis="A full-length STANDALONE romantic comedy from USA TODA"
                      "Y bestselling author R.S. Grey.")

session.add(book2)
session.commit()

book3 = Book(user_id=1,
             title="His Banana",
             author="Penelope Bloom",
             price="$11.06",
             genre=genre3,
             cover="https://images-na.ssl-images-amazon.com/images/I/41pinVPu"
                   "y0L.jpg",
             synopsis="My new boss likes rules, but there's one nobody dares "
                      "to break... No touching his banana. ")

session.add(book3)
session.commit()

book4 = Book(user_id=1,
             title="Long Hard Truckers",
             author="Madison Faye",
             price="$0.96",
             genre=genre3,
             cover="https://images-na.ssl-images-amazon.com/images/I/51MobIC3"
                   "LrL.jpg",
             synopsis="The two of us? We've seen our share of hell. But after"
                      " we left the Marines, all we wanted was our big rig tr"
                      "uck, our own rules, and the freedom of the open road5")

session.add(book4)
session.commit()

book5 = Book(user_id=1,
             title="Still Not Over You: An Enemies to Lovers Romance",
             author="Nicole Snow",
             price="$3.96",
             genre=genre3,
             cover="https://images-na.ssl-images-amazon.com/images/I/51c7CXd3"
                   "QdL.jpg",
             synopsis="I'm SO over that gorgeous, scary, heartbreaking man wh"
                      "o hates my guts. I'm just counting on him to save my l"
                      "ife.")

session.add(book5)
session.commit()

book6 = Book(user_id=1,
             title="Small Town Rumors",
             author="Carolyn Brown",
             price="$5.66",
             genre=genre3,
             cover="https://images-na.ssl-images-amazon.com/images/I/51hAbuSp"
                   "opL.jpg",
             synopsis="From New York Times bestselling author Carolyn Brown c"
                      "omes a funny heartache of a novel about overcoming the"
                      " past, confronting the future, and defying all expecta"
                      "tions.")

session.add(book6)
session.commit()


# Create genre Travel
genre4 = Genre(user_id=1, name="Travel")

session.add(genre4)
session.commit()

book1 = Book(user_id=1,
             title="The Lost Art of Reading Nature's Signs: Use Outdoor Clue"
                   "s to Find Your Way, Predict the Weather, Locate Water, T"
                   "rack Animals-and Other Forgotten Skills",
             author="Tristan Gooley",
             price="$82.38",
             genre=genre4,
             cover="https://images-na.ssl-images-amazon.com/images/I/51orF2IJ"
                   "n8L.jpg",
             synopsis="When writer and navigator Tristan Gooley journeys outs"
                      "ide, he sees a natural world filled with clues. The ro"
                      "ots of a tree indicate the sun's direction; the Big Di"
                      "pper tells the time; a passing butterfly hints at the "
                      "weather; a sand dune reveals prevailing wind; the scen"
                      "t of cinnamon suggests altitude; a budding flower poin"
                      "ts south. To help you understand nature as he does, Go"
                      "oley shares more than 850 tips for forecasting, tracki"
                      "ng, and more, gathered from decades spent walking the "
                      "landscape around his home and around the world. Whethe"
                      "r you're walking in the country or city, along a coast"
                      "line, or by night, this is the ultimate resource on wh"
                      "at the land, sun, moon, stars, plants, animals, and cl"
                      "ouds can reveal-if you only know how to look!")

session.add(book1)
session.commit()

book2 = Book(user_id=1,
             title="Bangkok: Recipes and Stories from the Heart of Thailand",
             author="Leela Punyaratabandhu",
             price="$15.00",
             genre=genre4,
             cover="https://images-na.ssl-images-amazon.com/images/I/61N70fOT"
                   "Z6L.jpg",
             synopsis="From one of the most respected authorities on Thai coo"
                      "king comes this beautiful and deeply personal ode to B"
                      "angkok, the top-ranked travel destination in the world"
                      ".")

session.add(book2)
session.commit()

book3 = Book(user_id=1,
             title="2019 Rand McNally Large Scale Road Atlas",
             author="Rand McNally",
             price="$14.52",
             genre=genre4,
             cover="https://images-na.ssl-images-amazon.com/images/I/51tOYq2s"
                   "fNL._SX381_BO1,204,203,200_.jpg",
             synopsis="Give road-weary eyes a break with this spiral-bound La"
                      "rge Scale edition featuring all the accuracy you've co"
                      "me to expect from Rand McNally, only bigger. Updated a"
                      "tlas contains maps of every U.S. state that are 35% la"
                      "rger than the standard atlas version plus over 350 det"
                      "ailed city inset and national park maps and a comprehe"
                      "nsive, unabridged index")

session.add(book3)
session.commit()

book4 = Book(user_id=1,
             title="AWOL on the Appalachian Trail",
             author="David Miller",
             price="$8.96",
             genre=genre4,
             cover="https://images-na.ssl-images-amazon.com/images/I/41sVw2cM"
                   "TbL.jpg",
             synopsis="In 2003, software engineer David Miller left his job, "
                      "family, and friends to fulfill a dream and hike the Ap"
                      "palachian Trail. AWOL on the Appalachian Trail is Mill"
                      "er's account of this thru-hike along the entire 2,172 "
                      "miles from Georgia to Maine. On page after page, reade"
                      "rs are treated to rich descriptions of the valleys and"
                      " mountains, the isolation and reverie, the inspiration"
                      " that fueled his quest, and the life-changing moments "
                      "that can only be experienced when dreams are pursued.")

session.add(book4)
session.commit()

book5 = Book(user_id=1,
             title="Take Off Your Shoes: One Man's Journey from the Boardroom"
                   " to Bali and Back",
             author="Ben Feder",
             price="$4.70",
             genre=genre4,
             cover="https://images-na.ssl-images-amazon.com/images/I/51s1DAcU"
                   "dVL.jpg",
             synopsis="The Eat, Pray, Love for busy executives, Take Off Your"
                      " Shoes invites the reader to join a journey of self-re"
                      "discovery.")

session.add(book5)
session.commit()


book6 = Book(user_id=1,
             title="Dear Bob and Sue",
             author="Matt Smith ",
             price="$9.73",
             genre=genre4,
             cover="https://images-na.ssl-images-amazon.com/images/I/513Qp1XW"
                   "QUL.jpg",
             synopsis="Dear Bob and Sue is the story of our (Matt and Karen S"
                      "mith) journey to all 59 U.S. National Parks. We wrote "
                      "the book as a series of emails to our friends, Bob and"
                      " Sue, in which we share our humorous and quirky observ"
                      "ations. It is at times irreverent, unpredictable and s"
                      "arcastic, all in the spirit of humor.")

session.add(book6)
session.commit()


# Create genre History
genre5 = Genre(user_id=1, name="History")

session.add(genre5)
session.commit()


book1 = Book(user_id=1,
             title="The Russia Hoax: The Illicit Scheme to Clear Hillary Clin"
                   "ton and Frame Donald Trump",
             author="Gregg Jarrett",
             price="$16.79",
             genre=genre5,
             cover="https://images-na.ssl-images-amazon.com/images/I/51bcQvf%"
                   "2B-pL._SX329_BO1,204,203,200_.jpg",
             synopsis="With insightful analysis and a fact-filled narrative, "
                      "The Russia Hoax delves deeply into Democrat wrongdoing"
                      ".")

session.add(book1)
session.commit()

book2 = Book(user_id=1,
             title="Helmet for My Pillow: From Parris Island to the Pacific",
             author="Robert Leckie",
             price="$117.86",
             genre=genre5,
             cover="https://images-na.ssl-images-amazon.com/images/I/514vh4cp"
                   "nZL.jpg",
             synopsis="Here is one of the most riveting first-person accounts"
                      " ever to come out of World War II. Robert Leckie enlis"
                      "ted in the United States Marine Corps in January 1942,"
                      " shortly after the Japanese attack on Pearl Harbor.")

session.add(book2)
session.commit()

book3 = Book(user_id=1,
             title="Born Survivors: Three Young Mothers and Their Extraordina"
                   "ry Story of Courage, Defiance, and Hope",
             author="Wendy Holden",
             price="$44.96",
             genre=genre5,
             cover="https://images-na.ssl-images-amazon.com/images/I/51xVPLrt"
                   "1jL.jpg",
             synopsis="The Nazis murdered their husbands but concentration ca"
                      "mp prisoners Priska, Rachel, and Anka would not let ev"
                      "il take their unborn children too-a remarkable true st"
                      "ory that will appeal to readers of The Lost and The Na"
                      "zi Officer's Wife, Born Survivors celebrates three mot"
                      "hers who defied death to give their children life.")

session.add(book3)
session.commit()

book4 = Book(user_id=1,
             title="Abigail and John: Portrait of a Marriage ",
             author="Edith Gelles",
             price="$24.57",
             genre=genre5,
             cover="https://images-na.ssl-images-amazon.com/images/I/51Jr390Q"
                   "2jL.jpg",
             synopsis="Readers who enjoyed Doris Kearns Goodwin's No Ordinary"
                      " Time, Cokie Roberts's Founding Mothers, and David McC"
                      "ullough's John Adams will love \"this eminently readab"
                      "le... charming and sensitive, yet candid and unflinchi"
                      "ng joint biography\" (Daniel Walker Howe, Pulitzer Pri"
                      "ze-winning author of What Hath God Wrought: The Transf"
                      "ormation of America, 1815-1848) of America's original "
                      "\"power couple\": Abigail and John Adams.")

session.add(book4)
session.commit()

book5 = Book(user_id=1,
             title="Night (Night)",
             author="Elie Wiesel",
             price="$4.93",
             genre=genre5,
             cover="https://images-na.ssl-images-amazon.com/images/I/41kkT0WK"
                   "kXL._SX310_BO1,204,203,200_.jpg",
             synopsis="Night is Elie Wiesel's masterpiece, a candid, horrific"
                      ", and deeply poignant autobiographical account of his "
                      "survival as a teenager in the Nazi death camps. This n"
                      "ew translation by Marion Wiesel, Elie's wife and frequ"
                      "ent translator, presents this seminal memoir in the la"
                      "nguage and spirit truest to the author's original inte"
                      "nt. ")

session.add(book5)
session.commit()

book6 = Book(user_id=1,
             title="The Button (Missing collection)",
             author="Wednesday Martin",
             price="$1.99",
             genre=genre5,
             cover="https://images-na.ssl-images-amazon.com/images/I/51D8UIxy"
                   "utL.jpg",
             synopsis="Press here for pleasure. Only Wednesday Martin, New Yo"
                      "rk Times bestselling author of Primates of Park Avenue"
                      ", could combine anthropology, anecdote, and adventure "
                      "to hilariously right an anatomic wrong.")

session.add(book6)
session.commit()

print "Books successfully added"
