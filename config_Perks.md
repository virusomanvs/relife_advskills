## Настройка списка текущих перков.
## Вы также можете добавлять сюда собственные перки или же удалить полностью запись о перке (это будет равно параметру PerkActive)

- **`PerkActive`**: `bool` Визуально отключает перк и убирает его из списка. Программно часть перков меняют исходный код, и поэтому убрать некоторые отсюда недостаточно чтобы вернуть ванильный функционал.
- **`PerkName`**: `int` ID перка.
- **`PerkNameDisplay`**: `string` Имя перка. Может быть как строка перевода так и обычный текст.
- **`PerkInfo`**: `string` Описание перка. Может быть как строка перевода так и обычный текст.
- **`PerkIcon`**: `string` Иконка перка. Список готовых иконок лежит в pbo relife_AdvSkills_Icons.pbo. Сюда достаточно вписать имя нужной иконки.
- **`PerkSkillType`**: `string` Тип навыка к которому относится перк.
- **`DefaultStatus`**: `bool` Неактуально.
- **`NeedLvl`**: `float` Стоимость перка. Если указано -1 то будет отображено что необходима книга для активации.
- **`NeedOtherPerk`**: `int` ID перка который необходим для активации этого перка.
- **`NeedAllReadedBook`**: `bool` 1 Если нужно прочесть все книги из перка чтобы он был разблокирован. 0 Нужно будет прочесть одну из книг в списке.
- **`NeedBooksToShow`**: `TStringArray` Массив с класснеймами книг, которые нужно прочесть чтобы перк был показан в списке. Оставить пустым если открыт по умолчанию.
- **`chanceToClear`**: `float` Шанс сброса перка если есть соответствующая настройка в сбросах перков у игрков.


```json
[
    {
        "PerkActive": 1,
        "PerkName": 188,
        "PerkNameDisplay": "#str_perk_name_181",
        "PerkInfo": "#str_perk_info_181",
        "PerkIcon": "energyhealth",
        "PerkSkillType": "MEDICAL",
        "DefaultStatus": 0,
        "NeedLvl": 25.0,
        "NeedOtherPerk": -1,
        "NeedAllReadedBook": 1,
        "NeedBooksToShow": ["RLF_MedicalBook3_Skills", "RLF_MedicalBook2_Skills"],
        "chanceToClear": 1.0
    },
    {
        "PerkActive": 1,
        "PerkName": 187,
        "PerkNameDisplay": "#str_perk_name_182",
        "PerkInfo": "#str_perk_info_182",
        "PerkIcon": "waterhealth",
        "PerkSkillType": "MEDICAL",
        "DefaultStatus": 0,
        "NeedLvl": 25.0,
        "NeedOtherPerk": -1,
        "NeedAllReadedBook": 0,
        "NeedBooksToShow": ["RLF_MedicalBook3_Skills"],
        "chanceToClear": 1.0
    }
]
```
