import math
import csv
import glob

# activity = ['work','go_back_home','baby_present','entertainment','smoke','alexa','others','print','check_body_condition']
evaluation_path = '/home/cybercamp2023/git/lab2/data/evaluation/edited/result/'
for i in range (0,13):
    with open(evaluation_path + str(i) +'.csv', 'w') as new:
        realnames = ['model', 'TP', 'FN', 'TN', 'FP', 'ACCURACY',
                 'MCC', 'F1', 'Cohen_kappa', 'SPECIFICITY', 'PRECISION', 'RECALL']
        writer = csv.DictWriter(new, fieldnames=realnames)
        writer.writeheader()
    new.close()



def metric(model,TP, FN,TN,FP,i):
    if ((int(TP + FP))) == 0 or (int((FN + TN)) == 0 ) or (int((FP + TN)) ==0)or (int((TP + FN))==0) :
        pass
    else  :
        metric = {}
        TP = int(TP)
        FN = int(FN)
        FP = int(FP)
        TN = int(TN)
        ACCURACY = float((TP + TN)/(TP + FP + FN + TN))
        PRECISION = float(TP/(TP + FP))
        RECALL = float(TP/(TP + FN))
        if ((PRECISION == 0) or (RECALL == 0)):
            pass
        else:
            F1 = float(2*PRECISION*RECALL/(PRECISION + RECALL))
            MCC = float((TP * TN - FP * FN)/ math.sqrt((TP + FP) * (FN + TN) * (FP + TN) * (TP + FN)))
            SPECIFICITY = float(TN/(TN + FP))
#             metric['TP'] = float(TP/(TP + FN))
#             metric['FN']  = float(FN /(TP + FN))
#             metric['TN'] = float(TN /(TN + FP))
#             metric['FP']  =float(FP /(TN + FP))
            metric['TP'] = float(TP/(TP + FN + TN + FP))
            metric['FN']  = float(FN /(TP + FN + TN + FP))
            metric['TN'] = float(TN /(TP + FN + TN + FP))
            metric['FP']  =float(FP /(TP + FN + TN + FP))
            metric['ACCURACY'] = ACCURACY
            metric['PRECISION'] =PRECISION
            metric['RECALL']= RECALL
            metric['F1'] = F1
            metric['MCC'] = MCC
            metric['Cohen_kappa'] = 2 * (TP * TN - FN * FP) / (TP * FN + TP * FP + 2 * TP * TN + FN^2 + FN * TN + FP^2 + FP * TN)
            metric['SPECIFICITY'] = SPECIFICITY
            metric['model'] = model
            print(metric)
           
            with open(evaluation_path + str(i) + '.csv',  'a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([metric['model'],metric['TP'],metric['FN'],metric['TN'],metric['FP'],metric['ACCURACY'],
                                 metric['MCC'],metric['F1'],metric['Cohen_kappa'],metric['SPECIFICITY'],metric['PRECISION'],metric['RECALL']])
            csvfile.close()
def main():
    data_path = '/home/cybercamp2023/git/lab2/data/evaluation/edited/'
    headers = ['model', 'TP', 'FN', 'TN', 'FP']
    for i in range (0,13):
        with open(data_path + str(i) +'.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=headers)
            for row in reader:
                metric(row['model'],row['TP'],row['FN'],row['TN'],row['FP'],str(i))
        csvfile.close()

main()








