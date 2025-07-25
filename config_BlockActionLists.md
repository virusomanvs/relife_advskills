## Здесь можно настроить блокировку действий (не всех), если у вас не вкачан перк. К примеру вы не хотите чтобы можно было крафтить болты для арбалета (а это не крафт, а действие), то можете заблочить его пока не вкачан перк. А при попытке выполнить действие, будет выведено уведомление что у вас не вкачан нужный перк.


Список ванильных действий можно найти в классе ActionConstructor, с другими модами точно также. 

| Поле              | Тип             | Описание                                                                                                                                                                                          |
| ----------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `actionName`      | `string`        | Название действия, которое нужно ограничить (например, `ActionChopTree`). Указывается имя класса действия.                                                                                        |
| `neededPerkID`    | `int`           | ID перка, который требуется для выполнения действия (если условие выполнено).                                                                                                                     |
| `isWhitelist`     | `bool`          | Определяет, как работает список предметов:<br>• `true` — список предметов, **требующих** активного перка;<br>• `false` — список предметов, **исключённых** из требования перка.                   |
| `useIsKindOf`     | `bool`          | Использовать ли `IsKindOf` для сравнения типов:<br>• `true` — будет использовать `GetGame().IsKindOf(item, type)`;<br>• `false` — будет использовать строгое сравнение по имени (`item == type`). |
| `itemInHandsList` | `array<string>` | Список названий классов предметов в руках, на которые распространяется правило. Может быть пустым (означает, что правило применяется ко всем предметам).                                          |



```json
[
    {
        "actionName": "ActionLockDoors",
        "neededPerkID": 133,
        "useIsKindOf": 0,
        "isWhitelist": 0,
        "itemInHandsList": []
    },
    {
        "actionName": "ActionUnlockDoors",
        "neededPerkID": 133,
        "useIsKindOf": 0,
        "isWhitelist": 0,
        "itemInHandsList": []
    }
]
```
ВНИМАНИЕ! Ваш экшен должен наследовать ActionConditionContinue иначе блок не будет работать. Чтобы у вас работал блок для модовых экшенов, там где есть свой ActionConditionContinue. Просто переопределите его

```C#
  override bool ActionConditionContinue(ActionData action_data)
	{
		if(super.ActionConditionContinue(action_data))
			return PerkBlockerCondition(action_data.m_Player, action_data.m_Target, action_data.m_MainItem);

		return super.ActionConditionContinue(action_data);
	}
```
