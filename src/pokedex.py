class StarterPokemon:

    """
    This class defined one of the starter Pokémon given to the player by
    Professor Oak at the start of Pokémon Red, Green, Blue, FireRed, and
    LeafGreen.

    Actual Pokémon can be created by calling the specific classes defining the
    starter Pokémon types. You can see more details about them at :ref:`starter`.
    """

    def __init__(self):
        self.name = None
        self.evolution = None
        self.ability = None
        self.pokemon_type = None
        self.base_stats = dict()

    def who_is_that_pokemon(self):
        """
        Shows the Pokémon name and its evolution.

        Usage:

        .. doctest::

           >>> import pokedex
           >>> friend = pokedex.Bulbasaur()
           >>> friend.who_is_that_pokemon()
           This pokemon is Bulbasaur.
           It will evolve into Ivysaur, Venusaur, Mega Venusaur, Gigantamax Venusaur.
           >>>
        """
        print(f"This pokemon is {self.name}.")
        print(f"It will evolve into {', '.join(self.evolution)}.")


class Bulbasaur(StarterPokemon):
    """
    Bulbasaur is a dual-type Grass/Poison Pokémon introduced in Generation I.

    It evolves into Ivysaur starting at level 16, which evolves into Venusaur
    starting at level 32.

    Along with :class:`Charmander` and :class:`Squirtle`, Bulbasaur is one of
    three starter Pokémon of Kanto available at the beginning of Pokémon Red,
    Green, Blue, FireRed, and LeafGreen.
    """

    def __init__(self):
        self.name = "Bulbasaur"
        self.pokemon_type = {"grass", "poison"}
        self.ability = "Overgrow"
        self.evolution = ["Ivysaur",
                          "Venusaur",
                          "Mega Venusaur",
                          "Gigantamax Venusaur"]


class Charmander(StarterPokemon):
    """
    Charmander is a Fire-type Pokémon introduced in Generation I.

    It evolves into Charmeleon starting at level 16, which evolves into
    Charizard starting at level 36.

    Along with :class:`Bulbasaur` and :class:`Squirtle`, Charmander is one of
    three starter Pokémon of Kanto available at the beginning of Pokémon Red,
    Green, Blue, FireRed, and LeafGreen.

    .. note::

       Charmeleon and Charizard are fire-type Pokémon, but Mega Charizard X and
       Gigantamax Charizard are also Flying Pokémon, while Mega Charizard Y is a
       Dragon-type Pokémon.
    """

    def __init__(self):
        self.name = "Charmander"
        self.pokemon_type = {"fire"}
        self.ability = "Blaze"
        self.evolution = [
            "Charmeleon",
            "Charizard",
            "Mega Charizard X",
            "Mega Charizard Y",
            "Gigantamax Charizard",
        ]


class Squirtle(StarterPokemon):
    """
    Squirtle is a Water-type Pokémon introduced in Generation I.

    It evolves into Wartortle starting at level 16, which evolves into Blastoise
    starting at level 36.

    Along with :class:`Bulbasaur` and :class:`Charmander`, Squirtle is one of
    three starter Pokémon of Kanto available at the beginning of Pokémon Red,
    Green, Blue, FireRed, and LeafGreen.
    """

    def __init__(self):
        self.name = "Squirtle"
        self.pokemon_type = {"water"}
        self.ability = "Torrent"
        self.evolution = ["Wartortle"]

class Caterpie(StarterPokemon):
    """
    For protection, it releases a horrible stench from the antenna on its head to drive away enemies.
    """

    def __init__(self):
        self.name = "Caterpie"
        self.pokemon_type = {"bug"}
        self.ability = "Shield Dust"
        self.evolution = ["Metapod", "Butterfree"]

class Pidgey(StarterPokemon):
    """
    A common sight in forests and woods. It flaps its wings at ground level to kick up blinding sand.

    Very docile. If attacked, it will often kick up sand to protect itself rather than fight back.
    """

    def __init__(self):
        self.name = "Pidgey"
        self.pokemon_type = {"normal", "flying"}
        self.ability = "Keen Eye"
        self.evolution = ["Pidgeotto", "Pidgeot"]


class Ratata(StarterPokemon):
    """
    Bites anything when it attacks. Small and very quick, it is a common sight in many places.

    It is cautious in the extreme. Even while it is asleep, it constantly listens by moving its ears around.
    """

    def __init__(self):
        self.name = "Ratata"
        self.pokemon_type = {"normal"}
        self.ability = "Run Away"
        self.evolution = ["Raticate"]


