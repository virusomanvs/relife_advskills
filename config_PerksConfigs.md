## Здесь хранятся настройки перков, которые могут быть увеличены в количестве, редактируя только конфиг.
## ActionContTimeConfigList - Позволяет вам с помощью перков влиять на скорость действий, которые построены на компоненте CAContinuousTime или CAContinuousRepeat

Узнать какой класс использует экшен, можно в коде.
![image](https://github.com/user-attachments/assets/21ebf8e4-3a57-47ec-97d8-7d47d62e4c55)

ВНИМАНИЕ! Если вы указали экшен, и перк не влияет на его время, или влияет но некорректно, то с этим ничего сделать нельзя! Этот экшен вы не сможете добавить в этот конфиг.

- **`ActionCreateGreenhouseGardenPlot`**: `string` Класснейм экшена скорость выполнения которую вы хотите изменить. Перки на скорость копания грядок, и скорость стройки, сделаны по этому принципу.
- **`perkID`**: `int` ID перка, при активации которого будет выполнятся эта настройка.
- **`setTime`**: `float` Время разделки. Если -1 то будет использоваться параметр ниже setCoef.
- **`setCoef`**: `float` Коэфицент на который будет умножено время экшена по умолчанию.

```json
    "ActionContTimeConfigList": {
        "ActionCreateGreenhouseGardenPlot": [
            {
                "perkID": 160,
                "setCoef": 0.8500000238418579,
                "setTime": 1
            },
            {
                "perkID": 161,
                "setCoef": 0.6000000238418579,
                "setTime": 1
            },
            {
                "perkID": 162,
                "setCoef": 0.3499999940395355,
                "setTime": 1
            }
        ],
        "ActionBuildPart": [
            {
                "perkID": 156,
                "setCoef": 0.8500000238418579,
                "setTime": 1
            },
            {
                "perkID": 155,
                "setCoef": 0.6499999761581421,
                "setTime": 1
            },
            {
                "perkID": 154,
                "setCoef": 0.4000000059604645,
                "setTime": 1
            }
        ],
    }
```
## SkinningPerkSettings - Настройка скорости разделки в зависимости от активированных перков. Перки должны быть в списке в порядке увеличения, так как они проверяются по списку с самого начала.
Вы можете создать множество перков в конфиге с перками и указать их здесь чтобы тонко влиять на скорость разделки.

- **`enableCoef`**: `bool` Включить чтобы перк влиял на разделку.
- **`perkID`**: `int` ID перка.
- **`setTime`**: `float` Время разделки. Если -1 то будет использоваться параметр ниже setCoef.
- **`setCoef`**: `float` Коэфицент на который будет умножено время из параметра DefaultSkinningTime в параметрах relife_AdvSkills.json.
  
```json
[
    "SkinningPerkSettings": [
        {
            "enableCoef": 1,
            "perkID": 157,
            "setTime": -1.0,
            "setCoef": 0.8500000238418579
        },
        {
            "enableCoef": 1,
            "perkID": 158,
            "setTime": -1.0,
            "setCoef": 0.6499999761581421
        },
        {
            "enableCoef": 1,
            "perkID": 159,
            "setTime": -1.0,
            "setCoef": 0.30000001192092898
        }
    ],
]
```

## EnduranceWeightPerkList - Настройка влияния веса на персонажа в зависимости от активированного перка.
Вы можете создать множество перков в конфиге с перками и указать их здесь чтобы тонко влиять на максимально переносимый вес.

- **`perkID`**: `int` ID перка.
- **`decreaseValue`**: `float` Коэфицент на который будет умножен максимально переносимый вес по умолчанию.
- К примеру персонаж может таскать 80 кг, decreaseValue = 0.5, то отсюда вытекает 80 кг * 0.5, получаем 40 и что весь вес внутри у него снизился в два раза.
  
```json
[
    "EnduranceWeightPerkList": [
        {
            "perkID": 173,
            "decreaseValue": 0.8999999761581421
        },
        {
            "perkID": 174,
            "decreaseValue": 0.800000011920929
        },
        {
            "perkID": 175,
            "decreaseValue": 0.699999988079071
        },
        {
            "perkID": 176,
            "decreaseValue": 0.6000000238418579
        },
        {
            "perkID": 177,
            "decreaseValue": 0.5
        }
    ]
]
```

## EnduranceDepletionPerkList - Настройка расхода стамины при выполнении действий (прыжки, удары, подтягивания) в зависимости от активированного перка.
Вы можете создать множество перков в конфиге с перками и указать их здесь.

- **`depletionEnduranceRegID`**: `int` ID для регистрации показаний в стамине ВНИМАНИЕ! Этот ID должен быть уникальным для EnduranceDepletionPerkList и EnduranceRecoveryPerkList и не пересекаться между друг другом. Ничего страшного не случится если они будут одинаковые или пересекутся, но будут срабатывать неверные значения.
- **`perkID`**: `int` ID перка.
- **`decreaseValue`**: `float` Коэфицент на который будет умножено требуемое кол-во стамины для выполнения действий по умолчанию.
- К примеру персонаж при беге за каждый шаг вы тратите 2% стамины. decreaseValue = 0.5, тогда 2 * 0.5, получаем 1, и теперь при активированом перке вы тратите 1% стамины.
  
```json
[
    "EnduranceDepletionPerkList": [
        {
            "depletionEnduranceRegID": 100,
            "perkID": 72,
            "decreaseValue": 0.8999999761581421
        },
        {
            "depletionEnduranceRegID": 101,
            "perkID": 73,
            "decreaseValue": 0.800000011920929
        },
        {
            "depletionEnduranceRegID": 102,
            "perkID": 74,
            "decreaseValue": 0.699999988079071
        },
        {
            "depletionEnduranceRegID": 103,
            "perkID": 75,
            "decreaseValue": 0.6000000238418579
        },
        {
            "depletionEnduranceRegID": 104,
            "perkID": 76,
            "decreaseValue": 0.5
        }
    ]
]
```


## EnduranceRecoveryPerkList - Настройка скорости восстановления стамины  в зависимости от активированного перка.
Вы можете создать множество перков в конфиге с перками и указать их здесь.

- **`depletionRecoveryRegID`**: `int` ID для регистрации показаний в стамине ВНИМАНИЕ! Этот ID должен быть уникальным для EnduranceDepletionPerkList и EnduranceRecoveryPerkList и не пересекаться между друг другом. Ничего страшного не случится если они будут одинаковые или пересекутся, но будут срабатывать неверные значения.
- **`perkID`**: `int` ID перка.
- **`decreaseValue`**: `float` Коэфицент на который будет умножена скорость восстановления стамины по умолчанию.
- К примеру при остановке стамина восстанавливается по 3% за секунду. decreaseValue = 2, тогда 3 * 2, получаем 6, и теперь при активированом перке стамина восстанавливается по 6% за секунду.
  
```json
[
    "EnduranceRecoveryPerkList": [
        {
            "depletionRecoveryRegID": 2000,
            "perkID": 77,
            "decreaseValue": 1.1
        },
        {
            "depletionRecoveryRegID": 2001,
            "perkID": 78,
            "decreaseValue": 1.2
        },
        {
            "depletionRecoveryRegID": 2002,
            "perkID": 79,
            "decreaseValue": 1.3
        },
        {
            "depletionRecoveryRegID": 2003,
            "perkID": 80,
            "decreaseValue": 1.4
        },
        {
            "depletionRecoveryRegID": 2004,
            "perkID": 81,
            "decreaseValue": 1.5
        }
    ]
]
```
