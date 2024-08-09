# Data for “Discovery of Crystallizable Organic Semiconductors with Machine Learning”

## install required packages

```bash
pip install ./requirements.txt
```
Note: You have to have a licensed and installed version of AlvaDesc software to calculate the descriptors


## File’s description
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

The script `Predict.py` runs one of those models, calculates the set of appropriate descriptors specified in `SITable_Descriptors_dHm_list.csv` (or `SITable_Descriptors_Tm_list.csv`)
and makes predictions for a set of input molecules.

An example of input file is `Test_mols.csv`, an example of the output is `Test_mols_pred.csv`

Bash script with an example of specification of input parameters is provided -- `run_Predict.sh`.

If you use this data, please cite the following work:

>**Discovery of Crystallizable Organic Semiconductors with Machine Learning**
>Holly M. Johnson, Filipp Gusev, Jordan T. Dull, Yejoon Seo, Rodney D. Priestley, Olexandr Isayev, and Barry P. Rand
>*Journal of the American Chemical Society* **2024** *146* (31), 21583-21590
>DOI: [10.1021/jacs.4c05245](https://pubs.acs.org/doi/10.1021/jacs.4c05245)
