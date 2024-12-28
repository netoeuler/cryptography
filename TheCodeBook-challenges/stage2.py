#Stage 2: Caesar Ciper (Shift)

code = "MHILY LZA XBHL XBPZXBL MVYABUHL HWWPBZ JSHBKPBZ JHLJBZ KPJABT HYJHUBT LZA ULBAYVU"

ini = 65
end = 90

last_str = code

for i in range(20):
	new_str = ''
	for s in last_str:
		new_s = chr((ord(s)+1))
		
		if s == ' ':
			new_str += ' '
			continue
		if ord(new_s) > end:
			new_s = chr(ini)

		new_str += new_s
		last_str = new_str
	print(i,new_str)

#The answer is on position 18, which is a phrase in Latin