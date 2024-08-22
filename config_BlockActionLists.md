## Здесь можно настроить блокировку действий (не всех), если у вас не вкачан перк. К примеру вы не хотите чтобы можно было крафтить болты для арбалета (а это не крафт, а действие), то можете заблочить его пока не вкачан перк. А при попытке выполнить действие, будет выведено уведомление что у вас не вкачан нужный перк.


Список ванильных действий можно найти в классе ActionConstructor, с другими модами точно также. 

- **`actionName`**: `string` Класс действия который, будет заблокирован, если **neededPerkID** не активирован у игрока.
- **`neededPerkID`**: `int` ID перка, который будет активировать доступность крафта.
  
```json
[
    {
        "actionName": "ActionClassName",
        "neededPerkID": 0
    },
    {
        "actionName": "ActionClassName2",
        "neededPerkID": 2
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
