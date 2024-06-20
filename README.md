# Data for "Discovery of Crystallizable Organic Semiconductors with Machine Learning"

## install required packages

```bash
pip install ./requirements.txt
```
Note: You have to have a licenced and installed version of AlvaDesc software to calculate the descriptors


## File's description
```bash
├── data
│   ├── Dataset_dHm.csv
│   └── Dataset_Tm.csv
├── descriptors
│   ├── SITable_Descriptors_dHm_list.csv
│   └── SITable_Descriptors_Tm_list.csv
├── models
│   ├── Model_dHm.pkl
│   └── Model_Tm.pkl
├── Predict.py
├── README.md
├── requirements.txt
├── run_Predict.sh
└── test
    ├── Test_mols.csv
    └── Test_mols_pred.csv
```
The training sets for dHm and Tm are in `Dataset_dHm.csv` and `Dataset_Tm.csv`. The pretrained models serialized in pickle format are `Model_dHm.pkl` and `Model_Tm.pkl`.

The script `Predict.py` runs one of those models, calculates set of appropriate descriptors specified in `SITable_Descriptors_dHm_list.csv` (or `SITable_Descriptors_Tm_list.csv`)
and makes predictions for set of input moecules.


Example of input file is `Test_mols.csv`, example of output is `Test_mols_pred.csv`

g
Bash script wiht example of specificaton of input parameters is provided -- `run_Predict.sh`.

If you use this data, please cite the following work:
> Johnson, H. M.; Gusev, F.; Dull, J. T.; Seo, Y.; Priestley, R. D.; Isayev, O.; Rand, B. P. Discovery of Crystallizable Organic Semiconductors with Machine Learning. April 17, 2024. https://doi.org/10.26434/chemrxiv-2024-hkszt.
