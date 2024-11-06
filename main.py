from pafts import PAFTS

p = PAFTS(
    path="/kaggle/input/testaudio/",
    output_path="/kaggle/working",
)

# Separator
p.separator()

p.run()
