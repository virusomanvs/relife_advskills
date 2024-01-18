## Начисление опыта при разделке и убийстве животных или зараженных.

- **`Animal_SusDomesticus`**: `string` Класснейм моба.
- **`AnimalType`**: `string` Класснейм моба.
- **`KillPoints`**: `float` Количество начисляемого опыта при убийстве.
- **`SkinningPoints`**: `float` Количество начисляемого опыта при разделке.
- **`toolSkinDamageCoef`**: `float` Множитель урона инструменту разделки. 1.0 стандартный урон.
- **`typeOfSkill`**: `string` Тип навыка на который будет начислен опыт.
- **`showNotify`**: `bool` Показывать уведомление о полученом опыте.

### `ItemSkin` - настройка предметов разделки.

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

### `perkCoefList` - настройка перков для изменения количества и состояния выпадаемых предметов при разделке.
Перки в массиве должны распологаться в порядке увеличения, так как будет использоваться крайний активированный перк.

- **`enableCoef`**: `bool` Включить зависимость от текущего перка.
- **`perkID`**: `int` ID перка который будет влиять на разделку.

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
                        "coefQuantity": 1.5,
                        "setQuantity": -1.0,
                        "coefCount": -1.0,
                        "setCount": 2
                    },
                    {
                        "enableCoef": 1,
                        "perkID": 19,
                        "coefQuantity": 1.7000000476837159,
                        "setQuantity": -1.0,
                        "coefCount": -1.0,
                        "setCount": 3
                    },
                    {
                        "enableCoef": 1,
                        "perkID": 20,
                        "coefQuantity": 1.899999976158142,
                        "setQuantity": -1.0,
                        "coefCount": -1.0,
                        "setCount": 3
                    }
                ]
            },
            {
                "itemClassname": "Guts",
                "itemCount": 2,
                "haveQuantity": 1,
                "countQuantity": -1.0,
                "randomQuantity": 1,
                "QuantRandMin": 0.30000001192092898,
                "QuantRandMax": 0.8999999761581421,
                "toolCoefEnable": 0,
                "toolDamageCoef": 1.0,
                "addSalmonella": 1,
                "addBrainKuru": 0,
                "perkCoefEnable": 1,
                "perkCoefList": []
            },
            {
                "itemClassname": "Bone",
                "itemCount": 1,
                "haveQuantity": 1,
                "countQuantity": 1.0,
                "randomQuantity": 1,
                "QuantRandMin": 0.10000000149011612,
                "QuantRandMax": 0.5,
                "toolCoefEnable": 0,
                "toolDamageCoef": 1.0,
                "addSalmonella": 1,
                "addBrainKuru": 0,
                "perkCoefEnable": 1,
                "perkCoefList": []
            },
            {
                "itemClassname": "Lard",
                "itemCount": 0,
                "haveQuantity": 1,
                "countQuantity": -1.0,
                "randomQuantity": 1,
                "QuantRandMin": 0.30000001192092898,
                "QuantRandMax": 0.8999999761581421,
                "toolCoefEnable": 0,
                "toolDamageCoef": 1.0,
                "addSalmonella": 1,
                "addBrainKuru": 0,
                "perkCoefEnable": 1,
                "perkCoefList": [
                    {
                        "enableCoef": 1,
                        "perkID": 20,
                        "coefQuantity": -1.0,
                        "setQuantity": -1.0,
                        "coefCount": -1.0,
                        "setCount": 1
                    }
                ]
            },
            {
                "itemClassname": "PigPelt",
                "itemCount": 0,
                "haveQuantity": 0,
                "countQuantity": -1.0,
                "randomQuantity": 1,
                "QuantRandMin": 0.30000001192092898,
                "QuantRandMax": 0.800000011920929,
                "toolCoefEnable": 0,
                "toolDamageCoef": 1.0,
                "addSalmonella": 0,
                "addBrainKuru": 0,
                "perkCoefEnable": 1,
                "perkCoefList": [
                    {
                        "enableCoef": 1,
                        "perkID": 63,
                        "coefQuantity": -1.0,
                        "setQuantity": -1.0,
                        "coefCount": -1.0,
                        "setCount": 1
                    }
                ]
            }
        ]
    },
