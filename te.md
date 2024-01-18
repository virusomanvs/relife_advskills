- **`enableLogsProfile`**: `bool` 0- 1. Вкл. или выкл. ведение логов которые сохраняются по пути **profiles\LogArchives\relife_AdvSKills**
- **`PointsName`**: `string` Название очков опыта. Используется в отображении меню и уведомлениях.
- **`SkillTypes`**: `TStringArray` массив со списком типов навыков. Только заглавные символы. Вывод в меню навыков выводится в том же порядке, как они указаны в конфиге.
- **`SkillTypesList`**: Настройки для определенного типа навыка.

## SkillTypesList
```json
"SkillTypesList": [
    {
         "skillType": "HUNTING",
         "skillTypeTitle": "#STR_RLF_SKILL_HUNTING",
         "skillTypeNotifyIcon": "relife_AdvSkills/gui/images/hunting.edds",
         "skillTypeMenuIcon": "relife_AdvSkills/gui/imagesets/top_menu/hunter.edds",
         "SkillStartedPoints": 0.0,
         "PointsDecreaseAfterDeath": 0.0
    }
]
```
