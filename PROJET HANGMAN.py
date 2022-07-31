import os
import random
q=input('Peze _k_ pouw gade koman jwet la jwe siw pat konnen deja sinon peze nenpot lot let pouw ka komanse jwe')
if q.lower() == 'k':
    print('Se yon jwet ki byen fasil e li amizan anpil...\nSe yon jwet kote yo baw on on fraz ki pral seviw kom yon endis pou w ka jwenn on mo.\nMen mo sa kache avek asterisk(*) pou w pa we ki mo li ye.\nChak let ou mete oswa ou panse mo a ka genyen si li genyen l li pral pran plas li nan mo a si li pa genyen l tou wap we pa gen okenn asterisk kap soti. Wap konplete mo a jouskaske ou jwenn tout mo a konple\nKonnya ou konnen koman li jwe, Enbyen jwe...\n Bon Chans!!!!!')
if q.lower()!="k": 

	dictionary = {"jovenel":"Pi resan prezidan ayisyen ki mouri sou pouvwa a", 
      'disko':'Kote moun al danse bwe,danse,e tande anpil mizik',
      "fim":"On bagay moun konn al gade nan sinema",
      "palmis":"Pye bwa ki reprezante ayisyen yo sou drapo yo a",
      "laptop":"Yo sevi avel pou gade videyo,jwe genm,e se sou li yo kode(prensipalman)",
      'plim':'Yo sevi avel pou ekri nan fey sou kaye e li souvan gen koule ble',
      'kreyon':'Yo sevi avel pou desine paske le ou fini ou ka efasel ak yon gom'}

	key = []
	for x in dictionary:
		key.append(x)
	name = random.choice(key)


	length =int(len(name))
	asterix = '*'*length

	while name != asterix:
		os.system('cls')

		print(dictionary[name])
		print("\nSa se mo wap verifye a: ",asterix)
	
		a =input("antre let ki manke yo pou konplete mo a:\n>>> ")
		a = a.lower()
		count = name.count(a)

		position = [pos for pos, char in enumerate(name) if char==a]

		if a in name and len(a)==1:

			index = name.find(a)

			if count==2:
				position = [pos for pos, char in enumerate(name) if char==a]

				position1 = position[0]
				position2 = position[1]

				asterix = asterix[:position1] +a+ asterix[position1+1:]
				asterix = asterix[:position2] +a+ asterix[position2+1:]

			elif count>2:
				position1 = position[0]
				position2 = position[1]
				position3 = position[2]

				asterix = asterix[:position1] +a+ asterix[position1+1:]
				asterix = asterix[:position2] +a+ asterix[position2+1:]
				asterix = asterix[:position3] +a+ asterix[position3+1:]
			else:
				asterix = asterix[:index]+a+asterix[index+1:]

	print(asterix)
