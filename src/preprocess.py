from pathlib import Path
from utils import get_current_dir

inputpath = get_current_dir().parent / "data" / "artvis_dump.csv"
outputpath = get_current_dir().parent / "data" / "artvis_cleaned.csv"


with open(inputpath, "r") as i:
    with open(outputpath, "w") as o:
        header = i.readline()
        o.write(header)  # keep as is
        
        numcols = header.count(",") + 1
        for index, line in enumerate(i):

            # replace "\N" with "null"
            line = line.replace(",\\N", ",null")

            line = line.split(",")
            for i, item in enumerate(line):
                line[i] = item.strip()

                # either drop or keep a single quote
                if '"' in item and "," in item:
                    line[i] = '"' + item.replace('"', "") + '"'
                elif '"' in item:
                    line[i] = item.replace('"', "")


            # validate col count
            # if len(line) != numcols:
            #     print(f"invalid: {line}\n")

            # # validate gender
            # if line[3].capitalize() not in ["M", "F"]:
            #     line[3] = "null"

            # # validate dates
            # line[4] = line[4].replace('"', "")
            # if not (line[4].count("-") == 2) and not (line[4] == "null"):
            #     line[4] = "null"
            # line[5] = line[5].replace('"', "")
            # if not (line[5].count("-") == 2) and not (line[5] == "null"):
            #     line[5] = "null"
        
            line = ",".join(line)
            o.write(line)
