## Настройка блокировки крафтов если не активирован определенный перк.

- **`recipeName`**: `string` Класс крафта который, будет заблокирован, если **neededPerkID** не активирован у игрока.
- **`neededPerkID`**: `int` ID перка, который будет активировать доступность крафта.
  
```json
[
    {
        "recipeName": "CraftClassname",
        "neededPerkID": 0
    },
    {
        "recipeName": "CraftClassname2",
        "neededPerkID": 2
    }
]
```
