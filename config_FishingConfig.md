## Настройка рыбалки
## PackedBaitConfigList - Настройка параметров у прикормки.

- **`RLF_PackedBait`**: `string` Класснейм пакета прикормки.
- **`timeActive`**: `int` Класснейм пакета прикормки.
- **`decreaseItemChanceCoef`**: `float` Коэфицент на который умножится шанс поймать предмет вместо рыбы. То есть чем меньше значение тем больше шанс поймать рыбу,  а не предмет.

```json
{
    "PackedBaitConfigList": {
        "RLF_PackedBait": {
            "timeActive": 10,
            "decreaseItemChanceCoef": 0.5
        }
    },
}
```
## FishingPerkConfig - Список различных параметров и шансов связанных с рыбалкой.
- **`DigWormMoreChance`**: `float` Шанс выкопать дополнительного червя при активированном перке.
- **`FishchanceToCatchPond_Default`**: `float` Шанс поймать что либо в озере, без вкачаных перков.
- **`FishchanceToCatchSea_Default`**: `float` Шанс поймать что либо в море, без вкачаных перков.
- **`FishingDamageBait`**: `float` Урон крючку при рыбалке, без вкачаных перков.
- **`FishingDamageRod`**: `float` Урон удочке при рыбалке, без вкачаных перков.
- **`IsNightBonus_NoPerk`**: `float` Бонус при рыбалке ночью, без вкачаных перков.
- **`FishingRainBonus_NoPerk`**: `float` Бонус при рыбалке в дождь, без вкачаных перков.
- **`FishingGarbageChance_Default`**: `float` Шанс на поимку мусора, без вкачаных перков.
- **`FishSkinningToolDamageDefault`**: `float` Урон ножу при разделке рыбы.
- **`FishingHookLoss_Default`**: `float` Шанс потери крючка при рыбалке без вкачанных перков.
- **`FishingLostFishChance`**: `float` Шанс срыва рыбы.
- **`FishingRepeatChance`**: `float` Шанс прокрута действия рыбалки, для более длительной рыбалки и более тонкой настройки.
```json
{
    "FishingPerkConfig": {
        "DigWormMoreChance": 0.5,
        "FishchanceToCatchPond_Default": 0.10000000149011612,
        "FishingDamageBait": -5.0,
        "IsNightBonus_NoPerk": 0.05000000074505806,
        "FishingDamageRod": -5.0,
        "FishingGarbageChance_Default": 0.800000011920929,
        "FishchanceToCatchSea_Default": 0.10000000149011612,
        "FishSkinningToolDamageDefault": -10.0,
        "FishingHookLoss_Default": 0.5,
        "FishingItemChance_Default": 0.3499999940395355,
        "FishingRainBonus_NoPerk": 0.05000000074505806,
        "FishingLostFishChance": 0.10000000149011612,
        "FishingRepeatChance": 0.3499999940395355
    },
}
```
## FishingLuresTypes - Список блесен, которые будут игнорироваться в случае потере наживки. На них будет работать только урон по здоровью.
```json
{
    "FishingLuresTypes": [
        "Lure1",
        "lure2"
    ],
}
```
## FishingGoodClothesTypesSlots и FishingGoodClothesTypes - Здесь вы можете добавить вещи и слоты на персонаже в которых они будут одеты. И если в слоте будет вещь, то к общую шансу на поимку в рыбалке, прибавится и шанс из списка ниже.

- **`Headgear`**: `string` Слот на персонаже который будет проверяться.
- **`BoonieHat`**: `string` Класснейм вещи которая даст бонус к рыбалке.
- **`0.01`**: `float` Шанс если надет этот предмет. 
Шанс будет плюсоваться со всех шмоток,  а не только одной из списка.
```json
{
   "FishingGoodClothesTypesSlots": [
        "Headgear"
    ],
    "FishingGoodClothesTypes": {
        "BoonieHat": 0.01,
        "Item2": 0.01
    },
}
```
