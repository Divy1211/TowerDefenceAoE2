extern const int cWatchTower = 79;
extern const int cWatchTowerWall = 2750;

extern const int cGuardTower = 234;
extern const int cGuardTowerWall = 2751;

extern const int cKeep = 235;
extern const int cKeepWall = 2752;

extern const int cBombardTower = 236;
extern const int cBombardTowerWall = 2753;

extern const int cFireTower = 190;
extern const int cFireTowerWall = 2754;

extern const int cSeaTower = 785;
extern const int cSeaTowerWall = 2755;

int mapWallToTower(int id = -1) {
    switch (id) {
        case cWatchTowerWall : {
            return (cWatchTower);
        }
        case cGuardTowerWall : {
            return (cGuardTower);
        }
        case cKeepWall : {
            return (cKeep);
        }
        case cBombardTowerWall : {
            return (cBombardTower);
        }
        case cFireTowerWall : {
            return (cFireTower);
        }
        case cSeaTowerWall : {
            return (cSeaTower);
        }
    }
    xsChatData("Error: Missing Wall to Tower ID");
    return (-1);
}
