## class PlayerBase

Возвращает активен ли перк
```bool IsPerkActive(int perkID)```

Добавляет опыт игроку (СЕРВЕР)
```C#
/*!
 * Функция класса PlayerBase — добавляет игроку очки указанного навыка.
 *
 * @param instigator    Объект, инициировавший добавление (например, this).
 * @param skillName     Название навыка (например, "HUNTING").
 * @param amount        Количество добавляемых очков.
 * @param showNotify    Показывать ли уведомление игроку.
 *
 * @example
 * bool notify = true;
 * player.AddSkillPoint(this, "HUNTING", 10, notify);
 */
void AddSkillPoint(Class instigator, string skillName, int amount, bool showNotify);
```

Активация перка (СЕРВЕР)
```C#
/*!
 * Функция класса PlayerBase — активирует указанный перк у игрока.
 *
 * @param instigator    Объект, инициировавший активацию (обычно this).
 * @param perkID        ID перка, который нужно активировать.
 * @param showNotify    Показывать игроку уведомление об активации.
 *
 * @example
 * player.ActivatePerk(this, 100, false);
 */
void ActivatePerk(Class instigator, int perkID, bool showNotify);
```
