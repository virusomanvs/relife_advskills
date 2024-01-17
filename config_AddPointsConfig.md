# Описание переменных в конфиге config_ActionCompletePoints.json

Описание действия `ActionChickenBreak`.

- **`ActionChickenBreak`**: Класснейм действия.
- **`skillPoints`**: Количество получаемого опыта при выполнении.
- **`typeOfSkill`**: Тип навыка.
- **`showNotify`**: Флаг для отображения уведомлений - 1 или 0.

# Описание функций в моем коде

## `GetAddPointsFromName(string pointConfigName)`

Функция возвращает значение типа `float` для указанного имени точки конфигурации.

### Параметры:

- **`pointConfigName`**: Строка, представляющая имя точки конфигурации.

### Возвращаемое значение:

- Если `AddPointBaseList` существует и содержит указанное `pointConfigName`, то возвращается соответствующее значение.
- В противном случае возвращается `0`.

### Пример использования:

```csharp
float result = GetAddPointsFromName("examplePoint");
// Результат может быть использован для дальнейших вычислений или операций.


Пример:

```json
{
    "CraftWhetstone": 1.0,
    "PlayerKilled": 15.0,
    "ActionInjectTarget": 1.0,
    "BadEatPrepareFruit": 0.0,
    "BadEatPrepareMeat": 0.0,
    "ActionFishingNewCircle": 0.10000000149011612,
    "BadEatPrepareFish": 0.0,
    "BloodTestSelf": 1.0
}
```
