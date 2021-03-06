import SimpleITK as sitk
import numpy as np
import os,glob
import sys
import argparse
parser = argparse.ArgumentParser()
parser.description='please enter two parameters a and b ...'
parser.add_argument("-o", "--output_path", help="path to output nii files",  type=str, default='/mnt/data6/NCP_CTs/NCP_controls')
parser.add_argument("-i", "--input_path", help="path to input dicom files",  type=str,
                    default='/home/cwx/extra/NCP_CTs/NCP_control/control')
args = parser.parse_args()

output_path=args.output_path
os.makedirs(output_path,exist_ok=True)
#input_path='/home/cwx/extra/NCP_ill'
#input_c='/home/cwx/extra/new_control/control/control'
#input_c='/home/cwx/extra/3rd/control/control '
input_path=args.input_path
for i in range(1,14):
    #
    path=input_path+str(i)
    #path=input_path
    all_id = os.listdir(path)
    for id in all_id:
        all_phase=os.listdir(os.path.join(path,id))
        for phase in all_phase:
            inner=os.listdir(os.path.join(path,id,phase))
            for itemsinnner in inner:
                if itemsinnner == "DICOMDIR" or itemsinnner == 'LOCKFILE' or itemsinnner == 'VERSION':
                    continue
                iinner=os.listdir(os.path.join(path,id,phase,itemsinnner))
                for iinn_item in iinner:
                    if iinn_item=='VERSION':
                        continue
                    #cid = int(id) + (i-1) * 20
                    output_name = os.path.join(output_path, 'c'+str(i)+'_'+str(id) + '_' + phase + '.nii')
                    #output_name = os.path.join(output_path, str(id) + '_' + phase + '.nii')
                    print(output_name)
                    case_path=os.path.join(path,id,phase,itemsinnner,iinn_item)
                    reader = sitk.ImageSeriesReader()
                    dicom_names = reader.GetGDCMSeriesFileNames(case_path)
                    reader.SetFileNames(dicom_names)
                    image = reader.Execute()
                    if image.GetSize()[-1]<=10:
                        continue
                    sitk.WriteImage(image,output_name)




