

str = 'date|g1_o|g1_h|g1_l|g1_c|g2|g2_CUMVOL~07-12-2012 09:15|5934.0000|5945.5000|5934.0000|5938.6500|1749606|1749606~07-12-2012 09:16|5939.1000|5941.8000|5936.3500|5941.8000|1064557|2814163'
records = str.split('~')
for record in records:
    elements = record.split('|')
    print elements
