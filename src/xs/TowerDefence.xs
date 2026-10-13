// include "TowerDefenceDev\Constants.xs";
include "TowerDefenceDev\Utils.xs";

include "TowerDefenceDev\Effects.xs";

void resetDamageClass(int objectId = -1, int type_ = -1) {
    for(class_ = cDamageClassInfantry; < cNumDamageClasses) {
        xsEffectAmount(cSetAttribute, objectId, cRemoveArmorType + type_ - cArmor, class_);
    }
}

void resetArmors(int objectId = -1) {
    resetDamageClass(objectId, cArmor);
}

void resetAttacks(int objectId = -1) {
    resetDamageClass(objectId, cAttack);
}

void main() {
    xsChatData("test");
}
