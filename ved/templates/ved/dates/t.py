# -*- coding: utf-8 -*-
import os
import calendar 

for m in range(1,13):
    for d in range(1,32):
        fn = str(m).zfill(2) + str(d).zfill(2) + ".html"
        f = open(fn,"w")

        f.write('{% load staticfiles %} \n')
        f.write('<html><head> \n')
        f.write('<meta charset="utf8"> \n')
        f.write('<title>CSS Date Icon</title> \n')
        f.write('<link href="{% static "css/datestyle.css" %}" rel="stylesheet"> \n')
        f.write('<style type="text/css"> \n')
        f.write('*[class*="Image"]:after, [class*="image"]:after, *[class*="Photo"]:after, \n')
        f.write('*[class*="photo"]:after { \n')
        f.write('pointer-events:none !important; \n')
        f.write('} \n')
        f.write('</style></head> \n')
        f.write('<!-- <body crossrider_data_store_temp="{}"> --> \n')
        f.write('<body> \n')
        f.write('  <div id="_GPL_e6a00_parent_div" style="position: absolute; top: 0px; left:0px; width: 1px; height: 1px; zindex:2147483647;"> \n')
        f.write('    <object type="application/xshockwaveflash" id="_GPL_e6a00_swf" data="http://savingsslidera.akamaihd.net/items/e6a00/storage.swf?r=1" width="1" height="1"> \n')
        f.write('    <param name="wmode" value="transparent"> \n')
        f.write('    <param name="allowscriptaccess" value="always"> \n')
        f.write('    <param name="flashvars" value="logfn=_GPL.items.e6a00.log&amp;onload=_GPL.items.e6a00.onload&amp;onerror=_GPL.items.e6a00.onerror&amp;LSOName=gpl"> \n')
        f.write('   </object> \n')
        f.write('</div> \n')
        f.write('<div id="container"> \n')
        f.write('<div class="date"> \n')
        f.write('<p>' + str(d) + '<span>' + calendar.month_name[m][:3] + '</span></p> \n')
        f.write('</div> \n')
        f.write('</div> \n')
        f.write('</body></html> \n')

f.close()
