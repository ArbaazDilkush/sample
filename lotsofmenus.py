from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Article, Base, MenuItem, User

engine = create_engine('sqlite:///articlemenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

article1 = Article(user_id=1,name="Advanced Technology")

session.add(article1)
session.commit()

menuItem2 = MenuItem(user_id=1,name="Cyber Security News", description="Focusing on cyberspace security issues, this open access journal Cybersecurity publishes high quality research and expert reviews to report the latest research.",
                     price="$27.50", course="Computer Science", article=article1)

session.add(menuItem2)
session.commit()


menuItem1 = MenuItem(user_id=1,name="Internet of Things", description="Internet of Things is the concept of connecting any device to the Internet and to other connected devices",
                     price="$19.99", course="Computer Science", article=article1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1,name="Hydraulics", description="Standard to explain everything needed to know to professionally design a system",
                     price="$35.50", course="Civil", article=article1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1,name="Digital Circuits", description="This article is related to circuits.",
                     price="$23.99", course="Electronics and Communication", article=article1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1,name="Bioelectical Sensors", description="Specialized for sensors. And very related to electronics.",
                     price="$27.99", course="Electrical and Electronics", article=article1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1,name="Gear Boxes", description="Covers the topics of all gear boxes and equivalent to mechanical system.",
                     price="$31.99", course="Mechanical", article=article1)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1,name="Fluid Mechanics", description="Covers every topic of FM",
                     price="$25.99", course="Civil", article=article1)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(user_id=1,name="Fundamentals of Power Electronics", description="Working principles, operating modes and analysis of DC-DC, DC-AC, AC-DC, and AC-AC converters would be covered for a variety of loads.",
                     price="$33.49", course="Electronics and Communication", article=article1)

session.add(menuItem7)
session.commit()



article2 = Article(name="Updated Technology")

session.add(article2)
session.commit()


menuItem1 = MenuItem(name="Python", description="",
                     price="$37.99", course="Computer Science", article=article2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(
    name="Peking Duck", description=" A famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook", price="$25", course="Entree", article=article2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Spicy Tuna Roll", description="Seared rare ahi, avocado, edamame, cucumber with wasabi soy sauce ",
                     price="15", course="Entree", article=article2)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Nepali Momo ", description="Steamed dumplings made with vegetables, spices and meat. ",
                     price="12", course="Entree", article=article2)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Beef Noodle Soup", description="A Chinese noodle soup made of stewed or red braised beef, beef broth, vegetables and Chinese noodles.",
                     price="14", course="Entree", article=article2)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(name="Ramen", description="a Japanese noodle soup dish. It consists of Chinese-style wheat noodles served in a meat- or (occasionally) fish-based broth, often flavored with soy sauce or miso, and uses toppings such as sliced pork, dried seaweed, kamaboko, and green onions.",
                     price="12", course="Entree", article=article2)

session.add(menuItem6)
session.commit()


# Menu for Panda Garden
article1 = Article(name="Panda Garden")

session.add(article1)
session.commit()


menuItem1 = MenuItem(name="Pho", description="a Vietnamese noodle soup consisting of broth, linguine-shaped rice noodles called banh pho, a few herbs, and meat.",
                     price="$8.99", course="Entree", article=article1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Chinese Dumplings", description="a common Chinese dumpling which generally consists of minced meat and finely chopped vegetables wrapped into a piece of dough skin. The skin can be either thin and elastic or thicker.",
                     price="$6.99", course="Appetizer", article=article1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Gyoza", description="The most prominent differences between Japanese-style gyoza and Chinese-style jiaozi are the rich garlic flavor, which is less noticeable in the Chinese version, the light seasoning of Japanese gyoza with salt and soy sauce, and the fact that gyoza wrappers are much thinner",
                     price="$9.95", course="Entree", article=article1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Stinky Tofu", description="Taiwanese dish, deep fried fermented tofu served with pickled cabbage.",
                     price="$6.99", course="Entree", article=article1)

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$9.50", course="Entree", article=article1)

session.add(menuItem2)
session.commit()


# Menu for Thyme for that
article1 = Article(name="Thyme for That Vegetarian Cuisine ")

session.add(article1)
session.commit()


menuItem1 = MenuItem(name="Tres Leches Cake", description="Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.",
                     price="$2.99", course="Dessert", article=article1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Mushroom risotto", description="Portabello mushrooms in a creamy risotto",
                     price="$5.99", course="Entree", article=article1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Honey Boba Shaved Snow", description="Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi",
                     price="$4.50", course="Dessert", article=article1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Cauliflower Manchurian", description="Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions",
                     price="$6.95", course="Appetizer", article=article1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Aloo Gobi Burrito", description="Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom",
                     price="$7.95", course="Entree", article=article1)

