import os
from pafts import PAFTS


p = PAFTS(
    path="/kaggle/input/testaudio/",
    output_path="/kaggle/working",
    # hf_token=str(os.getenv("HF_TOKEN")),
)

# Separator
p.separator()

# p.run()
