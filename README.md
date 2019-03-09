usage example:
```
$ pwd                                                                    
/mnt/c/Users/olegs/transliteration-tur                                   
$ cat test_krc_transliteration.py                                        
import sys                                                               
from transliterator import Transliterator                                
                                                                         
tr = Transliterator("krc_transliteration")                               
[print(tr.transliterate(line.rstrip())) for line in sys.stdin]           
$ cut -f2 ../trk-covered | head -3                                       
джыл                                                                     
эм                                                                       
джылны                                                                   
$ cut -f2 ../trk-covered | head -3 | python3 test_krc_transliteration.py 
dzil                                                                     
em                                                                       
dzilni                                                                   
$                                                                        
```
