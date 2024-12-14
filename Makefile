# define variables
PYTHON = python
QUARTO = quarto

TRAINING_SET = data/processed/training_set.csv
TEST_SET = data/processed/test_set.csv
DATA_CLEANED = data/processed/cleaned_wine_quality.csv
DATA_RAW = data/raw/wine_quality.csv
RESULTS = results/tables/model_results.csv
PLOTS = results/figures/dist_wine_scores.png results/figures/red_vs_white_all_features.png results/figures/total_vs_free_sulfur_dioxide.png results/figures/feature_corrs.png results/figures/density_red_vs_white.png results/figures/dist_wine_scores_by_feature.png
REFERENCES = report/references.bib
REPORT_HTML = reports/wine_quality_regressor_report.html
REPORT_PDF = reports/wine_quality_regressor_report.pdf

.PHONY: all clean

all: $(REPORT_HTML) $(REPORT_PDF)

# script1: download data - save raw data
$(DATA_RAW): ./scripts/data_download.py
	$(PYTHON) ./scripts/data_download.py \
		--id=186 \
		--raw_data_out=./data/raw

# script2: raw data validation - save cleaned data
$(DATA_CLEANED): ./scripts/validate_raw_data.py $(DATA_RAW)
	$(PYTHON) ./scripts/validate_raw_data.py \
		--input_path $(DATA_RAW) \
		--processed_data_path "./data/processed"

#script3: read data - split cleaned data into training and test sets
./data/processed/split_done: ./scripts/read_data.py $(DATA_CLEANED)
	$(PYTHON) ./scripts/read_data.py \
		$(DATA_CLEANED) \
		./data/processed \
		--seed=522 \
		--test_size=0.2
	touch ./data/processed/split_done

$(TRAINING_SET) $(TEST_SET): ./data/processed/split_done

# script4: EDA - save plots to .png files
$(PLOTS): ./scripts/eda.py $(TRAINING_SET)
	$(PYTHON) ./scripts/eda.py \
		$(TRAINING_SET) \
		./results/figures

# script5: model and result - save model information and result to .csv
$(RESULTS): ./scripts/model_and_results.py $(TRAINING_SET) $(TEST_SET)
	$(PYTHON) ./scripts/model_and_results.py \
		--training_data $(TRAINING_SET) \
		--test_data $(TEST_SET) \
		--results_to ./results/tables/ \
		--seed=522

# render reports using Quarto
$(REPORT_HTML): $(PLOTS) $(RESULTS) $(REFERENCES) ./reports/wine_quality_regressor_report.qmd
	$(QUARTO) render ./reports/wine_quality_regressor_report.qmd --to html
$(REPORT_PDF): $(PLOTS) $(RESULTS) $(REFERENCES) ./reports/wine_quality_regressor_report.qmd
	$(QUARTO) render ./reports/wine_quality_regressor_report.qmd --to pdf

# clean up analysis and remove all files generated
clean:
	rm -f $(DATA_RAW) $(DATA_CLEANED) $(TRAINING_SET) $(TEST_SET) $(RESULTS) $(PLOTS) $(REPORT_HTML) $(REPORT_PDF)