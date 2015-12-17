# caesar-decryption
A little Python script that does the following things:

1. Encrypt a given string seperated by space using Caesar shift. Number of shift is specified by user.
2. Decrypt an encrypted string.
3. Encrypt a given string using a randomly generated bijection function between sets of all letters.

#### Demo 1: Caesar encryption and decryption
 ```
Enter the string you want to encrypt: Got beaten up by friends by attending fake events on Facebook
Enter shift:5
------Encrypting------
Message: Got beaten up by friends by attending fake events on Facebook
Encrypted Message: Lty gjfyjs zu gd kwnjsix gd fyyjsinsl kfpj jajsyx ts Kfhjgttp
------Decrypting------
Trying shift = 0	Lty gjfyjs zu gd kwnjsix gd fyyjsinsl kfpj jajsyx ts Kfhjgttp
Trying shift = 1	Muz hkgzkt av he lxoktjy he gzzktjotm lgqk kbktzy ut Lgikhuuq
Trying shift = 2	Nva ilhalu bw if myplukz if haalukpun mhrl lcluaz vu Mhjlivvr
Trying shift = 3	Owb jmibmv cx jg nzqmvla jg ibbmvlqvo nism mdmvba wv Nikmjwws
Trying shift = 4	Pxc knjcnw dy kh oarnwmb kh jccnwmrwp ojtn nenwcb xw Ojlnkxxt
......
Trying shift = 18	Dlq ybxqbk rm yv cofbkap yv xqqbkafkd cxhb bsbkqp lk Cxzbyllh
Trying shift = 19	Emr zcyrcl sn zw dpgclbq zw yrrclbgle dyic ctclrq ml Dyaczmmi
Trying shift = 20	Fns adzsdm to ax eqhdmcr ax zssdmchmf ezjd dudmsr nm Ezbdannj
Trying shift = 21	Got beaten up by friends by attending fake events on Facebook
......
Trying shift = 25	Ksx fiexir yt fc jvmirhw fc exxirhmrk jeoi izirxw sr Jegifsso
Got beaten up by friends by attending fake events on Facebook
 ```

#### Demo 2: Random substition encryption
```
Enter the string you want to encrypt: Got beaten up by friends by attending fake events on Facebook
Encryption 1: Xih zlnhlu pe zs qobluvr zs nhhluvbux qndl lcluhr iu Qntlziid
Encryption 2: Pfo jixoiq wd jm nlyiqak jm xooiqayqp nxti iziqok fq Nxcijfft
Encryption 3: Fsw krywrp bh kx czerpil kx ywwrpiepf cyqr rtrpwl sp Cygrkssq
Encryption 4: Qeu ayruyn vt ab jfmynpk ab ruuynpmnq jroy yzynuk en Jriyaeeo
Encryption 5: Sxk owqkwe jh od irawezc od qkkwezaes iqtw wpwekc xe Iqvwoxxt
Encryption 6: Bwf daefaj zq dt hcgajlx dt effajlgjb heoa akajfx wj Hesadwwo
```

#### Next step: 

Come up with an algorithm that decipher the message encrypted in Demo 2.
