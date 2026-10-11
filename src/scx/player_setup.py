from prelude import *

TOWN_CENTER_X1 = 621

def player_setup(scx: AoE2DEScenario):
    pm = scx.player_manager
    om = scx.option_manager
    tm = scx.trigger_manager
    um = scx.unit_manager

    pm.active_players = 8
    om.lock_teams = True
    om.allow_players_choose_teams = False

    pm.set_diplomacy_teams([1, 3, 5, 7], [2, 4, 6, 8])

    all_visible = tm.add_trigger("All Visible", execute_on_load = True)
    for player in players(scx):
        um.add_unit(player.player_id, UnitInfo.INVISIBLE_OBJECT_A.ID, 0, 0)
        all_visible.new_effect.modify_resource(
            quantity = 1,
            tribute_list = ResourceId.REVEAL_MAP,
            source_player = player.player_id,
            operation = Operation.SET,
        )

        player.civilization = Civilization.BRITONS
        player.lock_civ = True
        player.allied_victory = True

        player.starting_age = StartingAge.FEUDAL_AGE
        player.food = 200
        player.wood = 200
        player.gold = 100
        player.stone = 200
        player.population_cap = 200

        player.disabled_buildings = [
            BuildingInfo.HOUSE.ID,
            BuildingInfo.MILL.ID,
            BuildingInfo.MINING_CAMP.ID,
            BuildingInfo.LUMBER_CAMP.ID,
            BuildingInfo.DOCK.ID,
            BuildingInfo.FARM.ID,
            BuildingInfo.BLACKSMITH.ID,
            BuildingInfo.MARKET.ID,
            BuildingInfo.MONASTERY.ID,
            BuildingInfo.UNIVERSITY.ID,
            TOWN_CENTER_X1,
            BuildingInfo.WONDER.ID,

            BuildingInfo.BARRACKS.ID,
            BuildingInfo.ARCHERY_RANGE.ID,
            BuildingInfo.STABLE.ID,
            BuildingInfo.SIEGE_WORKSHOP.ID,
            BuildingInfo.OUTPOST.ID,
            BuildingInfo.PALISADE_WALL.ID,
            BuildingInfo.PALISADE_GATE.ID,
            BuildingInfo.WATCH_TOWER.ID,
            BuildingInfo.STONE_WALL.ID,
            BuildingInfo.GATE.ID,
            BuildingInfo.CASTLE.ID,
        ]
