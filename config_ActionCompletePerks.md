# Описание переменных в конфиге config_ActionCompletePerks.json
## Настройка активации перка при выполнении действий наследуемых классы ActionContiniousBase и ActionSingleUseBase
Описание действия `ActionBandageSelf`.

- **`ActionBandageSelf`**: Класснейм действия.
- **`perkID`**: ID активируемого перка.
- **`itemInHandsList`**: Массив класснеймов предмета в руках, который должен быть чтобы перка активировался. Оставить пустым если предмет может быть любой.
- **`showNotify`**: Флаг для отображения уведомлений - 1 или 0.

Пример:

```json
{
   "ActionBandageSelf": {
        "perkID": 100,
        "itemInHandsList": [],
        "showNotify": 1
    }
 "ActionBandageTarget": {
        "perkID": 100,
        "itemInHandsList": ["Item1", "Item2"],
        "showNotify": 1
    }
}
