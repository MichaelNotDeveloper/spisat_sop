# Списать соп бесплатно



Запускаете на компе, только потом успейте выключить,
и заходим в [анкету сопа](https://lms.hse.ru/yii_index.php?r=rt/hse-rt-student-event-list)

```
git clone https://github.com/MichaelNotDeveloper/spisat_sop.git && 
cd spisat_sop && 
pip install pyautogui &&
python3 do_soap.py
```

```py
import pyautogui
import time
time.sleep(5)
delay = 0.02
for _ in range(1000):
    pyautogui.press('tab')
    time.sleep(delay)
    pyautogui.press('-')
    time.sleep(delay)
    pyautogui.press('left')
    time.sleep(delay)
```

У вас пять секунд чтобы кликнуть на галочку Затрудняюсь ответить в первом вопросе

Куда потратить сэкономленные 30 секунд?
- Позвонить маме
- Признатся в любви
- Решится написать ейчарке в компанию мечты
- Депнуть в казик
- Поставить звездочку проекту 
