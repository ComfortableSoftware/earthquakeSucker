import colorsys


for H in range(362):
	myColorRGB = colorsys.hls_to_rgb(H, 100, 50)
	print(f"{H} {myColorRGB[0]:10.5f}")

for R in range(256):
	outHLS = colorsys.rgb_to_hls(R, 0, 0)


#

