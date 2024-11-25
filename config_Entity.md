## Для добавления нового животного или зараженного в конфиг, необходимо просто создать в папке profile/RELIFE/PERKS_CONFIG/ENTITY (или скопировать с примера) файл JSON с параметрами ниже, и назвать его именем класса этого животного или зараженного. Также если есть конфиг для животного или зараженного, которого нет в игре (старый мод, неверно указали класснейм), то конфиг не будет загружен, для экономии ресурсов. Об этом вы можете узнать в логах relife_AdvSkills.log

![image](https://github.com/user-attachments/assets/8f878fe8-4939-48bd-bd40-87f033cd2891)

## Начисление опыта при разделке и убийстве животных или зараженных, которые наследует ZombieBase или AnimalBase. Также влияние перков на разделку и список ножей которыми можно разделать моба.

Вы не можете сюда вписывать крафты или все что вздумается! Вы можете настроить этот конфиг с нуля (не рекомендую) или же скачать уже готовый конфиг (GDrive) с ванильными животными, чтобы добавить свои по их приимеру.

ДЛЯ КОНВЕРТАЦИИ СТАРОГО КОНФИГА В НОВЫЙ ФОРМАТ, ВОСПОЛЬЗУЙТЕСЬ СКРИПТОМ PYTHON В ПАПКЕ CONVERTJSON ИЛИ ПЕРЕЙДИТЕ ПО АДРЕСУ https://virusomanvs.github.io/

- **`Animal_CapreolusCapreolus`**: `string` Класснейм моба при убийстве или разделке которого будет применен этот конфиг.
- **`KillPoints`**: `float` Количество начисляемого опыта при убийстве.
- **`SkinningPoints`**: `float` Количество начисляемого опыта при разделке.
- **`toolSkinDamageCoef`**: `float` Множитель урона инструменту разделки. 1.0 стандартный урон. То есть при увеличении этого значения, инструмент которым вы разделываете будет полчать повышеный урон. **ВанильныйУрон * toolSkinDamageCoef.**
- **`typeOfSkillKill`**: `string` Тип навыка на который будет начислен опыт при убийстве.
- **`typeOfSkillSkinning`**: `string` Тип навыка на который будет начислен опыт при разделке.
- **`onlyKillerAddPointsFromSkinning`**: `bool` Если включить то опыт при разделке получит только тот кто убил.
- **`showNotify`**: `bool` Показывать уведомление о полученом опыте при убийстве.
- **`modeKnifesAllow`**: `bool` Режим проверки ножей для разделки. 0 - Разрешено разделать только ножами из списка knifesList или knifesListID. 1 - Запрещена разделка ножами из списка knifesList или knifesListID.
- **`allowknifesListKindOf`**: `bool` Включить наследуемость класснйемов при проверке ножей. То есть, при значении 1, будут проверяться все ножи из списка knifesList, включая те, которые наследуют их классы. Иначе будет проверяться именно этот нож. 
- **`knifesList`**: `TStringArray` Массив класснеймов ножей, если есть записи, то животное можно будет разделать или нет, только ножами из этого списка. Если заполнено, то knifesListID будет проигнорировано. 
- **`knifesListID`**: `TIntArray` Массив ID списка ножей, если есть записи, то животное можно будет разделать или нет, только ножами из этого списка. Хранятся айди в отдельном конфиге config_KnifesListIDConfig.json

### `ItemSkin` - настройка предметов которые выпадут при разделке моба и влияние перков на параметр предмета.

- **`itemClassname`**: `string` Класснейм предмета.
- **`setCount[3]`**: `int` Количество предмета в штуках, которое выпадет при разделке. Первое число это фиксированное кол-во (1 штука, 3 штуки и т.д). Если вы хотите чтобы каждый раз случайно выпадало разное кол-во, укажите первое значение -1, а второе это минимальное случайное число, второе максимальное случайное число.
Пример. "setCount": [-1,1,3], При таких настройках предмета будет падать от 1 до 3 штук.
- **`chanceToSpawn`**: `float` Шанс спавна предмета от 0 до 1. Будет работать на каждый предмет из setCount. К примеру если у вас стоит выпадать по 3 куска мяса, то шанс будет срабатывать на каждый кусок.
- **`toolsSpawnList`**: `string` Массив с класснеймом ножей при разделке которомы будет спавнится предмет. Если пусто любой нож.
- **`haveQuantity`**: `bool` Если у предмета есть % или внутренне количество.
- **`setQuantity[3]`**: `float` Количество предмета в % от 0 до 1, которое выпадет при разделке. Первое число это фиксированное кол-во (100%, 50% и т.д). Если вы хотите чтобы каждый раз случайно выпадало разное кол-во в %, укажите первое значение -1, а второе это минимальное случайное число в %, второе максимальное случайное число в %. 
Пример. "setQuantity": [-1,0.5,1], При таких настройках предмета будет падать в % от 50 до 100%.
- **`setHealth[3]`**: `float` Здоровье предмета в % от 0 до 1, которое выпадет при разделке. Первое число это фиксированное здоровье (100%, 50% и т.д). Если вы хотите чтобы каждый раз случайно выпадало разное здоровье у предмета в %, укажите первое значение -1, а второе это минимальное случайное число в %, второе максимальное случайное число в %. 
Пример. "setHealth": [-1,0.5,1], При таких настройках предмета будет падать его здоровье в % от 50 до 100%.
- **`toolCoefEnable`**: `bool` Включить зависимость состояния от состояния инструмента разделки.
- **`toolDamageCoef`**: `float` Множитель состояния предмета от состояния инструмента.
- **`addSalmonella`**: `bool` Добавить агенты сальмонеллы предмету.
- **`addBrainKuru`**: `bool` Добавить агенты куру предмету.
- **`perkCoefEnable`**: `bool` Включить зависимость состояния и количества от активированных перков в массиве **perkCoefList**.
- **`toolHealthCoefEnable`**: `bool` Включить зависимость здоровья выпадаемого предмета от состояния ножа которым разделываете.
- **`coefHealthMinMaxValue[2]`**: `float` Диапазон коэфицента в котором будет варьироваться здоровье предмета в зависимости от ножа. То есть итоговое здоровье будет умножено на полученое значение.
Пример. "coefHealthMinMaxValue": [0.5,1.0], - при таких настройках, здоровье предмета будет помножено на 0.5 если нож почти уничтожен, и практически не изменится если нож нетронут.
- **`toolQuantityCoefEnable`**: `bool` Включить зависимость кол-ва в % выпадаемого предмета от состояния ножа которым разделываете.
- **`coefQuantityMinMaxValue[2]`**: `float` Диапазон коэфицента в котором будет варьироваться кол-во в % предмета в зависимости от ножа. То есть итоговое кол-во в % будет умножено на полученое значение.
Пример. "coefQuantityMinMaxValue": [0.5,1.0], - при таких настройках, кол-во в % предмета будет помножено на 0.5 если нож почти уничтожен, и практически не изменится если нож нетронут.
- **`toolDamageCoef`**: `float` Дополнительный множитель урона ножу при выпадении предмета.   
- **`addAgents`**: `TIntArray` Массив с ID агентами которые будут накинуты на предмет. По умолчанию на все кидается сальмонелла. ID ванильных агентов ниже
- **`perkCoefEnable`**: `bool` Включить зависимость состояния и количества от активированных перков в массиве **perkCoefList**.
```C#
enum eAgents
{
	//agent list
	CHOLERA 		= 1;
	INFLUENZA 		= 2;
	SALMONELLA		= 4;
	BRAIN 			= 8;
	FOOD_POISON		= 16;
	CHEMICAL_POISON		= 32;
	WOUND_AGENT		= 64;
	NERVE_AGENT		= 128;
}
```

### `perkCoefList` - настройка перков для изменения количества и состояния выпадаемых предметов при разделке.
Перки в массиве должны распологаться в порядке увеличения, так как будет использоваться крайний активированный перк. 
			
- **`enableCoef`**: `bool` Включить зависимость от текущего перка.
- **`perkID`**: `int` ID перка который будет влиять на разделку.

Остальные параметры точно такие же как и без перка. Только при активации перк перепишет их на свои значения.

```json
{
    "KillPoints": 3.0,
    "SkinningPoints": 2.0,
    "toolSkinDamageCoef": 1.0,
    "typeOfSkillKill": "HUNTING",
    "typeOfSkillSkinning": "HUNTING",
    "showNotify": 0,
    "modeKnifesAllow": 0,
    "allowknifesListKindOf": 1,
    "knifesList": [],
    "knifesListID": [],
    "ItemSkin": [
        {
            "itemClassname": "CowSteakMeat",
            "setCount": [
                1,
                -1,
                -1
            ],
            "chanceToSpawn": 1.0,
            "toolsSpawnList": {},
            "haveQuantity": 1,
            "setQuantity": [
                -1.0,
                0.30000001192092898,
                0.4000000059604645
            ],
            "setHealth": [
                1.0,
                -1.0,
                -1.0
            ],
            "toolHealthCoefEnable": 1,
            "coefHealthMinMaxValue": [
                0.5,
                1.0
            ],
            "toolQuantityCoefEnable": 0,
            "coefQuantityMinMaxValue": [
                0.5,
                1.0
            ],
            "toolDamageCoef": 1.0,
            "addAgents": [
                4
            ],
            "perkCoefEnable": 1,
            "perkCoefList": [
                {
                    "enableCoef": 1,
                    "perkID": 17,
                    "chanceToSpawn": 1.0,
                    "toolsSpawnList": {},
                    "setCount": [
                        2,
                        -1,
                        -1
                    ],
                    "haveQuantity": 1,
                    "setQuantity": [
                        -1.0,
                        0.5,
                        0.6000000238418579
                    ],
                    "setHealth": [
                        1.0,
                        -1.0,
                        -1.0
                    ],
                    "toolHealthCoefEnable": 1,
                    "coefHealthMinMaxValue": [
                        0.5,
                        1.0
                    ],
                    "toolQuantityCoefEnable": 0,
                    "coefQuantityMinMaxValue": [
                        0.5,
                        1.0
                    ],
                    "addAgents": [
                        4
                    ]
                },
                {
                    "enableCoef": 1,
                    "perkID": 18,
                    "chanceToSpawn": 1.0,
                    "toolsSpawnList": {},
                    "setCount": [
                        2,
                        -1,
                        -1
                    ],
                    "haveQuantity": 1,
                    "setQuantity": [
                        -1.0,
                        0.6000000238418579,
                        0.699999988079071
                    ],
                    "setHealth": [
                        1.0,
                        -1.0,
                        -1.0
                    ],
                    "toolHealthCoefEnable": 1,
                    "coefHealthMinMaxValue": [
                        0.5,
                        1.0
                    ],
                    "toolQuantityCoefEnable": 0,
                    "coefQuantityMinMaxValue": [
                        0.5,
                        1.0
                    ],
                    "addAgents": [
                        4
                    ]
                },
                {
                    "enableCoef": 1,
                    "perkID": 19,
                    "chanceToSpawn": 1.0,
                    "toolsSpawnList": {},
                    "setCount": [
                        3,
                        -1,
                        -1
                    ],
                    "haveQuantity": 1,
                    "setQuantity": [
                        -1.0,
                        0.699999988079071,
                        0.8500000238418579
                    ],
                    "setHealth": [
                        1.0,
                        -1.0,
                        -1.0
                    ],
                    "toolHealthCoefEnable": 1,
                    "coefHealthMinMaxValue": [
                        0.5,
                        1.0
                    ],
                    "toolQuantityCoefEnable": 0,
                    "coefQuantityMinMaxValue": [
                        0.5,
                        1.0
                    ],
                    "addAgents": [
                        4
                    ]
                },
                {
                    "enableCoef": 1,
                    "perkID": 20,
                    "chanceToSpawn": 1.0,
                    "toolsSpawnList": {},
                    "setCount": [
                        3,
                        -1,
                        -1
                    ],
                    "haveQuantity": 1,
                    "setQuantity": [
                        -1.0,
                        0.8500000238418579,
                        1.0
                    ],
                    "setHealth": [
                        1.0,
                        -1.0,
                        -1.0
                    ],
                    "toolHealthCoefEnable": 1,
                    "coefHealthMinMaxValue": [
                        0.5,
                        1.0
                    ],
                    "toolQuantityCoefEnable": 0,
                    "coefQuantityMinMaxValue": [
                        0.5,
                        1.0
                    ],
                    "addAgents": [
                        4
                    ]
                }
            ]
        },
        {
            "itemClassname": "Guts",
            "setCount": [
                2,
                -1,
                -1
            ],
            "chanceToSpawn": 1.0,
            "toolsSpawnList": {},
            "haveQuantity": 1,
            "setQuantity": [
                -1.0,
                0.30000001192092898,
                0.8999999761581421
            ],
            "setHealth": [
                1.0,
                -1.0,
                -1.0
            ],
            "toolHealthCoefEnable": 1,
            "coefHealthMinMaxValue": [
                0.5,
                1.0
            ],
            "toolQuantityCoefEnable": 1,
            "coefQuantityMinMaxValue": [
                0.5,
                1.0
            ],
            "toolDamageCoef": 1.0,
            "addAgents": [
                4
            ],
            "perkCoefEnable": 1,
            "perkCoefList": []
        },
        {
            "itemClassname": "Bone",
            "setCount": [
                1,
                -1,
                -1
            ],
            "chanceToSpawn": 1.0,
            "toolsSpawnList": {},
            "haveQuantity": 1,
            "setQuantity": [
                -1.0,
                0.10000000149011612,
                0.5
            ],
            "setHealth": [
                1.0,
                -1.0,
                -1.0
            ],
            "toolHealthCoefEnable": 1,
            "coefHealthMinMaxValue": [
                0.5,
                1.0
            ],
            "toolQuantityCoefEnable": 1,
            "coefQuantityMinMaxValue": [
                0.699999988079071,
                1.0
            ],
            "toolDamageCoef": 1.0,
            "addAgents": [
                4
            ],
            "perkCoefEnable": 1,
            "perkCoefList": []
        },
        {
            "itemClassname": "Lard",
            "setCount": [
                0,
                -1,
                -1
            ],
            "chanceToSpawn": 1.0,
            "toolsSpawnList": {},
            "haveQuantity": 1,
            "setQuantity": [
                -1.0,
                0.30000001192092898,
                0.8999999761581421
            ],
            "setHealth": [
                1.0,
                -1.0,
                -1.0
            ],
            "toolHealthCoefEnable": 1,
            "coefHealthMinMaxValue": [
                0.5,
                1.0
            ],
            "toolQuantityCoefEnable": 1,
            "coefQuantityMinMaxValue": [
                0.699999988079071,
                1.0
            ],
            "toolDamageCoef": 1.0,
            "addAgents": [
                4
            ],
            "perkCoefEnable": 1,
            "perkCoefList": [
                {
                    "enableCoef": 1,
                    "perkID": 20,
                    "chanceToSpawn": 1.0,
                    "toolsSpawnList": {},
                    "setCount": [
                        1,
                        -1,
                        -1
                    ],
                    "haveQuantity": 1,
                    "setQuantity": [
                        -1.0,
                        0.30000001192092898,
                        0.8999999761581421
                    ],
                    "setHealth": [
                        1.0,
                        -1.0,
                        -1.0
                    ],
                    "toolHealthCoefEnable": 1,
                    "coefHealthMinMaxValue": [
                        0.5,
                        1.0
                    ],
                    "toolQuantityCoefEnable": 0,
                    "coefQuantityMinMaxValue": [
                        0.5,
                        1.0
                    ],
                    "addAgents": [
                        4
                    ]
                }
            ]
        },
        {
            "itemClassname": "CowPelt",
            "setCount": [
                0,
                -1,
                -1
            ],
            "chanceToSpawn": 1.0,
            "toolsSpawnList": {},
            "haveQuantity": 1,
            "setQuantity": [
                -1.0,
                0.30000001192092898,
                0.800000011920929
            ],
            "setHealth": [
                1.0,
                -1.0,
                -1.0
            ],
            "toolHealthCoefEnable": 1,
            "coefHealthMinMaxValue": [
                0.5,
                1.0
            ],
            "toolQuantityCoefEnable": 1,
            "coefQuantityMinMaxValue": [
                0.699999988079071,
                1.0
            ],
            "toolDamageCoef": 1.0,
            "addAgents": [
                4
            ],
            "perkCoefEnable": 1,
            "perkCoefList": [
                {
                    "enableCoef": 1,
                    "perkID": 63,
                    "chanceToSpawn": 1.0,
                    "toolsSpawnList": {},
                    "setCount": [
                        1,
                        -1,
                        -1
                    ],
                    "haveQuantity": 0,
                    "setQuantity": [
                        -1.0,
                        0.30000001192092898,
                        0.8999999761581421
                    ],
                    "setHealth": [
                        1.0,
                        -1.0,
                        -1.0
                    ],
                    "toolHealthCoefEnable": 1,
                    "coefHealthMinMaxValue": [
                        0.5,
                        1.0
                    ],
                    "toolQuantityCoefEnable": 0,
                    "coefQuantityMinMaxValue": [
                        0.5,
                        1.0
                    ],
                    "addAgents": []
                }
            ]
        }
    ]
}
```
