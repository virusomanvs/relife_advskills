## Настройка тряски оружия и влияние перков на него

- **`weaponClassname`**: `string` Класснейм оружия. DefaultWeapon если включен параметр enableDefaultWeaponRecord. Настройка будет распространяться на все оружия которое не в списке до DefaultWeapon
- **`defaultSpeed`**: `float` Настройки скорости по умолчанию.
- **`defaultWeight`**: `float` Настройки веса по умолчанию.
- **`perkCoefEnable`**: `bool` Включить влияние перков на тряску оружия.
- **`ignoredKindOfClassName`**: `array` Игнорировать эти классы для этой настройки
### perkCoefList
- **`enableCoef`**: `bool` Включить влияние перка на тряску оружия.
- **`perkID`**: `int` ID перка.
- **`speed`**: `float` Настройки скорости .
- **`weight`**: `float` Настройки веса.
```json
[
    {
        "weaponClassname": "DefaultWeapon",
        "defaultSpeed": 1.0,
        "defaultWeight": 2.0,
        "perkCoefEnable": 1,
        "ignoredKindOfClassName": [
            "IgnoredClass"
        ],
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
