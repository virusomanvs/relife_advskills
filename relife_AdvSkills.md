- **`enableLogsProfile`**: `bool` 0- 1. Вкл. или выкл. ведение логов которые сохраняются по пути **profiles\LogArchives\relife_AdvSKills**
- **`PointsName`**: `string` Название очков опыта. Используется в отображении меню и уведомлениях.
- **`SkillTypes`**: `TStringArray` массив со списком типов навыков. Только заглавные символы. Вывод в меню навыков выводится в том же порядке, как они указаны в конфиге.
- **`SkillTypesList`**: Настройки для определенного типа навыка.

## SkillTypesList
```json
"SkillTypesList": [
    {
         "skillType": "HUNTING",
         "skillTypeTitle": "#STR_RLF_SKILL_HUNTING",
         "skillTypeNotifyIcon": "relife_AdvSkills/gui/images/hunting.edds",
         "skillTypeMenuIcon": "relife_AdvSkills/gui/imagesets/top_menu/hunter.edds",
         "SkillStartedPoints": 0.0,
         "PointsDecreaseAfterDeath": 0.0
    }
]
```
- **`skillType`**: `string` Имя навыка, которое определено в параметре **SkillTypes**
- **`skillTypeTitle`**: `string`  Название навыка для отображения в меню и уведомлениях.
- **`skillTypeNotifyIcon`**: `string` Полный путь к иконке формата **.edds** для отображения в уведомлениях.
- **`skillTypeMenuIcon`**: `string` Полный путь к иконке формата **.edds** для отображения в меню.
- **`SkillStartedPoints`**: `float` Количество очков на старте игрока или при смерти (в соответствии с настройками смерти).
- **`PointsDecreaseAfterDeath`**:  `float` Значение от 0.0 до 1.0 на сколько в процентах снизится кол-во опыта данного типа при смерти.
  
### ==============================

- **`StartingPointsForAll`**:  `float` Стартовое значения опыта, если в параметрах типа навыка не указано начальное значение.
- **`PointsDecreaseAfterDeathForAll`**:  `float` Значение от 0.0 до 1.0 на сколько в процентах уменьшится опыт, если в параметрах типа навыка не указано начальное значение.

## Настройка расхода инструментов для перков по их экономии
```json
    "RepairKitPerkConfig": {
        "WeaponCleaningKitLvl1": 0.8999999761581421,
        "TireRepairKitLvl1": 0.8999999761581421,
        "TireRepairKitLvl2": 0.800000011920929,
        "TireRepairKitLvl3": 0.699999988079071,
        "ElectronicRepairKitLvl1": 0.8999999761581421,
        "ElectronicRepairKitLvl2": 0.8500000238418579,
        "ElectronicRepairKitLvl3": 0.699999988079071,
        "WeaponCleaningKitLvl3": 0.699999988079071,
        "LeatherSewingKitLvl1": 0.8999999761581421,
        "LeatherSewingKitLvl2": 0.8500000238418579,
        "LeatherSewingKitLvl3": 0.699999988079071,
        "EpoxyPuttyLvl1": 0.8999999761581421,
        "EpoxyPuttyLvl2": 0.8500000238418579,
        "EpoxyPuttyLvl3": 0.699999988079071,
        "WeaponCleaningKitLvl2": 0.800000011920929,
        "SewingKitCoefLvl1": 0.8999999761581421,
        "SewingKitCoefLvl2": 0.8500000238418579,
        "SewingKitCoefLvl3": 0.699999988079071
    },
```
## Настройка сброса перков и опыта в случае смерти игрока

