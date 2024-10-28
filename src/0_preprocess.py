from utils import get_current_dir

inputpath = get_current_dir().parent / "data" / "artvis_dump.csv"
outputpath = get_current_dir().parent / "data" / "artvis_cleaned_v1.csv"

line_count = 0
err_count = 0


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

                # either drop or keep a single quote
                if '"' in linearr[i]:
                    linearr[i] = linearr[i].replace('"', "")
                if "," in linearr[i]:
                    linearr[i] = '"' + linearr[i] + '"'

            # check num of cols
            if len(linearr) != numcols:
                print(f"invalid @ index {index}: expected {numcols} but got {len(linearr)}")
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
                err_count += 1
                continue

            line = ",".join(linearr)
            o.write(line + "\n")
            line_count += 1


# over 10k lines use unquoted delimiters.
# they can only be fixed manually, so we have to drop them.
print(f"errors: {err_count}/{line_count}")
