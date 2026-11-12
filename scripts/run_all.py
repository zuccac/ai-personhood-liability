"""Runs every script and writes the figure. Takes a few minutes (Model 1 calibration)."""
import runpy, pathlib, os
os.chdir(pathlib.Path(__file__).parent)
pathlib.Path("../output").mkdir(exist_ok=True)
for s in ["model1_calibration.py", "model1_entity_size.py", "section3_retention_and_aggregation.py",
          "section4_vasicek_tail.py", "section4_second_best.py", "section6_deployment.py", "figure1_retention.py"]:
    print(f"\n=== {s} ===")
    runpy.run_path(s, run_name="__main__")
