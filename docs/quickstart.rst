Quickstart
==========

The Pokédex package contains basic information about the three `starter Pokémon <https://bulbapedia.bulbagarden.net/wiki/Starter_Pok%C3%A9mon>`_ from the `core series`_. These are detailed in :doc:`apidocs`.

.. _starter:

About starter Pokémon
---------------------

.. _startpoke:

.. figure:: starter_pokemon.png

   Starter Pokémon from the core series.

As you can see in the :ref:`startpoke` image, these starter Pokémon have different types and abilities, and will evolve into different creatures as their level progresses.

Base Stats
~~~~~~~~~~

The base stats for these Pokémon can be obtained from thi general `base stats list`_. If you need to compute total damage done in battle or the current HP for a given Pokémon, you can use :ref:`NumPy array <arrays.ndarray>` objects.

.. _core series: https://bulbapedia.bulbagarden.net/wiki/Core_series
.. _base stats list: https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_base_stats_(Generation_I)

Usage
-----

You can create an instance of Bulbasaur called ``friend``, for example, by doing

.. code::
   
   >>> import pokedex
   >>> friend = pokedex.Bulbasaur()


