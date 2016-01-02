# Caesar decryption and encryption

#### Usage:
```
>>>python main.py [file_name] [action] [shift]
```

#### Demo 1: Caesar encryption with user-defined number of shift

Original message:

_Data science is a phrase that is used too often. It has no clear definition because it has been defined differently by so many different people and organizations.
......
Those of us who practice the discipline seriously and professionally have a responsibility to ensure that data science is more than nominally scientific._

```
iseliget-MacBook-Air:caesar-decryption iseliget$ python main.py test.txt encrypt 7
Encryting file......
Encrypted file saved at "encrypted_test.txt"
```

Encrypted message:

_Khah zjplujl pz h woyhzl aoha pz bzlk avv vmalu. Pa ohz uv jslhy klmpupapvu iljhbzl pa ohz illu klmpulk kpmmlyluasf if zv thuf kpmmlylua wlvwsl huk vynhupghapvuz. 
......
Aovzl vm bz dov wyhjapjl aol kpzjpwspul zlypvbzsf huk wyvmlzzpvuhssf ohcl h ylzwvuzpipspaf av luzbyl aoha khah zjplujl pz tvyl aohu uvtpuhssf zjpluapmpj._

#### Demo2: Decrypt file encrypted by Caesar

Original message:

_Khah zjplujl pz h woyhzl aoha pz bzlk avv vmalu. Pa ohz uv jslhy klmpupapvu iljhbzl......Aovzl vm bz dov wyhjapjl aol kpzjpwspul zlypvbzsf huk wyvmlzzpvuhssf ohcl h ylzwvuzpipspaf av luzbyl aoha khah zjplujl pz tvyl aohu uvtpuhssf zjpluapmpj._

```
iseliget-MacBook-Air:caesar-decryption iseliget$ python main.py encrypted_test.txt decrypt
Decrypting file......
Decrypted file save at "decrypted_encrypted_test.txt"
```

Decrypted message:

_Data science is a phrase that is used too often. It has no clear definition because it has been defined differently by so many different people and organizations......Those of us who practice the discipline seriously and professionally have a responsibility to ensure that data science is more than nominally scientific._
