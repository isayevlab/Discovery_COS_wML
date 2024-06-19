from jsonargparse import CLI
import pandas as pd
from xgboost import XGBRegressor
from pickle import load as p_load
from typing import Union
import subprocess
import tempfile



def make_descriptor_df(smi_list,descriptor_list,AlvaDescBinPath,n_cpus):
    with tempfile.NamedTemporaryFile(suffix=".smi") as temp_mols , tempfile.NamedTemporaryFile(suffix=".txt") as temp_desc:
        d = pd.DataFrame(smi_list)

        d.to_csv(temp_mols.name,sep="\t",index=None,header=None)
        
        result = subprocess.run([AlvaDescBinPath,
                                f"--input={temp_mols.name}",
                                "--inputtype=SMILES",
                                f"--descriptors={','.join(descriptor_list)}",
                                f"--threads={n_cpus}",
                                f"--output={temp_desc.name}",
                                ], capture_output=True, text=True)

        descriptors = pd.read_csv(temp_desc,na_values='na',sep="\t",dtype='float',header=None)
        return(descriptors)


def DoScreenAlva(InputSmiFilePath: str,
              OutputFilePath:str,
              ModelFilePath:str,
              DescriptorListPath:str,
              AlvaDescBinPath:str,
              TargetSmiColumn:Union[str,int]="smiles",
              OutputColumnPrefix:str="ModelPred",

              num_cpus: int = 2,
              device="cpu",
              sep:str="\t",):

    try:
        TargetSmiColumn = int(TargetSmiColumn)
    except:
        pass
    
    good_desc= pd.read_csv(DescriptorListPath,header=None)[0].tolist()
    
    def screen_df(df_chunk,model,AlvaDescBinPath=AlvaDescBinPath,basename=OutputColumnPrefix):
        df = df_chunk

        if type(TargetSmiColumn)==int:
            smiles_list = df.iloc[:,TargetSmiColumn].tolist()
        else:
            smiles_list = df[TargetSmiColumn].tolist()
     
        X_desc = make_descriptor_df(smiles_list,good_desc,AlvaDescBinPath,num_cpus)
        preds_ar = model.predict(X_desc)
        df_tmp = pd.DataFrame(preds_ar,columns=[basename])
        
        return df_tmp
    
    model =p_load(open(ModelFilePath,"rb"))
    if hasattr(model,"device"):
        model.set_params(n_jobs=num_cpus,device=device)
    else:
        model.set_params(n_jobs=num_cpus)
    
    df = pd.read_csv(InputSmiFilePath,
                    sep=sep,)
    preds_df = screen_df(df_chunk=df,model=model)
   
    out_df = pd.concat([df.reset_index(drop=True),
                        preds_df.reset_index(drop=True)],axis=1)

    if type(TargetSmiColumn)==int:
        header = False
    else:
        header =True
    
    out_df.to_csv(
        OutputFilePath,
        sep=sep,
        index=False,  
        header=header, 
        float_format='%.5f')
    
if __name__ == "__main__":
    CLI(DoScreenAlva)