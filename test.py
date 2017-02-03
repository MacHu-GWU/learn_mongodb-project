from pathlib_mate import Path

n = 0
for p in Path(r"D:\耶鲁大学公开课 - 博弈论").select_by_ext(".rmvb"):
    n += 1
    new_fname = str(n).zfill(2)
    p.moveto(new_fname=new_fname)