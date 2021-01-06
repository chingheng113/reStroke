library(tableone)
data=read.csv("cluster_result.csv", header = T)
data$Sex=as.factor(data$Sex)
data$HTN=as.factor(data$HTN)
data$DM=as.factor(data$DM)
data$Dyslipidemia=as.factor(data$Dyslipidemia)
data$AF=as.factor(data$AF)
data$CVA_Hx=as.factor(data$CVA_Hx)
data$CT_Old_Lesion=as.factor(data$CT_Old_Lesion)
data$Smoking=as.factor(data$Smoking)
data$AntiPLT=as.factor(data$AntiPLT)
data$Adm_AntiCO=as.factor(data$Adm_AntiCO)
data$Adm_AntiTH=as.factor(data$Adm_AntiTH)
data$Dis_Out_Deterioration=as.factor(data$Dis_Out_Deterioration)
data$Dis_11_records=as.factor(data$Dis_11_records)
data$Adm_Pneumo0ia=as.factor(data$Adm_Pneumo0ia)
data$Adm_UTD=as.factor(data$Adm_UTD)
data$Adm_NG_feedi0g=as.factor(data$Adm_NG_feedi0g)
data$Adm_UIC=as.factor(data$Adm_UIC)
data$Marriage=as.factor(data$Marriage)
data$Sleep=as.factor(data$Sleep)
data$CT_0ew_Lesio0=as.factor(data$CT_0ew_Lesio0)
data$Alcohol=as.factor(data$Alcohol)
data$Adm_AF_0otEKG=as.factor(data$Adm_AF_0otEKG)
data$EKG_AF=as.factor(data$EKG_AF)
data$BUN.Cr=as.factor(data$BUN.Cr)
data$umap_label=as.factor(data$umap_label)
data$reStroke=as.factor(data$reStroke)

target_data=data[, -c(1, 64)]
target_data=target_data[-c(which(target_data$umap_label==-1)), ]


factorVars = c('Sex', 'HTN', 'DM', 'Dyslipidemia', 'AF', 'CVA_Hx', 'CT_Old_Lesion', 'Smoking', 
               'AntiPLT', 'Adm_AntiCO', 'Adm_AntiTH', 'Dis_Out_Deterioration',
               'Dis_11_records', 'Adm_Pneumo0ia', 'Adm_UTD', 'Adm_NG_feedi0g', 'Adm_UIC',
               'Marriage', 'Sleep', 'CT_0ew_Lesio0', 'Alcohol', 'Adm_AF_0otEKG', 'EKG_AF',
               'BUN.Cr', 'reStroke', 'umap_label')

#dput(names(target_data))
vars = c("Sex", "Age", "HTN", "DM", "Dyslipidemia", "AF", "CVA_Hx", 
         "CT_Old_Lesion", "Smoking", "WBC", "Segment", "Lymphocyte", "Hb", 
         "Hct", "PLT", "CHOL", "TG", "LDL", "HDL", "Hb1", "AST", "ALT", 
         "Cr", "Na", "K", "Temperature", "PR", "RR", "SBP", "DBP", "GCS", 
         "NIHSS_Wd", "BI_Wd", "MRS_Wd", "AntiPLT", "Adm_AntiCO", 
         "Adm_AntiTH", "Dis_Out_Deterioration", "Dis_11_records", "Drug.Quantity", 
         "Outpatient_times", "Admission_times", "Before_11_LOS", "Adm_Pneumo0ia", 
         "Adm_UTD", "Adm_NG_feedi0g", "Adm_UIC", "LOS", "Marriage", "Sleep", 
         "CT_0ew_Lesio0", "Alcohol", "Adm_AF_0otEKG", "EKG_AF", "BU0.Cr.Ratio", 
         "BUN.Cr", "Glucose", "NIHSS_Dis", "BI_Dis", "MRS_Dis", "reStroke")

tableOne = CreateTableOne(vars = vars, strata = "umap_label", data = target_data, factorVars = factorVars)
table1 = print(tableOne, smd = T)
write.csv(table1, "table1.csv")



#summary(tableOne$ContTable)
#summary(tableOne$CatTable)
