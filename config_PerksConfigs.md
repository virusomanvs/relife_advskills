## Здесь хранятся настройки перков, которые могут быть увеличены в количестве, редактируя только конфиг.

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

## Настройка скорости разделки в зависимости от активированных перков. Перки должны быть в списке в порядке увеличения, так как они проверяются по списку с самого начала.
Вы можете создать множество перков в конфиге с перками и указать их здесь чтобы тонко влиять на скорость разделки.

- **`enableCoef`**: `bool` Включить чтобы перк влиял на разделку.
- **`perkID`**: `int` ID перка.
- **`setTime`**: `float` Время разделки. Если -1 то будет использоваться параметр ниже setCoef.
- **`setCoef`**: `float` Коэфицент на который будет умножено время из параметра DefaultSkinningTime в параметрах relife_AdvSkills.json.
  
```json
[
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
        "setCoef": 0.05
    },
    {
        "enableCoef": 1,
        "perkID": 159,
        "setTime": -1.0,
        "setCoef": 0.30000001192092898
    }
]
```
