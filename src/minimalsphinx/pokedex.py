class StarterPokemon:

    """
    This class defined one of the starter Pokémon given to the player by
    |professor| at the start of Pokémon Red, Green, Blue, FireRed, and
    LeafGreen.

    Actual Pokémon can be created by calling the specific classes defining the
    starter Pokémon types. Pokémon can be carried in a Pokéball.

    You can see more details about Pokémon at :ref:`starter`.

    .. |professor| replace:: *Professor Oak*
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
    starting at level 32. Bulbasaur can be stored in a regular |pokeball|.

    Along with :class:`Charmander` and :class:`Squirtle`, Bulbasaur is one of
    three starter Pokémon of Kanto available at the beginning of Pokémon Red,
    Green, Blue, FireRed, and LeafGreen.

    .. warning:: Be careful!

       Bulbasaur is a grass-type Pokémon, but Mega Venusaur and Gigantamax
       Venusaur are also Poison Pokémon.

    Attributes
    ----------
    nickname: str
        The nickname of the pokemon.

    Notes
    -----

    See wikipedia_ for more details.

    .. _wikipedia: https://en.wikipedia.org/wiki/Bulbasaur

    .. |pokeball| image:: https://upload.wikimedia.org/wikipedia/commons/b/b1/Pok%C3%A9ball.png

    """

    def __init__(self, nickname=None):
        self.name = "Bulbasaur"
        self.pokemon_type = {"grass", "poison"}
        self.ability = "Overgrow"
        self.evolution = ["Ivysaur", "Venusaur", "Mega Venusaur", "Gigantamax Venusaur"]
        self._nickname = nickname

    @property
    def nickname(self):
        return self._nickname


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

    .. warning:: title

        This is an important directive for testing.
    """

    def __init__(self):
        self.name = "Squirtle"
        self.pokemon_type = {"water"}
        self.ability = "Torrent"
        self.evolution = ["Wartortle"]
