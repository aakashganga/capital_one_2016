import os

dir = '/Users/yizhisun/Desktop/capitol_one_2016/validation_output'
outputFile = '/Users/yizhisun/Desktop/capitol_one_2016/output_validation_transformed.csv'
target = open(outputFile, 'w')
files = os.listdir(dir)

firstLine = 'AUTH_ID, ACCT_ID_TOKEN, FRD_IND, ACCT_ACTVN_DT_YEAR, ACCT_ACTVN_DT_MONTH, ACCT_ACTVN_DT_DAY, ACCT_AVL_CASH_BEFORE_AMT, ACCT_AVL_MONEY_BEFORE_AMT, ACCT_CL_AMT, ACCT_CURR_BAL, ACCT_MULTICARD_IND, ACCT_OPEN_DT_YEAR, ACCT_OPEN_DT_MONTH, ACCT_OPEN_DT_DAY, ACCT_PROD_CD, ACCT_TYPE_CD, ADR_VFCN_FRMT_CD, ADR_VFCN_RESPNS_CD, APPRD_AUTHZN_CNT, APPRD_CASH_AUTHZN_CNT, ARQC_RSLT_CD, AUTHZN_ACCT_STAT_CD, AUTHZN_AMT, AUTHZN_CATG_CD, AUTHZN_CHAR_CD, AUTHZN_OPSET_ID, AUTHZN_ORIG_SRC_ID, AUTHZN_OUTSTD_AMT, AUTHZN_OUTSTD_CASH_AMT, AUTHZN_RQST_PROC_CD, AUTHZN_RQST_PROC_DT_YEAR, AUTHZN_RQST_PROC_DT_MONTH, AUTHZN_RQST_PROC_DT_DAY, AUTHZN_RQST_PROC_TM, AUTHZN_RQST_TYPE_CD, AUTHZN_TRMNL_PIN_CAPBLT_NUM, AVG_DLY_AUTHZN_AMT, CARD_VFCN_2_RESPNS_CD, CARD_VFCN_2_VLDTN_DUR, CARD_VFCN_MSMT_REAS_CD, CARD_VFCN_PRESNC_CD, CARD_VFCN_RESPNS_CD, CARD_VFCN2_VLDTN_CD, CDHLDR_PRES_CD, CRCY_CNVRSN_RT, ELCTR_CMRC_IND_CD, HOME_PHN_NUM_CHNG_DUR, HOTEL_STAY_CAR_RENTL_DUR, LAST_ADR_CHNG_DUR, LAST_PLSTC_RQST_REAS_CD, MRCH_CATG_CD, MRCH_CNTRY_CD, NEW_USER_ADDED_DUR, PHN_CHNG_SNC_APPN_IND, PIN_BLK_CD, PIN_VLDTN_IND, PLSTC_ACTVN_DT_YEAR, PLSTC_ACTVN_DT_MONTH, PLSTC_ACTVN_DT_DAY, PLSTC_ACTVN_REQD_IND, PLSTC_FRST_USE_TS_YEAR, PLSTC_FRST_USE_TS_MONTH, PLSTC_FRST_USE_TS_DAY, PLSTC_FRST_USE_TS_HOUR, PLSTC_ISU_DUR, PLSTC_PREV_CURR_CD, PLSTC_RQST_TS_YEAR, PLSTC_RQST_TS_MONTH, PLSTC_RQST_TS_DAY, PLSTC_RQST_TS_HOUR, POS_COND_CD, POS_ENTRY_MTHD_CD, RCURG_AUTHZN_IND, RVRSL_IND, SENDR_RSIDNL_CNTRY_CD, SRC_CRCY_CD, SRC_CRCY_DCML_PSN_NUM, TRMNL_ATTNDNC_CD, TRMNL_CAPBLT_CD, TRMNL_CLASFN_CD, TRMNL_ID, TRMNL_PIN_CAPBLT_CD, DISTANCE_FROM_HOME'
target.write(firstLine)
target.write("\n")


for file in files:
    with open(os.path.join(dir, file)) as f:
        i = 0
        for line in f:
            if i > 0:
                features = line.split(",")
                newLine = ""
                j = 0
                for feature in features:
                    if j in (3, 9, 26, 50):
                        if feature != '':
                            transformedFeature = feature.replace('-', ',')
                        else:
                            transformedFeature = ',,'
                        newLine = newLine + transformedFeature + ","
                    elif j in (52, 55):
                        if feature != '':
                            subFeatures = feature.split(' ')
                            transformedFeature = subFeatures[0].replace('-', ',')
                            transformedFeature += "," + subFeatures[1][:2]
                        else:
                            transformedFeature = ',,,'
                        newLine = newLine + transformedFeature + ","
                    elif j == 27:
                        if feature != '':
                            transformedFeature = feature[:2]
                        else:
                            transformedFeature = ''
                        newLine = newLine + transformedFeature + ","
                    else:
                        newLine = newLine + feature + ","
                    j += 1

                target.write(newLine[:-1])
            i += 1
        print(i.__str__())
target.close()
