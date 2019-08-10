# Python-class learning note
---
## **basic coding**

```
class Dog:
    def __init__(self, blood, age):
        self.bloodtype = blood
        self.dog_age = age
d = Dog('B', 23)
e = Dog('O', 20)
print(d.bloodtype)
```
---
## **explain**
* class : 定義類別(通常:首字大寫)
* def __init__(self, blood , age) : override系統設定(類似初始定義)，定義儲存資料的形式
-self : 指派使用class的參數，作為class的同位語
-blood / age : 儲存資料的變數
* self.bloodtype = blood : 以此呼叫方式，會回傳該物件的資料的值
* d = Dog('B', 23) : 建立物件
---
## **instance**

waiting complete...