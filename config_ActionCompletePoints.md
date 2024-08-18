# Описание переменных в конфиге config_ActionCompletePoints.json
## Настройка начисления опыта при выполнении действий наследуемых классы ActionContiniousBase и ActionSingleUseBase
Описание действия `ActionChickenBreak`.

Позволяет вам указать здесь класснейм действия и при выполнении его, игрок будет получать опыт на указанный тип навыка.

- **`ActionChickenBreak`**: Класснейм действия.
- **`skillPoints`**: Количество получаемого опыта при выполнении.
- **`typeOfSkill`**: Тип навыка.
- **`showNotify`**: Флаг для отображения уведомлений - 1 или 0.

Пример:

```json
{
  "ActionChickenBreak": {
    "skillPoints": 0.5,
    "typeOfSkill": "HUNTING",
    "showNotify": 1
  },
 "ActionConsumeStarBalsam": {
        "skillPoints": 0.5,
        "typeOfSkill": "MEDICAL",
        "showNotify": 1
    },
}
