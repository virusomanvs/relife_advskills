## Настройка тряски оружия и влияние перков на него

- **`weaponClassname`**: `string` Класснейм оружия. DefaultWeapon если включен параметр 
- **`itemHarvestName`**: `string` Класснейм выпадаемого плода при сборе.
- **`skillPointsForHarvest`**: `float` Количество опыта при сборе урожая.
- **`randomCount`**: `bool` Включить рандомное количество.
- **`setCount`**: `float`  Фиксированное количество в штуках если **randomCount** равно -1.
- **`countRandMin`**: `float` Рандом количество в штуках минимум.
- **`countRandMax`**: `float` Рандом количество в штуках максимум.
- **`randomQuantity`**: `bool` Включить рандомное количество в %.
- **`setQuantityPerc`**: `float` Фикс. количество в %.
- **`quantRandMinPerc`**: `float` Рандом количество в % минимум.
- **`quantRandMaxPerc`**: `float` Рандом количество в % максимум.
- **`perkCoefEnable`**: `bool` Включить влияние перков на сбор урожая.
  
```json
[
    {
        "weaponClassname": "DefaultWeapon",
        "defaultSpeed": 1.0,
        "defaultWeight": 2.0,
        "perkCoefEnable": 1,
        "perkCoefList": [
            {
                "enableCoef": 1,
                "perkID": 170,
                "speed": 1.2000000476837159,
                "weight": 1.7000000476837159
            },
            {
                "enableCoef": 1,
                "perkID": 171,
                "speed": 1.0,
                "weight": 1.2000000476837159
            },
            {
                "enableCoef": 1,
                "perkID": 172,
                "speed": 0.6000000238418579,
                "weight": 0.6000000238418579
            }
        ]
    }
]
```
