from glob import glob
import json

for notebook_file in glob("**/*.ipynb", recursive=True):
    with open(notebook_file, "r", encoding="utf-8") as fh:
        notebook_data = json.load(fh)
    for cell in notebook_data.get("cells", []):
        if cell.get("cell_type") != "markdown":
            orig_lines = json.dumps(cell.get("outputs", []), ensure_ascii=False, indent=1).count("\n")
            cell["outputs"] = [""] * (orig_lines - 1) if orig_lines >= 2 else []
            cell["execution_count"] = None
    with open(notebook_file, "w", encoding="utf-8") as fh:
        json.dump(notebook_data, fh, ensure_ascii=False, indent=1)
