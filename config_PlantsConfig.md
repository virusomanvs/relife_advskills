## Настройка сбора урожая и влияние перков на него

- **`plantName`**: `string` Класснейм растения.
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
        "plantName": "Plant_Tomato",
        "itemHarvestName": "Tomato",
        "skillPointsForHarvest": 1.0,
        "randomCount": 1,
        "setCount": 1,
        "countRandMin": 1,
        "countRandMax": 1,
        "randomQuantity": 1,
        "setQuantityPerc": 0.5,
        "quantRandMinPerc": 0.10000000149011612,
        "quantRandMaxPerc": 0.5,
        "perkCoefEnable": 1,
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
