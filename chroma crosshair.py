
##################################################################################################################################
###                                                                                                                            ###
###     :::::::::::   :::    :::    ::::::::      :::   :::     :::    :::    ::::::::     ::::::::    :::    :::   ::::::::   ###
###        :+:       :+:    :+:   :+:    :+:    :+:+: :+:+:    :+:    :+:   :+:    :+:   :+:    :+:   :+:   :+:   :+:    :+:   ###
###       +:+       +:+    +:+   +:+    +:+   +:+ +:+:+ +:+   +:+    +:+   +:+    +:+   +:+    +:+   +:+  +:+    +:+           ###
###      +#+       +#++:++#++   +#+    +:+   +#+  +:+  +#+   +#++:++#++   +#+    +:+   +#+    +:+   +#++:++     +#++:++#++     ###
###     +#+       +#+    +#+   +#+    +#+   +#+       +#+   +#+    +#+   +#+    +#+   +#+    +#+   +#+  +#+           +#+      ###
###    #+#       #+#    #+#   #+#    #+#   #+#       #+#   #+#    #+#   #+#    #+#   #+#    #+#   #+#   #+#   #+#    #+#       ###
###   ###       ###    ###    ########    ###       ###   ###    ###    ########     ########    ###    ###   ########         ###
###                                                                                                                            ###
##################################################################################################################################

import telnetlib
import time
import colorsys

HOST = "localhost"
PORT = 8888
delay = 0.05

tn = telnetlib.Telnet(HOST, PORT)

with open(__file__) as f:
    for x in f.readlines()[:13]:
        print(x.strip())
        tn.write(('echo "' + x.strip() + '"\n').encode('utf-8'))

tn.write("cl_crosshaircolor 5\n".encode('utf-8'))

index = 0
while True:
    r, g, b = tuple(round(i * 255) for i in colorsys.hsv_to_rgb(index/360,1,1))
    tn.write("cl_crosshaircolor_r {}\n".format(r).encode('utf-8'))
    tn.write("cl_crosshaircolor_g {}\n".format(g).encode('utf-8'))
    tn.write("cl_crosshaircolor_b {}\n".format(b).encode('utf-8'))
    index += 1
    if index == 360:
        index = 0
    time.sleep(delay)