- **`CLEARPERKAFTERDEATH`**: `bool` Включить/выключить сброс перков при смерти игрока
- **`ClearPlayerPerkUsingPenalty`**: `bool` Включить сброс перков при достижении определенного количества смертей
- **`PlayerCountDeathToPenalty`**: `int` Количество смертей при достижении которых сброятся перки
- **`clearPlayersPoints`**: `bool` Включить/выключить сброс опыта при смерти игрока
- **`enableDeacreasePoints`**: `bool` Включить/выключить сброс опыта на определенный процент указанный в типе навыка при смерти игрока
- **`clearPerkUsingChance`**: `bool` Сброс перков используя их внутренний шанс сброса **chanceToClear** 
- **`clearPerkUsingRandom`**: `bool` Сброс случайных перков в количестве указанном в **clearPerkUsingRandom_count**. Зависимые перки также будут сброшены по цепочке.
- **`clearPerkUsingRandom_count`**: `int` Количество сбрасываемых перков в случае если **clearPerkUsingRandom** равен `true`.
- 
```json
{
    "clearPerkUsingChance": 0,
    "clearPerkUsingRandom": 0,
    "clearPerkUsingRandom_count": 5,
    "IgnoreDeathPerkPlayers": [],
    "desc11": "[][][][_PERK ROTTEN EAT SETTINGS_][][][]",
    "BadEatPrepareTool": [
        "Sickle",
        "KukriKnife",
        "FangeKnife",
        "Hacksaw",
        "HandSaw",
        "KitchenKnife",
        "SteakKnife",
        "StoneKnife",
        "Cleaver",
        "CombatKnife",
        "Machete",
        "CrudeMachete",
        "OrientalMachete",
        "WoodAxe",
        "Hatchet",
        "FirefighterAxe",
        "Sword",
        "AK_Bayonet",
        "M9A1_Bayonet",
        "Mosin_Bayonet",
        "SKS_Bayonet",
        "BoneKnife"
    ],
    "BadEatPrepareMeat": [
        "CowSteakMeat",
        "SheepSteakMeat",
        "GoatSteakMeat",
        "MouflonSteakMeat",
        "BoarSteakMeat",
        "PigSteakMeat",
        "DeerSteakMeat",
        "WolfSteakMeat",
        "BearSteakMeat",
        "ChickenBreastMeat",
        "Kit_FoxSteakMeat",
        "Kit_RabbitLegMeat"
    ],
    "BadEatPrepareFish": [
        "CarpFilletMeat",
        "MackerelFilletMeat"
    ],
    "BadEatPrepareFruit": [
        "Apple",
        "Plum",
        "Pear",
        "SambucusBerry",
        "CaninaBerry",
        "Banana",
        "Orange",
        "Tomato",
        "GreenBellPepper",
        "Zucchini",
        "Pumpkin",
        "SlicedPumpkin",
        "Potato",
        "Kiwi",
        "MushroomBase"
    ],
    "desc8": "[][][][_PERK CATEYE SETTINGS_][][][]",
    "cateyesValue": [
        1.5,
        2.5,
        3.5,
        4.199999809265137
    ],
    "hour_start": 20,
    "min_start": 30,
    "hour_end": 4,
    "min_end": 30,
    "desc85": "[][][][_GARDENING SETTINGS_][][][]",
    "ShakeForFruitChance": 0.15000000596046449,
    "ShakeForFruitChancePerkPlusOne": 0.5,
    "desc10": "[][][][_ENDURANCE SETTINGS_][][][]",
    "Endurance_Per_Meter": 0.001500000013038516,
    "Endurance_Per_Full_Stamina_Melee": 0.05000000074505806,
    "Endurance_Per_Jump": 0.05000000074505806,
    "StaminaPercentDepletion": [
        0.8999999761581421,
        0.800000011920929,
        0.699999988079071,
        0.6000000238418579,
        0.5
    ],
    "StaminaPercentRecovery": [
        1.100000023841858,
        1.2000000476837159,
        1.2999999523162842,
        1.399999976158142,
        1.5
    ],
    "WeightPercentDecrease": [
        0.8999999761581421,
        0.800000011920929,
        0.699999988079071,
        0.6000000238418579,
        0.5
    ],
    "desc7": "[][][][_OTHER SETTINGS_][][][]",
    "ItemSkinningInPercent": 1,
    "WellMinWater": 1100,
    "WellMaxWater": 6500,
    "desc0": "[][][][_FISHING SETTINGS_][][][]",
    "BushBugSearchChance": 0.25,
    "BushBugSearchChancePerk": 0.4000000059604645,
    "ChanceToCatchDragonFly": 0.20000000298023225,
    "TreeDeadBugSearchChance": 0.44999998807907107,
    "TreeBugSearchChance": 0.25,
    "ChanceToCatchFrog": 0.07999999821186066,
    "FrogCatchQuantityMinMax": [
        0.6499999761581421,
        1.0
    ],
    "FrogCatchHealthMinMax": [
        0.6499999761581421,
        1.0
    ],
    "FishingRepeatChance": 0.3499999940395355,
    "FishingLostFishChance": 0.10000000149011612,
    "FishingHookLoss_Default": 0.5,
    "FishingHookLoss_OnHookPerk_1": 0.3499999940395355,
    "FishingHookLoss_OnHookPerk_2": 0.25,
    "FishingHookLoss_OnHookPerk_3": 0.10000000149011612,
    "FishingItemChance_Default": 0.3499999940395355,
    "FishchanceToCatchSea_Default": 0.10000000149011612,
    "FishchanceToCatchSea_OnFishingPerk_1": 0.20000000298023225,
    "FishchanceToCatchSea_OnFishingPerk_2": 0.30000001192092898,
    "FishchanceToCatchSea_OnFishingPerk_3": 0.4000000059604645,
    "FishchanceToCatchPond_Default": 0.10000000149011612,
    "FishchanceToCatchPond_OnFishingPerk_1": 0.20000000298023225,
    "FishchanceToCatchPond_OnFishingPerk_2": 0.30000001192092898,
    "FishchanceToCatchPond_OnFishingPerk_3": 0.4000000059604645,
    "FishingGarbageChance_Default": 0.800000011920929,
    "FishingGarbageChance_OnFishingLuckyPerk_1": 0.699999988079071,
    "FishingGarbageChance_OnFishingLuckyPerk_2": 0.6000000238418579,
    "FishingGarbageChance_OnFishingLuckyPerk_3": 0.5,
    "GoodFishingRodBonus": 0.10000000149011612,
    "IsNightBonus": 0.10000000149011612,
    "FishingRainBonus": 0.10000000149011612,
    "FishingModifier": 1.0,
    "GoodFishingClothesBonus": 0.05000000074505806,
    "FishingGoodRodTypes": [
        "FishingRod"
    ],
    "FishingGoodClothesTypes": [],
    "FishingSeaFishTypes": [
        {
            "itemFishID": 0,
            "className": "Mackerel",
            "chanceToCatch": 0.5,
            "skillPointsForCatch": 1.0,
            "randomQuantity": 0,
            "setQuantityPerc": 0.5,
            "quantRandMinPerc": 0.10000000149011612,
            "quantRandMaxPerc": 0.800000011920929,
            "perkCoefEnable": 1,
            "difficultCatch": [
                1.0,
                1.0
            ],
            "perkCoefList": [
                {
                    "enableCoef": 1,
                    "perkID": 38,
                    "randomQuantity": 0,
                    "setQuantityPerc": -1.0,
                    "quantRandMinPerc": 0.10000000149011612,
                    "quantRandMaxPerc": 0.800000011920929
                }
            ]
        }
    ],
    "FishingPondFishTypes": [
        {
            "itemFishID": 0,
            "className": "Carp",
            "chanceToCatch": 0.5,
            "skillPointsForCatch": 1.0,
            "randomQuantity": 0,
            "setQuantityPerc": 0.5,
            "quantRandMinPerc": 0.10000000149011612,
            "quantRandMaxPerc": 0.800000011920929,
            "perkCoefEnable": 1,
            "difficultCatch": [
                1.0,
                1.0
            ],
            "perkCoefList": []
        }
    ],
    "FishingGoodItemTypes": [],
    "FishingTrashItemTypes": [],
    "FishingGarbageItemsTypes": [],
    "FishingGoodItemsTypes": [],
    "PlantTypeList": [],
    "RecipePoint": [],
    "BlockCraftLists": [],
    "ActionFinnishPoint": {},
    "WeaponList": [],
    "ReadBookPoint": {},
    "EntityList": {},
    "SkillPerks": []
}
```
