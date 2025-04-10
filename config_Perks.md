## Настройка списка текущих перков. Можете редактировать, добавлять свои чтобы настроить другие виды перков.
## Вы также можете добавлять сюда собственные перки или же удалить полностью запись о перке (это будет равно параметру PerkActive)

- **`PerkActive`**: `bool` Визуально отключает перк и убирает его из списка. Программно часть перков меняют исходный код, и поэтому убрать некоторые отсюда недостаточно чтобы вернуть ванильный функционал. Если у вас какой-то конфликт, напишите мне в ЛС, я постараюсь вам помочь в меру своих возможностей, если от меня что либо зависит.
- **`PerkName`**: `int` ID перка. Должен быть уникальным.
- **`PerkNameDisplay`**: `string` Имя перка которое отображается в меню перков. Может быть как строка перевода так и обычный текст.
- **`PerkInfo`**: `string` Описание перка которое отображается в меню перков.. Может быть как строка перевода так и обычный текст.
- **`PerkIcon`**: `string` Иконка перка. Список готовых иконок лежит в pbo relife_AdvSkills_Icons.pbo. Сюда достаточно вписать имя нужной иконки. Чтобы добавить свою иконку, запакуйте ее в этот PBO как и остальные иконки и укажите здесь ее имя. Если вы не знаете как открыть edds файлы и посмотреть иконку, вы можете на гугл диске найти архив с конвертированными иконками, их название идентичны.
  
![image](https://github.com/user-attachments/assets/27649003-83b6-43d1-974e-c79810871090)

- **`PerkSkillType`**: `string` Тип навыка к которому относится перк. Будет отображен в меню в соответствующем разделе.
- **`DefaultStatus`**: `bool` 1 = Активировать перк у игрока по умолчанию при первом заходе или после смерти. То есть перк будет всегда активирован.
- **`DisableBeforeParentActive`**: `bool` 1 = перк не будет отображен в меню перков, если он состоит в цепочке перков и перк который требуется для его активации не активирован.
- **`NeedLvl`**: `float` Стоимость перка. Если указано -1 то будет отображено что необходима книга для активации. И перк можно будет активировать только прочитав книгу, для этого вам нужно ее сделать и указать в соответствующем конфиге по книгам.
- **`NeedOtherPerk`**: `int` ID перка который необходим для активации этого перка.
- **`blockOtherPerk`**: `int` ID перка при активации которого, этот перк будет невозможно активировать. Не работает в обратную сторону! Если вы здесь укажите перк 222, то при активации его вы не сможете активировать этот, но если вы активируете этот перк, вы сможете активировать 222. Для 222 перка, также нужно вносить настройку.
- **`chanceToClear`**: `float` Шанс сброса перка если есть соответствующая настройка в сбросах перков у игрков. От 0 до 1.
- **`NeedAllReadedBook`**: `bool` 1 Если нужно прочесть все книги из перка чтобы он был разблокирован. 0 Нужно будет прочесть одну из книг в списке.
- **`AllowReturn`**: `bool` Включает возможность вернуть перк и вернуть за это часть поинтов из параметра ReturnPoints. Выключено по умолчанию.
- **`ReturnPoints`**: `float` Кол-во поинтов которое будет возвращено в случае возврата перка.
- **`NeedBooksToShow`**: `TStringArray` Массив с класснеймами книг, которые нужно прочесть чтобы перк был показан в списке. Оставить пустым если открыт по умолчанию. Если здесь есть класснейм книги, то перка не будет в списке всех перков, пока вы не прочтете одну или все из списка. Не забудьте настроить книги чтобы они были в статусе показа перков.

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
        "blockOtherPerk": -1,
        "chanceToClear": 1.0,
        "NeedAllReadedBook": 1,
        "AllowReturn": 0,
        "ReturnPoints": 30,
        "NeedBooksToShow": ["RLF_MedicalBook3_Skills", "RLF_MedicalBook2_Skills"],
    },
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
        "blockOtherPerk": -1,
        "chanceToClear": 1.0,
        "NeedAllReadedBook": 0,
        "AllowReturn": 0,
        "ReturnPoints": 30,
        "NeedBooksToShow": []
    },
]
```

## Список ID перков можно посмотреть в админке, либо ниже
![image](https://github.com/user-attachments/assets/32f0def1-d595-4815-b777-8b648e8fbf2b)
![image](https://github.com/user-attachments/assets/dc45ecc9-5fe0-4f29-8122-65659fb24505)
![image](https://github.com/user-attachments/assets/3a2db728-d477-4f70-ba16-4d03f3fc4a27)
![image](https://github.com/user-attachments/assets/6d1e7c55-ce3c-4116-ad88-c4d3b3b0bd22)
![image](https://github.com/user-attachments/assets/75ea4285-5251-4ec1-9af7-e27747d8854b)
![image](https://github.com/user-attachments/assets/a3375f45-6690-4bbf-86c7-a4ff120b39ad)
![image](https://github.com/user-attachments/assets/12c583d3-1e99-4339-8068-a13f959126cf)
![image](https://github.com/user-attachments/assets/ce6dbabc-4c3b-4106-b194-a02360e56977)
![image](https://github.com/user-attachments/assets/f6f01aed-4be1-4632-b97f-b2e01873c63b)