class Spearow(StarterPokemon):
    """
    Eats bugs in grassy areas. It has to flap its short wings at high speed to stay airborne.

    Inept at flying high. However, it can fly around very fast to protect its territory.
    """

    def __init__(self):
        self.name = "Spearow"
        self.pokemon_type = {"normal", "flying"}
        self.ability = "Keen Eye"
        self.evolution = ["Fearow"]


class Pikachu(StarterPokemon):
    """
    When several of these Pokémon gather, their electricity could build and cause lightning storms.

    It keeps its tail raised to monitor its surroundings. If you yank its tail, it will try to bite you.
    """

    def __init__(self):
        self.name = "Pikachu"
        self.pokemon_type = {"electric"}
        self.ability = "Static"
        self.evolution = ["Raichu", "Alolan Raichu"]

class Jigglypuff(StarterPokemon):
    """
    When its huge eyes light up, it sings a mysteriously soothing melody that lulls its enemies to sleep.

    Nothing can avoid falling asleep hearing a Jigglypuff's song. The sound waves of its singing voice match the brain waves of someone in a deep sleep.
    """

    def __init__(self):
        self.name = "Jigglypuff"
        self.pokemon_type = {"normal", "fairy"}
        self.ability = "Cute Charm"
        self.evolution = ["Wigglytuff"]


class Meowth(StarterPokemon):
    """
    Adores round objects. It wanders the streets on a nightly basis to look for dropped loose change.

    It is nocturnal in nature. If it spots something shiny, its eyes glitter brightly.
    """

    def __init__(self):
        self.name = "Meowth"
        self.pokemon_type = {"normal"}
        self.ability = "Pickup"
        self.evolution = ["Persian", "Alolan Persian"]


class Psyduck(StarterPokemon):
    """
    While lulling its enemies with its vacant look, this wily Pokémon will use psychokinetic powers.

    It is constantly wracked by a headache. When the headache turns intense, it begins using mysterious powers.
    """

    def __init__(self):
        self.name = "Psyduck"
        self.pokemon_type = {"water"}
        self.ability = "Damp"
        self.evolution = ["Golduck"]


class Abra(StarterPokemon):
    """
    Using its ability to read minds, it will identify impending danger and teleport to safety.

    It sleeps for 18 hours a day. Even when awake, it teleports itself while remaining seated.
    """

    def __init__(self):
        self.name = "Abra"
        self.pokemon_type = {"psychic"}
        self.ability = "Synchronize"
        self.evolution = ["Kadabra", "Alakazam"]


class Machop(StarterPokemon):
    """
    Loves to build its muscles. It trains in all styles of martial arts to become even stronger.

    It loves working out. As it gazes at its muscles, which continue to swell day by day, it becomes more and more dedicated to its training.
    """

    def __init__(self):
        self.name = "Machop"
        self.pokemon_type = {"fighting"}
        self.ability = "Guts"
        self.evolution = ["Machoke", "Machamp"]


class Bellsprout(StarterPokemon):
    """
    A carnivorous Pokémon that traps and eats bugs. It uses its root feet to soak up needed moisture.

    If it notices anything that moves, it immediately flings its vine at the object.
    """

    def __init__(self):
        self.name = "Bellsprout"
        self.pokemon_type = {"grass", "poison"}
        self.ability = "Chlorophyll"
        self.evolution = ["Weepinbell", "Victreebel"]


class Geodude(StarterPokemon):
    """
    Commonly found near mountain trails and the like. If you step on one by accident, it gets angry.

    It uses both hands to climb precipitous cliffs. People who see it in action have been known to take up bouldering.
    """

    def __init__(self):
        self.name = "Geodude"
        self.pokemon_type = {"rock", "ground"}
        self.ability = "Rock Head"
        self.evolution = ["Graveler", "Golem"]

class Ponyta(StarterPokemon):
    """
    Capable of jumping incredibly high. Its hooves and sturdy legs absorb the impact of a hard landing.

    Its hooves are 10 times harder than diamonds. It can trample anything completely flat in little time.
    """

    def __init__(self):
        self.name = "Ponyta"
        self.pokemon_type = {"fire"}
        self.ability = "Run Away"
        self.evolution = ["Rapidash", "Galarian Rapidash"]


class Slowpoke(StarterPokemon):
    """
    Incredibly slow and sluggish. It is quite content to loll about without worrying about the time.

    It is always so absent-minded that it won't react, even if its flavorful tail is bitten.
    """

    def __init__(self):
        self.name = "Slowpoke"
        self.pokemon_type = {"water", "psychic"}
        self.ability = "Oblivious"
        self.evolution = ["Slowbro", "Mega Slowbro", "Slowking", "Galarian Slowbro"]


