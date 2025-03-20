## Здесь можно настроить перки которые позволяют чинить вещи до состояния НЕТРОНУТО.

- **`perkID`**: `int` ID перка.
- **`repairKitList`**: `TStringArray` Массив наборов ремонта. Нужно явное указание, не подерживается наследуемость.
- **`disallowMode`**: `bool` Если включен, то можно будет починить все предметы кроме тех которые есть в itemsList.
- **`itemsList`**: `TStringArray` Массив вещей. Нужно явное указание, не подерживается наследуемость. Если здесь что либо есть, и disallowMode выключен, то можно будет починить только предметы из списка.
  
```json
[
    {
        "perkID": 251,
        "repairKitList": [
            "SewingKit"
        ],
        "disallowMode": 1,
        "itemsList": [
            "disalowItems"
        ]
    },
    {
        "perkID": 252,
        "repairKitList": [
            "OtherKit"
        ],
        "disallowMode": 1,
        "itemsList": [
            "disalowItems"
        ]
    }
]
