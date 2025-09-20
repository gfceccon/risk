from risk.game.base.map_base import MapBase
from risk.game.map.continent import Continent
from risk.game.map.territory import Territory
from risk.game.base.config import default_config


class World(MapBase):
    def __init__(self):
        super().__init__(config=default_config)
        self.continents = {
            "north_america": self._create_na("north_america"),
            "south_america": self._create_sa("south_america"),
            "europe": self._create_europe("europe"),
            "africa": self._create_africa("africa"),
            "asia": self._create_asia("asia"),
            "australia": self._create_oceania("australia"),
        }
        self._create_intercontinental_borders()

    def _create_na(self, short_name) -> Continent:
        # North America Territories
        self.alaska = Territory("Alaska", 1)
        self.alberta = Territory("Alberta", 2)
        self.central_america = Territory(
            "Central America", 3)
        self.eastern_us = Territory("Eastern United States", 4)
        self.greenland = Territory("Greenland", 5)
        self.northwest_territory = Territory(
            "Northwest Territory", 6)
        self.ontario = Territory("Ontario", 7)
        self.quebec = Territory("Quebec", 8)
        self.western_us = Territory("Western United States", 9)

        # North America Borders
        self.alaska.add_borders([self.northwest_territory, self.alberta])
        self.northwest_territory.add_borders(
            [self.alaska, self.alberta, self.ontario, self.greenland])
        self.greenland.add_borders(
            [self.northwest_territory, self.ontario, self.quebec])
        self.alberta.add_borders(
            [self.alaska, self.northwest_territory, self.ontario, self.western_us])
        self.ontario.add_borders(
            [self.greenland, self.northwest_territory, self.alberta, self.eastern_us, self.western_us, self.quebec])
        self.quebec.add_borders(
            [self.greenland, self.ontario, self.eastern_us])
        self.western_us.add_borders(
            [self.alberta, self.ontario, self.eastern_us, self.central_america])
        self.eastern_us.add_borders(
            [self.quebec, self.ontario, self.western_us, self.central_america])
        self.central_america.add_borders([self.western_us, self.eastern_us])

        # North America Continent
        north_america = Continent(
            "North America",
            [self.alaska, self.alberta, self.central_america, self.eastern_us,
             self.greenland, self.northwest_territory, self.ontario,
             self.quebec, self.western_us],
            bonus_troops=self.config.CONTINENT_BONUSES.get(short_name, 0))
        return north_america

    def _create_sa(self, short_name) -> Continent:
        # South America Territories
        self.argentina = argentina = Territory("Argentina", 1)
        self.brazil = brazil = Territory("Brazil", 2)
        self.venezuela = venezuela = Territory("Venezuela", 3)
        self.peru = peru = Territory("Peru", 4)

        # South America Borders
        self._create_borders([
            (venezuela, peru),
            (venezuela, brazil),
            (peru, brazil),
            (peru, argentina),
            (argentina, brazil),
        ])

        # South America Continent
        south_america = Continent(
            "South America", [argentina, brazil, venezuela, peru],
            bonus_troops=self.config.CONTINENT_BONUSES.get(short_name, 0))
        return south_america

    def _create_europe(self, short_name) -> Continent:
        # Europe Territories
        self.great_britain = great_britain = Territory("Great Britain", 1)
        self.iceland = iceland = Territory("Iceland", 2)
        self.northern_europe = northern_europe = Territory(
            "Northern Europe", 3)
        self.scandinavia = scandinavia = Territory("Scandinavia", 4)
        self.southern_europe = southern_europe = Territory(
            "Southern Europe", 5)
        self.ukraine = ukraine = Territory("Ukraine", 6)
        self.western_europe = western_europe = Territory("Western Europe", 7)

        # Europe Borders
        iceland.add_borders([scandinavia, great_britain])
        scandinavia.add_borders(
            [great_britain, iceland, ukraine, northern_europe])
        ukraine.add_borders([scandinavia, northern_europe, southern_europe])
        great_britain.add_borders(
            [iceland, scandinavia, northern_europe, western_europe])
        northern_europe.add_borders(
            [great_britain, scandinavia, ukraine, southern_europe, western_europe])
        western_europe.add_borders(
            [great_britain, northern_europe, southern_europe])
        southern_europe.add_borders(
            [northern_europe, ukraine, western_europe])

        # Europe Continent
        europe = Continent(
            "Europe", [great_britain, iceland, northern_europe, scandinavia,
                       southern_europe, ukraine, western_europe],
            bonus_troops=self.config.CONTINENT_BONUSES.get(short_name, 0))
        return europe

    def _create_africa(self, short_name) -> Continent:
        # Africa Territories
        self.congo = congo = Territory("Congo", 1)
        self.east_africa = east_africa = Territory("East Africa", 2)
        self.egypt = egypt = Territory("Egypt", 3)
        self.madagascar = madagascar = Territory("Madagascar", 4)
        self.north_africa = north_africa = Territory("North Africa", 5)
        self.south_africa = south_africa = Territory("South Africa", 6)

        # Africa Borders
        north_africa.add_borders([egypt, east_africa, congo])
        egypt.add_borders([north_africa, east_africa])
        east_africa.add_borders(
            [north_africa, egypt, congo, south_africa, madagascar])
        congo.add_borders([north_africa, east_africa, south_africa])
        south_africa.add_borders([congo, east_africa, madagascar])
        madagascar.add_borders([east_africa, south_africa])

        # Africa Continent
        africa = Continent(
            "Africa", [congo, east_africa, egypt,
                       madagascar, north_africa, south_africa],
            bonus_troops=self.config.CONTINENT_BONUSES.get(short_name, 0))
        return africa

    def _create_asia(self, short_name) -> Continent:
        # Asia Territories
        self.afghanistan = afghanistan = Territory("Afghanistan", 1)
        self.china = china = Territory("China", 2)
        self.india = india = Territory("India", 3)
        self.irkutsk = irkutsk = Territory("Irkutsk", 4)
        self.japan = japan = Territory("Japan", 5)
        self.kamchatka = kamchatka = Territory("Kamchatka", 6)
        self.middle_east = middle_east = Territory("Middle East", 7)
        self.mongolia = mongolia = Territory("Mongolia", 8)
        self.siam = siam = Territory("Siam", 9)
        self.siberia = siberia = Territory("Siberia", 10)
        self.ural = ural = Territory("Ural", 11)
        self.yakutsk = yakutsk = Territory("Yakutsk", 12)

        # Asia Borders
        afghanistan.add_borders([middle_east, ural, china, india])
        china.add_borders(
            [afghanistan, siberia, india, siam, mongolia, ural])
        india.add_borders([afghanistan, china, siam, middle_east])
        irkutsk.add_borders([mongolia, siberia, yakutsk, kamchatka])
        japan.add_borders([kamchatka, mongolia])
        kamchatka.add_borders([japan, mongolia, irkutsk, yakutsk])
        middle_east.add_borders([afghanistan, india])
        mongolia.add_borders([japan, kamchatka, irkutsk, china, siberia])
        siam.add_borders([india, china])
        siberia.add_borders([irkutsk, mongolia, china, ural, yakutsk])
        ural.add_borders([afghanistan, china, siberia])
        yakutsk.add_borders([siberia, irkutsk, kamchatka])

        # Asia Continent
        asia = Continent(
            "Asia", [afghanistan, china, india, irkutsk, japan,
                     kamchatka, middle_east, mongolia, siam, siberia, ural, yakutsk],
            bonus_troops=self.config.CONTINENT_BONUSES.get(short_name, 0))
        return asia

    def _create_oceania(self, short_name) -> Continent:
        # Australia Territories
        self.eastern_australia = eastern_australia = Territory(
            "Eastern Australia", 1)
        self.new_guinea = new_guinea = Territory("New Guinea", 2)
        self.indonesia = indonesia = Territory("Indonesia", 3)
        self.western_australia = western_australia = Territory(
            "Western Australia", 4)

        # Australia Borders
        indonesia.add_borders([new_guinea, western_australia])
        new_guinea.add_borders(
            [indonesia, eastern_australia, western_australia])
        western_australia.add_borders(
            [indonesia, eastern_australia, new_guinea])
        eastern_australia.add_borders([new_guinea, western_australia])

        # Australia Continent
        australia = Continent(
            "Australia", [western_australia, new_guinea,
                          indonesia, eastern_australia],
            bonus_troops=self.config.CONTINENT_BONUSES.get(short_name, 0))
        return australia

    def _create_intercontinental_borders(self):
        # Intercontinental Borders
        self._create_borders([
            # Africa <-> Asia
            (self.egypt, self.middle_east),
            (self.east_africa, self.middle_east),

            # Africa <-> Europe
            (self.north_africa, self.southern_europe),
            (self.north_africa, self.western_europe),
            (self.egypt, self.southern_europe),

            # North America <-> Asia
            (self.alaska, self.kamchatka),

            # North America <-> Europe
            (self.greenland, self.iceland),

            # South America <-> Africa
            (self.brazil, self.north_africa),

            # South America <-> North America
            (self.venezuela, self.central_america),

            # Europe <-> Asia
            (self.southern_europe, self.middle_east),
            (self.ukraine, self.middle_east),
            (self.ukraine, self.afghanistan),
            (self.ukraine, self.ural),

            # Oceania <-> Asia
            (self.indonesia, self.siam),
        ])
