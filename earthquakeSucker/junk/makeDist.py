

OBStr = "{"
CBStr = "}"

REDLIST =     [0X00, 0XFF, 0XFF, 0XFF, 0X99, 0X00, 0X00, 0X00, 0X00, 0X00, 0X99, 0XFF, 0XFF]
GREENLIST =   [0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X99, 0XFF, 0XFF, 0XFF, 0XFF, 0X99, 0XFF]
BLUELIST =    [0X00, 0X00, 0X99, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0X99, 0X00, 0X00, 0X00, 0XFF]
BREDLIST =    [0XFF, 0X00, 0X00, 0X00, 0X99, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0X99, 0X00, 0X00]
BGREENLIST =  [0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0X99, 0X00, 0X00, 0X00, 0X00, 0X99, 0X00]
BBLUELIST =   [0XFF, 0XFF, 0X99, 0X00, 0X00, 0X00, 0X00, 0X00, 0X99, 0XFF, 0XFF, 0XFF, 0X00]
# FDOut = None
FDOut = open("../styleChunk.css", "w")

COLOR = 0
BACKGROUND = 1
goodList = [0x00, 0x99, 0xff]
indexNum = 0
for Rgb in range(0x00, 0x100, 0x33):
	for rGb in range(0x00, 0x100, 0x33):
		for rgB in range(0x00, 0x100, 0x33):
			if (Rgb in goodList) and (rGb in goodList) and (rgB in goodList):
				colorStr = f"""{Rgb:02x}{rGb:02x}{rgB:02x}"""
				notColorStr = f"""{Rgb ^ 0xff:02x}{rGb ^ 0xff:02x}{rgB ^ 0xff:02x}"""
				outStr = f"""
.n{indexNum:02x}
{OBStr}
	color: #{notColorStr};
	background-color: #{colorStr};
{CBStr}

"""
				print(outStr)
				FDOut.write(outStr)
				FDOut.flush()
				indexNum += 1

FDOut.flush()
FDOut.close()

