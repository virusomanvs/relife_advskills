# Описание переменных в конфиге config_ActionCompletePoints.json

Параметры могут быть указаны для поиска начисляемого опыта по имени переменной.

## `GetAdvSkills().GetAddPointsFromName(string pointConfigName)`

Функция возвращает значение типа `float` для указанного имени начисления опыта.

### Параметры:

- **`pointConfigName`**: Строка, представляющая параметр.

### Возвращаемое значение:

- Если `AddPointBaseList` существует и содержит указанное `pointConfigName`, то возвращается соответствующее значение.
- В противном случае возвращается `0`.

### Пример использования:

```csharp
float result = GetAdvSkills().GetAddPointsFromName("PlayerKilled");
// Вернется значение 15.0 
```

Пример конфигурации:

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
