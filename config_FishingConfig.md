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
- **`IsNightBonus_NoPerk`**: `float` Бонус при рыбалке ночью, без вкачаных перков.
- **`FishingRainBonus_NoPerk`**: `float` Бонус при рыбалке в дождь, без вкачаных перков.
```json
{
    "FishingPerkConfig": {
        "DigWormMoreChance": 0.5,
        "FishchanceToCatchPond_Default": 0.10000000149011612,
        "FishingDamageBait": -5.0,
        "GoodFishingClothesBonus": 0.009999999776482582,
        "IsNightBonus_NoPerk": 0.05000000074505806,
        "FishingDamageRod": -5.0,
        "FishingGarbageChance_Default": 0.800000011920929,
        "FishchanceToCatchSea_Default": 0.10000000149011612,
        "FishSkinningToolDamageDefault": -10.0,
        "FishingHookLoss_Default": 0.5,
        "FishingItemChance_Default": 0.3499999940395355,
        "FishingRainBonus_NoPerk": 0.05000000074505806,
        "GoodFishingRodBonus": 0.10000000149011612,
        "FishingLostFishChance": 0.10000000149011612,
        "FishingRepeatChance": 0.3499999940395355
    },
}
```
