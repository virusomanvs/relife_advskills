## Настройка сбора урожая и влияние перков на него

## Для перехода конфига с версии которая была в августе, на версию которая вышла с релизом 1.26 используйте конвертер конфига. https://virusomanvs.github.io/plant


- **`plantName`**: `string` Класснейм растения.
- **`itemHarvestName`**: `string` Класснейм выпадаемого плода при сборе.
- **`skillPointsForHarvest`**: `float` Количество опыта при сборе урожая.
- **`skillTypeForHarvest`**: `string` Тип навыка на который начислится опыт.
- **`showNotifyAddPoints`**: `bool` Включить уведомление о начисление опыта.
- **`chanceToSpawn`**: `float`  Шанс спавна для каждого плода от 0 до 1.
- **`setCount`**: `float` Кол-во плодов в спавне. Первый параметр - фиксированное кол-во, если -1 будет использоваться рандомное кол-во в диапазоне от второго параметра до третьего.
- **`setQuantity`**: `float` Кол-во плода в %. Первый параметр - фиксированное кол-во в %, если -1 будет использоваться рандомное кол-во в % в диапазоне от второго параметра до третьего. От 0 до 1
- **`setQuantity`**: `float` Здоровье плода. Первый параметр - фиксированное здоровье, если -1 будет использоваться рандомное здоровье в диапазоне от второго параметра до третьего. От 0 до 1
- **`randomQuantity`**: `bool` Включить рандомное количество в %.
- **`setQuantityPerc`**: `float` Фикс. количество в %.
- **`quantRandMinPerc`**: `float` Рандом количество в % минимум.
- **`quantRandMaxPerc`**: `float` Рандом количество в % максимум.
- **`perkCoefEnable`**: `bool` Включить влияние перков на сбор урожая.
  
```json
[
    {
        "plantName": "Plant_Tomato",
        "itemHarvestName": "Tomato",
        "skillPointsForHarvest": 1,
        "skillTypeForHarvest": "GARDENING",
        "showNotifyAddPoints": 1,
        "chanceToSpawn": 1,
        "setCount": [
            1,
            -1,
            -1
        ],
        "setQuantity": [
            -1,
            0.1,
            0.5
        ],
        "setHealth": [
            1,
            -1,
            -1
        ],
        "perkCoefEnable": 1,
        "perkCoefList": [
            {
                "enableCoef": 1,
                "perkID": 30,
                "chanceToSpawn": 1,
                "setCount": [
                    -1,
                    1,
                    2
                ],
                "setQuantity": [
                    -1,
                    0.5,
                    0.7
                ],
                "setHealth": [
                    1,
                    -1,
                    -1
                ]
            },
            {
                "enableCoef": 1,
                "perkID": 31,
                "chanceToSpawn": 1,
                "setCount": [
                    -1,
                    1,
                    2
                ],
                "setQuantity": [
                    -1,
                    0.7,
                    0.8
                ],
                "setHealth": [
                    1,
                    -1,
                    -1
                ]
            },
            {
                "enableCoef": 1,
                "perkID": 32,
                "chanceToSpawn": 1,
                "setCount": [
                    -1,
                    2,
                    3
                ],
                "setQuantity": [
                    -1,
                    0.9,
                    1
                ],
                "setHealth": [
                    1,
                    -1,
                    -1
                ]
            }
        ]
    }
]
```

### `perkCoefList` - настройка перков для изменения количества и состояния выпадаемых предметов при сборе урожая.
Перки в массиве должны распологаться в порядке увеличения, так как будет использоваться крайний активированный перк. Значение -1.0 отключает настройку в тех пунктах которые имеют значение типа `float`.

- **`enableCoef`**: `bool` Включить зависимость от текущего перка.
- **`perkID`**: `int` ID перка который будет влиять на разделку.
- **`randomCount`**: `bool` Включить рандомное количество.
- **`setCount`**: `float`  Фиксированное количество в штуках если **randomCount** равно -1.
- **`countRandMin`**: `float` Рандом количество в штуках минимум.
- **`countRandMax`**: `float` Рандом количество в штуках максимум.
- **`randomQuantity`**: `bool` Включить рандомное количество в %.
- **`setQuantityPerc`**: `float` Фикс. количество в %.
- **`quantRandMinPerc`**: `float` Рандом количество в % минимум.
- **`quantRandMaxPerc`**: `float` Рандом количество в % максимум.


```json
"perkCoefList": [
  {
    "enableCoef": 1,
    "perkID": 30,
    "randomCount": 1,
    "setCount": 1,
    "countRandMin": 1,
    "countRandMax": 2,
    "randomQuantity": 1,
    "setQuantityPerc": 0.5,
    "quantRandMinPerc": 0.5,
    "quantRandMaxPerc": 0.699999988079071
  },
]
```
