# Описание настроек мода перков для сторонних модов которые хранятся в конфигах этих модов.

### COTZ_Workbench https://steamcommunity.com/sharedfiles/filedetails/?id=2895049000 
### HP_Crafter https://steamcommunity.com/sharedfiles/filedetails/?id=3133007745. 
### ТОЛЬКО ДЛЯ ЭТИХ МОДОВ
Вы можете настроить блокировку крафта в верстаке, если не активирован перк, достаточно в конфиг крафта добавить дополнительные параметры.

- **`needPerkToCraft`** `int`: ID перка который блокирует крафт в верстаке, если он не активирован.
- **`addPointForCraft`** `float`: Количество опыта выдаваемого после крафта на верстаке.
- **`typeSkill`** `string`: Тип навыка на который начислять опыт.

Пример конфига, добавьте параметры от перков в свой конфиг верстака:

```json
		"CraftCategories": [
			{
			    "CategoryName": "Крафт",
  				"CraftItems": [
  					{
  						"Result": "Plum",
  						"ResultCount": 1,
  						"needPerkToCraft": 100,
  						"addPointForCraft": 1,
  						"typeSkill": "HUNTING",
  						"ComponentsDontAffectHealth": 1,
  						"CraftType": "craft",
  						"RecipeName": "Крафт сливы",
  						"CraftComponents": [
  						{
  							"Classname": "Apple",
  							"Amount": 1,
  							"Destroy": 1,
  							"Changehealth": 0
  						}
  							],
  						"AttachmentsNeed": [
  												
  						]
  					},
```
