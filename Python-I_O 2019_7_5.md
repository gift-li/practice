# Python-I/O 2019/7/5
---
## **basic coding**
```
data = open('open.txt', 'w', encoding='utf-8')
data.write('happy')
(資訊處理)
data.close()
```
---
## **explain**
* open() : 以何種方式開啟檔案
standard : open('file','mode',encoding='encoding system')
-'mode' : 開啟檔案的模式
```
open('a.txt','w',encoding='utf-8')
```

* 檔案.write(str) : 對該檔案寫入字串
```
a.txt.write('happy')`
```
---
## **instance**
* 重複創檔and寫入資訊:
```
for i in range(5):
    fp = open('a'+str(i)+'.txt', 'w', encoding= 'utf-8')
    fp.write('happy'+i)
    fp.close()
```
#### warning: \n為字串，需包覆在''內



waiting update...