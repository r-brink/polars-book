from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .snippet1 import q1 as q1
from .snippet1 import q1_plan as q1_plan
from .snippet1 import q1_opt_plan as q1_opt_plan
from .snippet2 import q2_plan as q2_plan
from .snippet2 import q2 as q2
from .snippet3 import q3 as q3
from .snippet3 import q3_schema as q3_schema
from .snippet4 import q4 as q4
from .snippet5 import q5 as q5

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/predicate_pushdown")

for n, x in enumerate([q1, q2]):
    x.show_graph(optimized=False, show=False, output_path=f"{path}/graph{n + 1}.png")
    x.show_graph(optimized=True, show=False, output_path=f"{path}/graph{n + 1}-optimized.png")

df1 = q1.fetch(int(1e7))
df2 = q2.fetch(int(1e7))
df3 = q3
df4 = q4
df5 = q5
for n, x in enumerate([df1, df2, df3, q3_schema, df4, df5, q1_plan, q2_plan, q1_opt_plan]):
    with open(f"{path}/output{n + 1}.txt", "w") as f:
        f.write(f"{x}\n")
