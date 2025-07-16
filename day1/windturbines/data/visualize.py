import os, glob
os.chdir(os.path.dirname(__file__))
outdir1 = "../vistemp"
outdir2 = "../vis"
os.system(f"rm -rf {outdir1}/; mkdir {outdir1}")
os.system(f"rm -rf {outdir2}/; mkdir {outdir2}")
for fname in sorted(glob.glob("../../../day1/laserstrike/data/secret/group3/group3/*.in")):
    eds = []
    with open(fname) as f:
        n = int(f.readline())
        for _ in range(n-1):
            a, b = map(int, f.readline().split())
            eds.append((a, b))

    basename = os.path.basename(fname)[:-3]
    outfile = f"{outdir1}/{basename}.gv"
    outsvg = f"{outdir2}/{basename}.svg"
    with open(outfile, "w") as f:
        f.write("graph G {\n")
        for a,b in eds:
            f.write(f"  {a} -- {b};\n")
        f.write("}\n")

    print("Generating", outsvg)
    os.system(f"neato {outfile} -T svg > {outsvg}")
os.system(f"rm -rf {outdir1}/")
