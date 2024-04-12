##class PlayerBase

**`bool IsPerkActive(int perkID)`**
void AddSkillPoint(string skillType, float valuePoints)
void ActivatePerk( Class instance = this, int PerkID = -1, bool showNotify = false)

- **`enableLogsProfile`**: `bool` 0- 1. Вкл. или выкл. ведение логов которые сохраняются по пути **profiles\LogArchives\relife_AdvSKills**
- **`PointsName`**: `string` Название очков опыта. Используется в отображении меню и уведомлениях.
- **`SkillTypes`**: `TStringArray` массив со списком типов навыков. Только заглавные символы. Вывод в меню навыков выводится в том же порядке, как они указаны в конфиге.
- **`SkillTypesList`**: Настройки для определенного типа навыка.