class Magnemite(StarterPokemon):
    """
    Uses anti-gravity to stay suspended. Appears without warning and uses Thunder Wave and similar moves.

    The units at the sides of its body generate anti-gravity energy to keep it aloft in the air.
    """

    def __init__(self):
        self.name = "Magnemite"
        self.pokemon_type = {"electric", "steel"}
        self.ability = "Magnet Pull"
        self.evolution = ["Magneton", "Magnezone"]


class Farfetchd(StarterPokemon):
    """
    The sprig of green onions it holds is its weapon. It is used much like a metal sword.

    Although it can cut steel with its beak, it will not pick up a blade if it is dirty.
    """

    def __init__(self):
        self.name = "Farfetch'd"
        self.pokemon_type = {"normal", "flying"}
        self.ability = "Keen Eye"
        self.evolution = ["Sirfetch'd", "Galarian Farfetch'd"]


class Doduo(StarterPokemon):
    """
    A bird that makes up for its poor flying with its fast foot speed. Leaves giant footprints.

    It lives on a grassy plain where it can see a long way. If it sees an enemy, it runs away at 60 mph.
    """

    def __init__(self):
        self.name = "Doduo"
        self.pokemon_type = {"normal", "flying"}
        self.ability = "Run Away"
        self.evolution = ["Dodrio"]


class Seel(StarterPokemon):
    """
    The protruding horn on its head is very hard. It is used for bashing through thick ice.

    Seel hunts for prey in the frigid sea underneath sheets of ice. When it needs to breathe, it punches a hole through the ice with the sharply protruding section of its head.
    """

    def __init__(self):
        self.name = "Seel"
        self.pokemon_type = {"water"}
        self.ability = "Thick Fat"
        self.evolution = ["Dewgong"]


class Grimer(StarterPokemon):
    """
    Appears in filthy areas. Thrives by sucking up polluted sludge that is pumped out of factories.

    Wherever Grimer has passed, so many germs are left behind that no plants will ever grow again.
    """

    def __init__(self):
        self.name = "Grimer"
        self.pokemon_type = {"poison"}
        self.ability = "Stench"
        self.evolution = ["Muk", "Alolan Muk"]


class Shellder(StarterPokemon):
    """
    Its hard shell repels any kind of attack. It is vulnerable only when its shell is open.

    Even though it is encased in a sturdy shell, the body inside is tender. It can't withstand a harsh attack.
    """

    def __init__(self):
        self.name = "Shellder"
        self.pokemon_type = {"water"}
        self.ability = "Shell Armor"
        self.evolution = ["Cloyster"]


class Gastly(StarterPokemon):
    """
    A being that exists as a thin gas. It can topple an Indian elephant by enveloping the prey in two seconds.

    It wraps its opponent in its gas-like body, slowly weakening its prey by poisoning it through the skin.
    """

    def __init__(self):
        self.name = "Gastly"
        self.pokemon_type = {"ghost", "poison"}
        self.ability = "Levitate"
        self.evolution = ["Haunter", "Gengar", "Mega Gengar"]


class Onix(StarterPokemon):
    """
    Burrows at high speed in search of food. The tunnels it leaves are used as homes by Diglett.

    As it digs through the ground, it absorbs many hard objects. This is what makes its body so solid.
    """

    def __init__(self):
        self.name = "Onix"
        self.pokemon_type = {"rock", "ground"}
        self.ability = "Rock Head"
        self.evolution = ["Steelix", "Mega Steelix"]


class Drowzee(StarterPokemon):
    """
    Puts enemies to sleep, then eats their dreams. Occasionally gets sick from eating bad dreams.

    It puts its enemy to sleep and eats the victim's dreams. It is known to visit children to steal their dreams through the holes in their noses.
    """

    def __init__(self):
        self.name = "Drowzee"
        self.pokemon_type = {"psychic"}
        self.ability = "Insomnia"
        self.evolution = ["Hypno"]


class Krabby(StarterPokemon):
    """
    Its pincers are superb weapons. They sometimes break off during battle, but they grow back fast.

    If it loses a pincer, it somehow becomes incapable of walking sideways. However, it can still live on in the water.
    """

    def __init__(self):
        self.name = "Krabby"
        self.pokemon_type = {"water"}
        self.ability = "Hyper Cutter"
        self.evolution = ["Kingler", "Galarian Kingler"]


class Voltorb(StarterPokemon):
    """
    It was discovered when Poké Balls were introduced. It is said that there is some connection.

    It was discovered at the site of a meteor strike 50 years ago. Its own energy source is its main enemy.
    """

    def __init__(self):
        self.name = "Voltorb"
        self.pokemon_type = {"electric"}
        self.ability = "Soundproof"
        self.evolution = ["Electrode"]
