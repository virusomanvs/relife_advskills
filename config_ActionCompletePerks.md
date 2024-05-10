# Описание переменных в конфиге config_ActionCompletePerks.json
## Настройка активации перка при выполнении действий наследуемых классы ActionContiniousBase и ActionSingleUseBase
Описание действия `ActionChickenBreak`.

- **`ActionChickenBreak`**: Класснейм действия.
- **`skillPoints`**: Количество получаемого опыта при выполнении.
- **`typeOfSkill`**: Тип навыка.
- **`showNotify`**: Флаг для отображения уведомлений - 1 или 0.

Пример:

```json
{
  "ActionBandageSelf": {
    "skillPoints": 0.5,
    "typeOfSkill": "HUNTING",
    "showNotify": 1
  },
 "ActionBandageSelf": {
        "perkID": 100,
        "itemInHandsList": [],
        "showNotify": 1
    }
}
