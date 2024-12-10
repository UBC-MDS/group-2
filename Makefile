# Makefile for smarter data analysis pipeline
# Replaces runall.sh functionality using GNU Make

# Define variables
PYTHON = python
QUARTO = quarto

TRAINING_SET = data/processed/training_set.csv
TEST_SET = data/processed/test_set.csv
DATA_RAW = data/raw/wine_quality.csv
DATA_CLEANED = data/processed/cleaned_wine_quality.csv
RESULTS = results/tables/model_results.csv
PLOTS = results/figures/dist_wine_scores.png results/figures/red_vs_white_all_features.png results/figures/total_vs_free_sulfur_dioxide.png results/figures/feature_corrs.png results/figures/density_red_vs_white.png results/figures/dist_wine_scores_by_feature.png
REPORT_HTML = reports/wine_quality_regressor_report.html
REPORT_PDF = reports/wine_quality_regressor_report.pdf

# Pattern rules
# results/%.dat: data/%.txt
# 	$(PYTHON) scripts/wordcount.py --input_file=$< --output_file=$@

# results/figures/%.png: results/%.dat
# 	$(PYTHON) scripts/plotcount.py --input_file=$< --output_file=$@

# results/figures/sierra.png : scripts/plotcount.py results/sierra.dat
#     python scripts/plotcount.py \
#         --input_file=results/sierra.dat \
#         --output_file=results/figure/sierra.png

# Save validated data
$(DATA_CLEANED): $(DATA_RAW)
	$(PYTHON) scripts/validate_raw_data.py

# Create training and test sets
$(TRAINING_SET): $(DATA_CLEANED)
	$(PYTHON) scripts/read_data.py
$(TEST_SET): $(DATA_CLEANED)
	$(PYTHON) scripts/read_data.py

# Create plots from EDA
$(PLOTS): $(TRAINING_SET)
	$(PYTHON) scripts/eda.py

# Create table containing model information and results
$(RESULTS): $(TRAINING_SET) $(TEST_SET)
	$(PYTHON) scripts/model_and_results.py

# Create html/pdf reports
$(REPORT_HTML): $(PLOTS) reports/wine_quality_regressor_report.qmd
	$(QUARTO) render reports/wine_quality_regressor_report.qmd --to html
$(REPORT_PDF): $(PLOTS) reports/wine_quality_regressor_report.qmd
	$(QUARTO) render reports/wine_quality_regressor_report.qmd --to pdf

# Targets
.PHONY: all clean

all: $(DATA_CLEANED) $(TRAINING_SET) $(TEST_SET) $(RESULTS) $(PLOTS) $(REPORT_HTML) $(REPORT_PDF)

clean:
	rm -f $(DATA_CLEANED) $(TRAINING_SET) $(TEST_SET) $(RESULTS) $(PLOTS) $(REPORT_HTML) $(REPORT_PDF)
