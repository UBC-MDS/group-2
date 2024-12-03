python scripts/generate_figures.py --input_dir="data/00030067-eng.csv"     --out_dir="results"
quarto render reports/qmd_example.qmd --to html
quarto render reports/qmd_example.qmd --to pdf
python scripts/generate_figures.py --input_dir="data/00030067-eng.csv"     --out_dir="results"
quarto render reports/qmd_example.qmd --to html
quarto render reports/qmd_example.qmd --to pdf
quarto render reports/wine_quality_regressor_report.qmd --to html
quarto render reports/wine_quality_regressor_report.qmd --to pdf
