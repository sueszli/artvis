from utils import get_current_dir

inputpath = get_current_dir().parent / "data" / "artvis_dump.csv"
outputpath = get_current_dir().parent / "data" / "artvis_cleaned.csv"


with open(inputpath, "r") as i:
    with open(outputpath, "w") as o:
        # turn header to utf-8
        header = "".join([c for c in i.readline() if ord(c) < 128])
        header = header.replace("\n", "")
        o.write(header + "\n")

        numcols = header.count(",") + 1
        for index, line in enumerate(i):
            # drop "\N"
            line = line.replace(",\\N", ",null")

            linearr = line.split(",")
            for i, _ in enumerate(linearr):
                linearr[i] = linearr[i].strip()

                # fix num of quotation marks
                if '"' in linearr[i]:
                    linearr[i] = linearr[i].replace('"', "")
                if "," in linearr[i]:
                    linearr[i] = '"' + linearr[i] + '"'

            # over 10k lines use unquoted delimiters.
            # they can only fixed manually, so we have to drop them.
            debug = False
            if len(linearr) != numcols:
                if debug:
                    print(f"invalid in line {index}: expected {numcols} but got {len(linearr)}")
                    tmpheader = header.split(",")
                    tmpline = linearr
                    while len(tmpheader) < len(tmpline):
                        tmpheader.append("null")
                    while len(tmpline) < len(tmpheader):
                        tmpline.append("null")
                    assert len(tmpheader) == len(tmpline)
                    for i, (a, b) in enumerate(zip(tmpheader, tmpline)):
                        print(f"{i:2d}: {a} -> {b}")
                    print("\n")
                continue

            # check format
            # - linearr[0] is a positive integer
            # - linearr[3] must be "M" or "F"
            # - linearr[4] must be a date with format "YYYY-MM-DD"
            # - linearr[5] must be a date with format "YYYY-MM-DD"
            # - linearr[12] must be a positive integer
            # - linearr[14] must be a positive integer
            # - linearr[17] must be a decimal number
            # - linearr[18] must be a decimal number
            if not linearr[0].isnumeric():
                linearr[0] = "null"
            if linearr[3] not in ["M", "F"]:
                linearr[3] = "null"
            if (len(linearr[4]) != 10) or (linearr[4][4] != "-") or (linearr[4][7] != "-"):
                linearr[4] = "null"
            if (len(linearr[5]) != 10) or (linearr[5][4] != "-") or (linearr[5][7] != "-"):
                linearr[5] = "null"
            if not linearr[12].isnumeric():
                linearr[12] = "null"
            if not linearr[14].isnumeric():
                linearr[14] = "null"
            try:
                float(linearr[17])
            except:
                linearr[17] = "null"
            try:
                float(linearr[18])
            except:
                linearr[18] = "null"

            line = ",".join(linearr)
            o.write(line + "\n")
