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
- **`enableDefaultWeaponRecord`**:  `bool` Включить тряску оружия для всех видов используя параметр DefaultWeapon.

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
## Добавление опыта ОХОТНИКА игроку при стрельбе из оружия.

- **`AddPointToPlayerWeaponFire`**: `bool` Включить/выключить начисление при стрельбе.
- **`EnableDefaultPointToPlayerWeaponFire`**: `bool` Включить/выключить начисление опыта при стрельбе из все оружий, но если перед параметром DefaultWeapon будет запись с оружием, параметры будут браться из него.
- **`WeaponFireAddPoints`**: `string`,`float`  Класснейм оружия наследуемого Weapon_Base и начисляемый опыт за каждый патрон. Опыт будет начислен при достижении значения AddPointMax
- **`AddPointMax`**: `float` Каждый выстрел хранит и плюсует общее значение, при достижении этого значения будет начислено текущее количество опыта. Например: АКМ за каждый выстрел 0.25, AddPointMax = 1, значит при выстреле 4 раза будет начислен AddPointMax. Лишний опыт будет отсеян. Например, если получится при выстреле значение больше чем положено, будет все равно начислено AddPointMax.
- **`PointSkillType`**: `string` Навык, куда будет начислен опыт за стрельбу. HUNTING по умолчанию.
- **`ShowWeaponFireAddPointNotify`**: `bool` Показывать уведомление при начислении опыта.
  
`!ВНИМАНИЕ! Не проверено на слабых системах, возможно снижение серверного FPS так как много каких действий происходит за каждый выстрел.`

