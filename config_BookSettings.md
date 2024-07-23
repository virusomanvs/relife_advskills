## Настройка книг при прочтении которых будет начисляться опыт, активироваться или разблокироваться перк.

- **`RLF_MedicalBook1_Skills`**: `string` Класснейм книги.
- **`skillPoints`**: `float` Количество начисляемого опыта.
- **`typeOfSkill`**: `string` Тип навыка на который будет начислен опыт.
- **`isPerkShowBook`**: `bool` Если эта книга для разблокировки перков (скрытия их до прочтения книги), значение должно быть `1`.
- **`isPerkActivatedBook`**: `bool` Если эта книга для активации перка, значение должно быть `1`.
- **`perkActivatedID`**: `int` ID перка который будет активирован при прочтении.
- **`showNotify`**: `bool` Показывать уведомление о полученом опыте или изученом навыке.
  
```json
{
    "RLF_MedicalBook1_Skills": {
        "skillPoints": 15.0,
        "typeOfSkill": "MEDICAL",
        "isPerkActivatedBook": 0,
        "isPerkShowBook": 0,
        "perkActivatedID": -1,
        "showNotify": 1
    },
}
```
