f = open("/var/lib/pgsql/data/pg_hba.conf","r")
lines = f.readlines()
f.close()

output_lines = []
for line in lines:
    if('#' in lines):
       output_lines.append(line)
    else:   
       output_lines.append("#" + line)
f = open("/var/lib/pgsql/data/pg_hba.conf", "w")
f.write("\n".join(output_lines))
f.close()
