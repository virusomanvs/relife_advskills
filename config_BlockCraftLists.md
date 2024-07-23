## Настройка блокировки крафтов если не активирован определенный перк.
Здесь вы можете указать крафт, и пока не активирован перк, вы не сможете выполнить этот крафт.

Список вванильных крафтов можно найти в функции RegisterRecipies, с другими модами точно также.

![image](https://github.com/user-attachments/assets/f48648cb-255b-4781-a697-09cab53b7bf8)

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
