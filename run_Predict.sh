python ./Predict.py \
        "./Test_mols.csv" \
        "./Test_mols_pred.csv" \
        "./Model_Tm.pkl" \
        "./SITable_Descriptors_Tm_list.csv" \
        "/data/apps/alvaDesc_Linux_64_v2_0_12/usr/bin/alvaDescCLI" \
        --TargetSmiColumn "SMILES_STD" \
        --num_cpus 5 \
        --sep ","\