```json
{
    "AddPointToPlayerWeaponFire": 1,
    "EnableDefaultPointToPlayerWeaponFire": 0,
    "AddPointMax": 1.0,
    "WeaponFireAddPoints": {
        "Magnum": 1.0,
        "AKM": 0.25,
        "DefaultWeapon": 1.0
    },
    "ShowWeaponFireAddPointNotify": 1,
    "ItemSkinningInPercent": 1,
}
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
- **`IgnoreDeathPerkPlayers`**: `TStringArray` массив строк STEAMID для игнорирования сброса перков. При наличии STEAMID игрока, на него не будут распространяться никакие настройки сброса перков или опыта.
```json
{
     "IgnoreDeathPerkPlayers": [
        "steamid1",
        "steamid2"
     ],
}
```
## Настройка вырезания гнили в продуктах
- **`BadEatPrepareTool`**: `TStringArray` массив с класснеймом предметов с помощью которых можно будет вырезать гниль из продуктов.
```json
{
    "BadEatPrepareTool": [
        "Sickle",
        "KukriKnife",
        "FangeKnife",
        "Hacksaw",
    ]
}
```
- **`BadEatPrepareMeat`**: `TStringArray` массив с класснеймом мяса в котором можно будет вырезать гниль.
```json
{
    "BadEatPrepareMeat": [
       "CowSteakMeat",
        "SheepSteakMeat",
        "GoatSteakMeat",
        "MouflonSteakMeat",
        "BoarSteakMeat"
    ]
}
```
- **`BadEatPrepareFish`**: `TStringArray` массив с класснеймом рыбы в которой можно будет вырезать гниль.
```json
{
    "BadEatPrepareFish": [
        "CarpFilletMeat",
        "MackerelFilletMeat"
    ]
}
```
- **`BadEatPrepareFruit`**: `TStringArray` массив с класснеймом фруктов, овощей или грибов в которых можно будет вырезать гниль.
```json
{
    "BadEatPrepareFruit": [
         "Apple",
        "Plum",
        "Pear",
    ]
}
```
## Настройки для перка `Кошачьи глазки`
- **`cateyesValue`**: `TFloatArray` массив с настройками яркости для уровней перка `Кошачьи глазки`. Начиная с 0 по 4 уровень.
- **`enableCatEyePerk`**: `Bool` включить или выключить кошачьи глазки, при графических артефактах с другими модами.
```json
{
   "cateyesValue": [
        1.5,
        2.5,
        3.5,
        4.199999809265137
    ],
}
```
- **`hour_start`**: `int` Время в часах для активации перка.
- **`min_start`**: `int` Время в минутах для активации перка.
- **`hour_end`**: `int` Время в часах для деактивации перка.
- **`min_end`**: `int` Время в минутах для деактивации перка.

## Настройки для пасссивного начисления опыта Силы
# начисление опыта происходит когда сумма значения будет равна 1, максимальное значение может быть 1. То есть, если у вас стоит значение 0.2 за метр, вам нужно пройти 5 метров, тогда будет начислено 1 очко навыков.

- **`Endurance_Per_Meter`**: `float` Начисление опыта при пройденном растоянии за каждый метр.
- **`Endurance_Per_Full_Stamina_Melee`**: `float` Начисление опыта при ударах в рукопашном бою.
- **`Endurance_Per_Jump`**: `float` Начисление опыта за каждый прыжок.
## Настройки для перков по уменьшению расхода стамины, восстановлению и переносимому весу.

- **`StaminaPercentDepletion`**: `float`  Снижение требуемой выносливости для передвижения от 5 перка к 1.
```json
{
    "StaminaPercentDepletion": [
        0.8999999761581421,
        0.800000011920929,
        0.699999988079071,
        0.6000000238418579,
        0.5
    ],
}
```
- **`StaminaPercentRecovery`**: `float` Увеличение скорости восстановления выносливости от 5 перка к 1.
```json
{
    "StaminaPercentRecovery": [
        1.100000023841858,
        1.2000000476837159,
        1.2999999523162842,
        1.399999976158142,
        1.5
    ],
}
```
- **`WeightPercentDecrease`**: `float` Увеличение переносимого веса от 5 перка к 1.
```json
{
    "WeightPercentDecrease": [
        0.8999999761581421,
        0.800000011920929,
        0.699999988079071,
        0.6000000238418579,
        0.5
    ],
}
```

### ==============================

- **`ItemSkinningInPercent`**: `bool` Включает использование процентов при разделке животных, для настройки состояния мяса. Если выключено, то настройки состояния должны быть в фактическом количестве.
- **`FishingPerkConfig`**: `map` Хранит в себе настройки для перков по рыбалке, может быть изменен для своих целей.

Чтобы получить настройку из массива используйте GetAdvSkills().GetFishingPerkConfig(`string settingsName`);
```json
"FishingPerkConfig": {
        "DigWormMoreChance": 0.5,
        "FishchanceToCatchPond_OnFishingPerk_1": 0.20000000298023225,
        "FishchanceToCatchPond_OnFishingPerk_2": 0.30000001192092898,
        "FishchanceToCatchPond_OnFishingPerk_3": 0.4000000059604645,
        "IsNightBonus": 0.10000000149011612,
        "FishchanceToCatchPond_Default": 0.10000000149011612,
        "FishingDamageRodWithPerk": -2.0,
        "FishingDamageBait": -5.0,
        "GoodFishingClothesBonus": 0.5,
        "FishingHookLoss_Default": 0.5,
        "FishingItemChance_Default": 0.3499999940395355,
        "FishingLostFishChance": 0.10000000149011612,
        "FishingRainBonus": 0.10000000149011612,
        "FishingGarbageChance_OnFishingLuckyPerk_1": 0.699999988079071,
        "FishingGarbageChance_OnFishingLuckyPerk_2": 0.6000000238418579,
        "FishingGarbageChance_OnFishingLuckyPerk_3": 0.5,
        "FishchanceToCatchSea_OnFishingPerk_1": 0.20000000298023225,
        "FishchanceToCatchSea_OnFishingPerk_2": 0.30000001192092898,
        "FishchanceToCatchSea_OnFishingPerk_3": 0.4000000059604645,
        "FishingDamageRod": -5.0,
        "FishingHookLoss_OnHookPerk_3": 0.10000000149011612,
        "FishchanceToCatchSea_Default": 0.10000000149011612,
        "FishingHookLoss_OnHookPerk_1": 0.3499999940395355,
        "FishingHookLoss_OnHookPerk_2": 0.25,
        "FishingGarbageChance_Default": 0.800000011920929,
        "FishingDamageBaitWithPerk": -2.0,
        "GoodFishingRodBonus": 0.10000000149011612,
        "FishingRepeatChance": 0.3499999940395355
    }