session.add(menuItem5)
session.commit()

menuItem2 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$6.80", course="Entree", article=article1)

session.add(menuItem2)
session.commit()


# Menu for Tony's Bistro
article1 = Article(name="Tony\'s Bistro ")

session.add(article1)
session.commit()


menuItem1 = MenuItem(name="Shellfish Tower", description="Lobster, shrimp, sea snails, crawfish, stacked into a delicious tower",
                     price="$13.95", course="Entree", article=article1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Chicken and Rice", description="Chicken... and rice",
                     price="$4.95", course="Entree", article=article1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Mom's Spaghetti", description="Spaghetti with some incredible tomato sauce made by mom",
                     price="$6.95", course="Entree", article=article1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)",
                     description="Milk, cream, salt, ..., Liquid nitrogen magic", price="$3.95", course="Dessert", article=article1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Tonkatsu Ramen", description="Noodles in a delicious pork-based broth with a soft-boiled egg",
                     price="$7.95", course="Entree", article=article1)

session.add(menuItem5)
session.commit()


# Menu for Andala's
article1 = Article(name="Andala\'s")

session.add(article1)
session.commit()


menuItem1 = MenuItem(name="Lamb Curry", description="Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.",
                     price="$9.95", course="Entree", article=article1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Chicken Marsala", description="Chicken cooked in Marsala wine sauce with mushrooms",
                     price="$7.95", course="Entree", article=article1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Potstickers", description="Delicious chicken and veggies encapsulated in fried dough.",
                     price="$6.50", course="Appetizer", article=article1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Nigiri Sampler", description="Maguro, Sake, Hamachi, Unagi, Uni, TORO!",
                     price="$6.75", course="Appetizer", article=article1)

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$7.00", course="Entree", article=article1)

session.add(menuItem2)
session.commit()


# Menu for Auntie Ann's
article1 = Article(name="Auntie Ann\'s Diner' ")

session.add(article1)
session.commit()

menuItem9 = MenuItem(name="Chicken Fried Steak", description="Fresh battered sirloin steak fried and smothered with cream gravy",
                     price="$8.99", course="Entree", article=article1)

session.add(menuItem9)
session.commit()


menuItem1 = MenuItem(name="Boysenberry Sorbet", description="An unsettlingly huge amount of ripe berries turned into frozen (and seedless) awesomeness",
                     price="$2.99", course="Dessert", article=article1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Broiled salmon", description="Salmon fillet marinated with fresh herbs and broiled hot & fast",
                     price="$10.95", course="Entree", article=article1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Morels on toast (seasonal)", description="Wild morel mushrooms fried in butter, served on herbed toast slices",
                     price="$7.50", course="Appetizer", article=article1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Tandoori Chicken", description="Chicken marinated in yoghurt and seasoned with a spicy mix(chilli, tamarind among others) and slow cooked in a cylindrical clay or metal oven which gets its heat from burning charcoal.",
                     price="$8.95", course="Entree", article=article1)

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$9.50", course="Entree", article=article1)

session.add(menuItem2)
session.commit()

menuItem10 = MenuItem(name="Spinach Ice Cream", description="vanilla ice cream made with organic spinach leaves",
                      price="$1.99", course="Dessert", article=article1)

session.add(menuItem10)
session.commit()


# Menu for Cocina Y Amor
article1 = Article(name="Cocina Y Amor ")

session.add(article1)
session.commit()


menuItem1 = MenuItem(name="Super Burrito Al Pastor", description="Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa, Tortilla",
                     price="$5.95", course="Entree", article=article1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Cachapa", description="Golden brown, corn-based Venezuelan pancake; usually stuffed with queso telita or queso de mano, and possibly lechon. ",
                     price="$7.99", course="Entree", article=article1)

session.add(menuItem2)
session.commit()


article1 = Article(name="State Bird Provisions")
session.add(article1)
session.commit()

menuItem1 = MenuItem(name="Chantrelle Toast", description="Crispy Toast with Sesame Seeds slathered with buttery chantrelle mushrooms",
                     price="$5.95", course="Appetizer", article=article1)

session.add(menuItem1)
session.commit

menuItem1 = MenuItem(name="Guanciale Chawanmushi", description="Japanese egg custard served hot with spicey Italian Pork Jowl (guanciale)",
                     price="$6.95", course="Dessert", article=article1)

session.add(menuItem1)
session.commit()


menuItem1 = MenuItem(name="Lemon Curd Ice Cream Sandwich", description="Lemon Curd Ice Cream Sandwich on a chocolate macaron with cardamom meringue and cashews",
                     price="$4.25", course="Dessert", article=article1)

session.add(menuItem1)
session.commit()


print "added menu items!"