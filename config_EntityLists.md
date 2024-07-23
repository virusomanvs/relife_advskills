## Начисление опыта при разделке и убийстве животных или зараженных, которые наследует ZombieBase или AnimalBase. Также влияние перков на разделку и список ножей которыми можно разделать моба.

Вы не можете сюда вписывать крафты или все что вздумается!

- **`Animal_CapreolusCapreolus`**: `string` Класснейм моба при убийстве или разделке которого будет применен этот конфиг.
- **`KillPoints`**: `float` Количество начисляемого опыта при убийстве.
- **`SkinningPoints`**: `float` Количество начисляемого опыта при разделке.
- **`toolSkinDamageCoef`**: `float` Множитель урона инструменту разделки. 1.0 стандартный урон. То есть при увеличении этого значения, инструмент которым вы разделываете будет полчать повышеный урон. **ВанильныйУрон * toolSkinDamageCoef.**
- **`typeOfSkillKill`**: `string` Тип навыка на который будет начислен опыт при убийстве.
- **`typeOfSkillSkinning`**: `string` Тип навыка на который будет начислен опыт при разделке.
- **`showNotify`**: `bool` Показывать уведомление о полученом опыте при убийстве.
- **`modeKnifesAllow`**: `bool` Режим проверки ножей для разделки. 0 - Разрешено разделать только ножами из списка knifesList или knifesListID. 1 - Запрещена разделка ножами из списка knifesList или knifesListID.
- **`allowknifesListKindOf`**: `bool` Включить наследуемость класснйемов при проверке ножей. То есть, при значении 1, будут проверяться все ножи из списка knifesList, включая те, которые наследуют их классы. Иначе будет проверяться именно этот нож. 
- **`knifesList`**: `TStringArray` Массив класснеймов ножей, если есть записи, то животное можно будет разделать или нет, только ножами из этого списка. Если заполнено, то knifesListID будет проигнорировано. 
- **`knifesListID`**: `TIntArray` Массив ID списка ножей, если есть записи, то животное можно будет разделать или нет, только ножами из этого списка.

### `ItemSkin` - настройка предметов которые выпадут при разделке моба.

- **`itemClassname`**: `string` Класснейм предмета.
- **`itemCount`**: `int` Количество предмета в штуках, не в %.
- **`haveQuantity`**: `bool` Если у предмета есть % или внутренне количество.
- **`countQuantity`**: `float` Количество предмета в % или фактическом состоянии.
- **`randomQuantity`**: `bool` Включить случайно количество предмета в % или фактическом состоянии.
- **`QuantRandMin`**: `float` Минимальное значение случайного количества.
- **`QuantRandMax`**: `float` Максимальное значение случайного количества.
- **`toolCoefEnable`**: `bool` Включить зависимость состояния от состояния инструмента разделки.
- **`toolDamageCoef`**: `float` Множитель состояния предмета от состояния инструмента.
- **`addSalmonella`**: `bool` Добавить агенты сальмонеллы предмету.
- **`addBrainKuru`**: `bool` Добавить агенты куру предмету.
- **`perkCoefEnable`**: `bool` Включить зависимость состояния и количества от активированных перков в массиве **perkCoefList**.

```json
{
    "Animal_CapreolusCapreolus": {
        "KillPoints": 5.0,
        "SkinningPoints": 5.0,
        "toolSkinDamageCoef": 1.0,
        "typeOfSkillKill": "HUNTING",
        "typeOfSkillSkinning": "HUNTING",
        "showNotify": 1,
        "modeKnifesAllow": 0,
        "allowknifesListKindOf": 1,
        "knifesList": ["knife1", "knife2"],
        "knifesListID": [],
        "ItemSkin": [
            {
                "itemClassname": "MeatClassName",
                "setCount": [1,-1,-1],
                "chanceToSpawn": 1.0,
                "haveQuantity": 1,
                "setQuantity": [1,-1,-1],
                "setHealth": [1,-1,-1],
                "toolHealthCoefEnable": 0,
                "coefHealthMinMaxValue": [0.5,1.0],
                "toolQuantityCoefEnable": 0,
                "coefQuantityMinMaxValue": [0.5,1.0],
                "toolDamageCoef": 1.0,
                "addAgents": [
                    4
                ],
                "perkCoefEnable": 1,
                "perkCoefList": [
                    {
                        "enableCoef": 1,
                        "perkID": 89,
                        "chanceToSpawn": 1.0,
                        "setCount": [1,-1,-1],
                        "haveQuantity": 1,
                        "setQuantity": [1,-1,-1],
                        "setHealth": [1,-1,-1],
                        "toolHealthCoefEnable": 0,
                        "coefHealthMinMaxValue": [0.5,1.0],
                        "toolQuantityCoefEnable": 0,
                        "coefQuantityMinMaxValue": [0.5,1.0],
                        "addAgents": [
                            4
                        ]
                    },
                    {
                        "enableCoef": 1,
                        "perkID": 90,
                        "chanceToSpawn": 1.0,
                        "setCount": [1,-1,-1],
                        "haveQuantity": 1,
                        "setQuantity": [1,-1,-1],
                        "setHealth": [1,-1,-1],
                        "toolHealthCoefEnable": 0,
                        "coefHealthMinMaxValue": [0.5,1.0],
                        "toolQuantityCoefEnable": 0,
                        "coefQuantityMinMaxValue": [0.5,1.0],
                        "addAgents": [
                            4
                        ]
                    }
                ]
            }
        ]
    }
}
```

### `perkCoefList` - настройка перков для изменения количества и состояния выпадаемых предметов при разделке.
Перки в массиве должны распологаться в порядке увеличения, так как будет использоваться крайний активированный перк. Значение -1.0 отключает настройку в тех пунктах которые имеют значение типа `float`.

- **`enableCoef`**: `bool` Включить зависимость от текущего перка.
- **`perkID`**: `int` ID перка который будет влиять на разделку.
- **`coefQuantity`**: `float` Множитель увеличения количества в % от значения по умолчанию.
- **`setQuantity`**: `float` Фиксированное количество в % если **coefQuantity** равно -1.
- **`coefCount`**: `float` Множитель увеличения количества в штуках от значения по умолчанию.
- **`setCount`**: `float`  Фиксированное количество в штуках если **coefCount** равно -1.

```json
"perkCoefList": [
    {
      "enableCoef": 1,
      "perkID": 17,
      "coefQuantity": 1.2000000476837159,
      "setQuantity": -1.0,
      "coefCount": -1.0,
      "setCount": 2
    },
    {
      "enableCoef": 1,
      "perkID": 18,
      "coefQuantity": 1.2000000476837159,
      "setQuantity": -1.0,
      "coefCount": -1.0,
      "setCount": 3
    }
]
```
