## Настройка книг при прочтении которых будет начисляться опыт или активироваться перк.

- **`RLF_MedicalBook3_Skills`**: `string` Класснейм книги.
- **`className`**: `string` Класснейм книги.
- **`skillPoints`**: `float` Количество начисляемого опыта.
- **`typeOfSkill`**: `string` Тип навыка на который будет начислен опыт.
- **`isPerkActivatedBook`**: `bool` Если эта книга для активации перка, значение должно быть `true`.
- **`perkActivatedID`**: `int` ID перка который будет активирован при прочтении.
- **`showNotify`**: `bool` Показывать уведомление о полученом опыте или изученом навыке.
  
```json
{
    "RLF_MedicalBook3_Skills": {
        "className": "RLF_MedicalBook3_Skills",
        "skillPoints": 15.0,
        "typeOfSkill": "MEDICAL",
        "isPerkActivatedBook": 0,
        "perkActivatedID": -1,
        "showNotify": 1
    },
}
```
