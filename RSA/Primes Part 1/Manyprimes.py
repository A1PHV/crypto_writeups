from Crypto.Util.number import inverse, long_to_bytes

N = 580642391898843192929563856870897799650883152718761762932292482252152591279871421569162037190419036435041797739880389529593674485555792234900969402019055601781662044515999210032698275981631376651117318677368742867687180140048715627160641771118040372573575479330830092989800730105573700557717146251860588802509310534792310748898504394966263819959963273509119791037525504422606634640173277598774814099540555569257179715908642917355365791447508751401889724095964924513196281345665480688029639999472649549163147599540142367575413885729653166517595719991872223011969856259344396899748662101941230745601719730556631637
e = 65537
ciphertext = 320721490534624434149993723527322977960556510750628354856260732098109692581338409999983376131354918370047625150454728718467998870322344980985635149656977787964380651868131740312053755501594999166365821315043312308622388016666802478485476059625888033017198083472976011719998333985531756978678758897472845358167730221506573817798467100023754709109274265835201757369829744113233607359526441007577850111228850004361838028842815813724076511058179239339760639518034583306154826603816927757236549096339501503316601078891287408682099750164720032975016814187899399273719181407940397071512493967454225665490162619270814464

factor_set = (9282105380008121879, 9303850685953812323, 9389357739583927789, 10336650220878499841, 10638241655447339831, 11282698189561966721, 11328768673634243077, 11403460639036243901, 11473665579512371723, 11492065299277279799, 11530534813954192171, 11665347949879312361, 12132158321859677597, 12834461276877415051, 12955403765595949597, 12973972336777979701, 13099895578757581201, 13572286589428162097, 14100640260554622013, 14178869592193599187, 14278240802299816541, 14523070016044624039, 14963354250199553339, 15364597561881860737, 15669758663523555763, 15824122791679574573, 15998365463074268941, 16656402470578844539, 16898740504023346457, 17138336856793050757, 17174065872156629921, 17281246625998849649)

phi = 1
for prime in factor_set:
    phi *= (prime - 1)

d = inverse(e, phi)

plaintext = pow(ciphertext, d, N)
print(long_to_bytes(plaintext))