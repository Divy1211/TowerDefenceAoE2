include "TowerDefenceDev\Constants.xs";

rule replaceTowers inactive {
    static int count = 0;
    count++;
    if(count%2 == 0) {
        return;
    }

    static int units = -1;
    for(player = 1; <= xsGetNumPlayers()) {
        units = xsGetPlayerUnitIds(player, cWallClass, units);
        for(i = 0; < xsArrayGetSize(units)) {
            int unitId = xsArrayGetInt(units, i);
            if(xsGetUnitBuildPoints(unitId) >= xsGetUnitAttribute(unitId, cTrainTime)) {
                xsCreateUnit(
                    mapWallToTower(xsGetUnitObjectId(unitId)),
                    player,
                    xsGetUnitPosition(unitId),
                    false,
                    false,
                    false
                );
                xsRemoveUnit(unitId);
            }
        }
    }
}