## Начисление опыта при выполнении крафтов.

- **`className`**: `string` Класснейм крафта.
- **`skillPoints`**: `float` Количество начисляемого опыта.
- **`typeOfSkill`**: `string` Тип навыка на который будет начислен опыт.
- **`showNotify`**: `bool` Показывать уведомление о полученом опыте или изученом навыке.
  
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

