s = 'date|o|h|l|c|e|f~07-12-2012 09:15|5934.0000|5945.5000|5934.0000|5938.6500|1749606|1749606~07-12-2012 09:16|5939.1000|5941.8000|5936.3500|5941.8000|1064557|2814163'

rows = s.split ('~')
d = {}
keys = rows [0].split ('|')
for key in keys: d [key] = []
for row in rows [1:]:
    for idx, value in enumerate (row.split ('|') ):
        d [keys [idx] ].append (value)

print (d)