```

## Настройки перков рыбалки
- **`DigWormMoreChance`**: `float` Шанс на выкапывание дополнительного червя при активированном перке.
- **`FishingRepeatChance`**: `float` Шанс прокрута круглешка действия. Чем больше, тем дольше будет крутится кругляш.
- **`FishingHookLoss_Default`**: `float` Шанс потери наживки без перка.
- **`FishingHookLoss_OnHookPerk_`**: `float` Шансы потери наживки при перках.
- **`FishchanceToCatchSea_Default`**: `float` Шанс поимки в море по умолчнанию.
- **`FishchanceToCatchSea_OnFishingPerk_`**: `float` Шанс поимки в море при перках.
- **`FishchanceToCatchPond_Default`**: `float` Шанс поимки в озере по умолчнанию.
- **`FishchanceToCatchPond_OnFishingPerk_`**: `float` Шанс поимки в озере при перках.
- **`FishingGarbageChance_Default`**: `float` Шанс поймать плохую вещь.
- **`FishingGarbageChance_OnFishingLuckyPerk_`**: `float` Шанс поймать плохую вещь при перках.

- FishingItemChance_Default это общий шанс на поимку вещи, сначала проверяется шанс чтобы поймать рыбу, если шанс на рыбу не сработал, проверяется шанс на поимку предмета, если он сработал проверяется шанс на поимку мусора FishingGarbageChance_Default ну и тут если да, то мусор если нет, то хорошие предметы.
- 
- **`GoodFishingRodBonus`**: `float` + процент ловле при удочках указанных в параметре **FishingGoodRodTypes**
- **`IsNightBonus`**: `float` Бонус к рыбалке ночью +10%
- **`FishingRainBonus`**: `float` Бонус к рыбалке в дождь +10%
- **`GoodFishingClothesBonus`**: `float` Бонус к рыбалке при ловле в определеной вещи на голове (панамка рыбака) указанной в **FishingGoodRodTypes**
- **`FishingGoodClothesTypes`**: `TStringArray` Список вещей на голове которые дают бонус к рыбалке.
```json
{
    "FishingGoodClothesTypes": [
        "BonieHat_ColorBase"
    ],
}
```
- **`FishingLuresTypes`**: `TStringArray` Список блесен которые не будут исчезать при ловле, на них будет работать только урон по самой блесне. Актуально для модов на рыбалку.
```json
{
    "FishingLuresTypes": [
        "LureClassName"
    ],
}
```
- **`FishingGarbageItemsTypes`**: `TStringArray` Список мусора который падает при рыбалке.
```json
{
    "FishingGarbageItemsTypes": [
        "Rag"
    ],
}
```
- **`FishingGoodItemsTypes`**: `TStringArray` Список полезных предметов которые падает при рыбалке.
```json
{
    "FishingGoodItemsTypes": [
        "Apple"
    ],
}
```
- **`FishingGoodRodTypes`**: `TStringArray` Список удочек которые дают бонус к рыбалке.
```json
{
    "FishingGoodRodTypes": [
        "FishingRod"
    ],
}
```
- **`FishignSeaFishTypes`**: Список морской рыбы
```json
    {
            "itemFishID": 0,
            "className": "Mackerel",
            "isNeededFishingRod": ["Rod1", "Rod2"],
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
```
- **`className`**: `string` classname рыбы
- **`isNeededFishingRod`**: `TSTringArray` список classname удочек для ловли. Если заполнено, то будет ловиться только с этих удочки, иначе шанс просто равен 0
- **`chanceToCatch`**: `float` Шанс на выбор из списка. То есть когда сработает шанс на поимку, будет выбираться шанс на ту рыбу которую вы поймали. Вы можете вносить рыбу в массив в любом порядке шансов, при выборе, скрипт перемешает всю рыбу в массиве и шансы будут выбираться более правильно. 0.5 это 50%.
- **`skillPointsForCatch`**: `float` Начисляемый опыт за поимку рыбы
- **`randomQuantity`**: `bool` Включить рандомное качество в процентах пойманной рыбы, если выключено будут использоваться настройки **setQuantityPerc** также в процентах от 0 до 1
- **`randomQuantity`**: `float` Количество пойманой рыбы в процентах от 0 до 1
- **`quantRandMinPerc`**: `float` Минимум рандомное число для **randomQuantity**
- **`quantRandMaxPerc`**: `float` Максимум рандомное число для **randomQuantity**
- **`perkCoefEnable`**: `bool` Включить зависимость от перков которые указаны в массиве **perkCoefList**

```json
{
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
```
- **`enableCoef`**: `bool` Включить отдельно
- **`perkID`**: `int` ID перка при активации которого будет учитываться эта настройка
- **`randomQuantity`**: `bool` Включить рандомное качество в процентах пойманной рыбы, если выключено будут использоваться настройки **setQuantityPerc** также в процентах от 0 до 1
- **`setQuantityPerc`**: `float` Количество пойманой рыбы в процентах от 0 до 1
- **`quantRandMinPerc`**: `float` Минимум рандомное число для **randomQuantity**
- **`quantRandMaxPerc`**: `float` Максимум рандомное число для **randomQuantity**
  
- **`FishignSeaFishTypes`**: Список рыбы из пруда. Настройки такие же как и у морской рыбы.

