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

HOST = "localhost"
PORT = 8888
delay = 0.2
enddelay = 0.5
tn = telnetlib.Telnet(HOST, PORT)
while True:
    try:
        tn.write("cl_clanid 39440807\n".encode('utf-8')) #thomhooks
        time.sleep(enddelay)
        tn.write("cl_clanid 39440831\n".encode('utf-8')) #thomhook
        time.sleep(delay)
        tn.write("cl_clanid 39440833\n".encode('utf-8')) #thomhoo
        time.sleep(delay)
        tn.write("cl_clanid 39440841\n".encode('utf-8')) #thomho
        time.sleep(delay)
        tn.write("cl_clanid 39440852\n".encode('utf-8')) #thomh
        time.sleep(delay)
        tn.write("cl_clanid 39440865\n".encode('utf-8')) #thom
        time.sleep(delay)
        tn.write("cl_clanid 39440870\n".encode('utf-8')) #tho
        time.sleep(delay)
        tn.write("cl_clanid 39440873\n".encode('utf-8')) #th
        time.sleep(delay)
        tn.write("cl_clanid 39440880\n".encode('utf-8')) #t
        time.sleep(delay)
        tn.write("cl_clanid 0\n".encode('utf-8'))        #blank
        time.sleep(delay)
        tn.write("cl_clanid 39440880\n".encode('utf-8')) #t
        time.sleep(delay)
        tn.write("cl_clanid 39440873\n".encode('utf-8')) #th
        time.sleep(delay)
        tn.write("cl_clanid 39440870\n".encode('utf-8')) #tho
        time.sleep(delay)
        tn.write("cl_clanid 39440865\n".encode('utf-8')) #thom
        time.sleep(delay)
        tn.write("cl_clanid 39440852\n".encode('utf-8')) #thomh
        time.sleep(delay)
        tn.write("cl_clanid 39440841\n".encode('utf-8')) #thomho
        time.sleep(delay)
        tn.write("cl_clanid 39440833\n".encode('utf-8')) #thomhoo
        time.sleep(delay)
        tn.write("cl_clanid 39440831\n".encode('utf-8')) #thomhook
        time.sleep(delay)
        
    except:
        tn.write("cl_clanid 0\n".encode('utf-8'))
        break