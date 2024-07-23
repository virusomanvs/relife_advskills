## Добавление своих типов навыков и изменение уже существующих.
- **`enableLogsProfile`**: `bool` 0- 1. Вкл. или выкл. ведение логов которые сохраняются по пути **profiles\LogArchives\relife_AdvSKills**
- **`PointsName`**: `string` Название очков опыта. Используется в отображении меню и уведомлениях.
- **`SkillTypes`**: `TStringArray` массив со списком типов навыков. Только заглавные символы. Вывод в меню навыков выводится в том же порядке, как они указаны в конфиге.
- **`SkillTypesList`**: Настройки для определенного типа навыка.

## SkillTypesList
```json
"SkillTypesList": [
    {
         "skillType": "HUNTING",
         "skillTypeTitle": "#STR_RLF_SKILL_HUNTING",
         "skillTypeNotifyIcon": "relife_AdvSkills/gui/images/hunting.edds",
         "skillTypeMenuIcon": "relife_AdvSkills/gui/imagesets/top_menu/hunter.edds",
         "SkillStartedPoints": 0.0,
         "PointsDecreaseAfterDeath": 0.0
    }
]
```
- **`skillType`**: `string` Имя навыка, которое определено в параметре **SkillTypes**
- **`skillTypeTitle`**: `string`  Название навыка для отображения в меню и уведомлениях.
- **`skillTypeNotifyIcon`**: `string` Полный путь к иконке формата **.edds** для отображения в уведомлениях.
- **`skillTypeMenuIcon`**: `string` Полный путь к иконке формата **.edds** для отображения в меню.
- **`SkillStartedPoints`**: `float` Количество очков на старте игрока или при смерти (в соответствии с настройками смерти).
- **`PointsDecreaseAfterDeath`**:  `float` Значение от 0.0 до 1.0 на сколько в процентах снизится кол-во опыта данного типа при смерти.
  
### ==============================

- **`StartingPointsForAll`**:  `float` Стартовое значения опыта, если в параметрах типа навыка не указано начальное значение.
- **`PointsDecreaseAfterDeathForAll`**:  `float` Значение от 0.0 до 1.0 на сколько в процентах уменьшится опыт, если в параметрах типа навыка не указано начальное значение.
- **`enableDefaultWeaponRecord`**:  `bool` Включить тряску оружия для всех видов используя параметр DefaultWeapon.
- **`DefaultSkinningTime`**: `float` Первоначальная скорость разделки животных без перков.
## Добавление опыта ОХОТНИКА игроку при стрельбе из оружия.

- **`AddPointToPlayerWeaponFire`**: `bool` Включить/выключить начисление при стрельбе.
- **`EnableDefaultPointToPlayerWeaponFire`**: `bool` Включить/выключить начисление опыта при стрельбе из все оружий, но если перед параметром DefaultWeapon будет запись с оружием, параметры будут браться из него.
- **`WeaponFireAddPoints`**: `string`,`float`  Класснейм оружия наследуемого Weapon_Base и начисляемый опыт за каждый патрон. Опыт будет начислен при достижении значения AddPointMax
- **`AddPointMax`**: `float` Каждый выстрел хранит и плюсует общее значение, при достижении этого значения будет начислено текущее количество опыта. Например: АКМ за каждый выстрел 0.25, AddPointMax = 1, значит при выстреле 4 раза будет начислен AddPointMax. Лишний опыт будет отсеян. Например, если получится при выстреле значение больше чем положено, будет все равно начислено AddPointMax.
- **`PointSkillType`**: `string` Навык, куда будет начислен опыт за стрельбу. HUNTING по умолчанию.
- **`ShowWeaponFireAddPointNotify`**: `bool` Показывать уведомление при начислении опыта.

  
`!ВНИМАНИЕ! Не проверено на слабых системах, возможно снижение серверного FPS так как много каких действий происходит за каждый выстрел.`

```json
{
    "AddPointToPlayerWeaponFire": 1,
    "EnableDefaultPointToPlayerWeaponFire": 0,
    "AddPointMax": 1.0,
    "WeaponFireAddPoints": {
        "Magnum": 1.0,
        "AKM": 0.25,
        "DefaultWeapon": 1.0
    },
    "ShowWeaponFireAddPointNotify": 1
}
```
## Настройка сброса перков и опыта в случае смерти игрока

- **`CLEARPERKAFTERDEATH`**: `bool` Включить/выключить сброс перков при смерти игрока
- **`ClearPlayerPerkUsingPenalty`**: `bool` Включить сброс перков при достижении определенного количества смертей
- **`PlayerCountDeathToPenalty`**: `int` Количество смертей при достижении которых сброятся перки
- **`clearPlayersPoints`**: `bool` Включить/выключить сброс опыта при смерти игрока
- **`enableDeacreasePoints`**: `bool` Включить/выключить сброс опыта на определенный процент указанный в типе навыка при смерти игрока
- **`clearReadedBook`**: `bool` Сброс прочитанных книг. 
- **`clearPerkUsingChance`**: `bool` Сброс перков используя их внутренний шанс сброса **chanceToClear** 
- **`clearPerkUsingRandom`**: `bool` Сброс случайных перков в количестве указанном в **clearPerkUsingRandom_count**. Зависимые перки также будут сброшены по цепочке.
- **`clearPerkUsingRandom_count`**: `int` Количество сбрасываемых перков в случае если **clearPerkUsingRandom** равен `true`.
- **`IgnoreDeathPerkPlayers`**: `TStringArray` массив строк STEAMID для игнорирования сброса перков. При наличии STEAMID игрока, на него не будут распространяться никакие настройки сброса перков или опыта.
```json
{
     "IgnoreDeathPerkPlayers": [
        "steamid1",
        "steamid2"
     ],
}
```
## Настройка вырезания гнили в продуктах
- **`BadEatPrepareTool`**: `TStringArray` массив с класснеймом предметов с помощью которых можно будет вырезать гниль из продуктов.
```json
{
    "BadEatPrepareTool": [
        "Sickle",
        "KukriKnife",
        "FangeKnife",
        "Hacksaw",
    ]
}
```
- **`BadEatPrepareMeat`**: `TStringArray` массив с класснеймом мяса в котором можно будет вырезать гниль.
```json
{
    "BadEatPrepareMeat": [
       "CowSteakMeat",
        "SheepSteakMeat",
        "GoatSteakMeat",
        "MouflonSteakMeat",
        "BoarSteakMeat"
    ]
}
```
- **`BadEatPrepareFish`**: `TStringArray` массив с класснеймом рыбы в которой можно будет вырезать гниль.
```json
{
    "BadEatPrepareFish": [
        "CarpFilletMeat",
        "MackerelFilletMeat"
    ]
}
```
- **`BadEatPrepareFruit`**: `TStringArray` массив с класснеймом фруктов, овощей или грибов в которых можно будет вырезать гниль.
```json
{
    "BadEatPrepareFruit": [
         "Apple",
        "Plum",
        "Pear",
    ]
}
```
## Настройки для пасссивного начисления опыта Силы
## начисление опыта происходит когда сумма значения будет равна 1, максимальное значение может быть 1. То есть, если у вас стоит значение 0.2 за метр, вам нужно пройти 5 метров, тогда будет начислено 1 очко навыков.

- **`Endurance_Per_Meter`**: `float` Начисление опыта при пройденном растоянии за каждый метр.
- **`Endurance_Per_Full_Stamina_Melee`**: `float` Начисление опыта при ударах в рукопашном бою.
- **`Endurance_Per_Jump`**: `float` Начисление опыта за каждый прыжок.

