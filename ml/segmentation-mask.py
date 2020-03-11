import json 
import pprint as pp  
import cv2
import numpy as np
import os.path as path
import argparse
import os
import glob

def parse_args():
    parser = argparse.ArgumentParser(description='DeepFashion2 batch processing: photos->masked clothes')
    parser.add_argument('--root_dir', dest='root_dir',
                        default=r"C:\Users\gnc\Desktop\COMP491\DeepFashion2\train\train",
                        help='directory to store input photos', type=str)
    args = parser.parse_args()
    return args


args = parse_args()
for arg in vars(args):
    print('[%s] =' % arg, getattr(args, arg))

img_names = os.listdir("%s/annos" % args.root_dir)
img_ids = [it[0:6] for it in img_names]

for id in img_ids :
    # if (int(id) > 50) : break
    if (int(id) % 100 == 0) :
        print("Processing %s out of %s" % (id, img_ids[-1]))
    dst_path = "%s/masked/%s.jpg" % (args.root_dir, id)
    if path.exists(dst_path) :
        continue

    with open('%s/annos/%s.json' % (args.root_dir, id), 'r') as f:
        seg_data = json.load(f)

    src = cv2.imread('%s/image/%s.jpg' % (args.root_dir, id))
    mask = np.zeros(src.shape, np.uint8) 

    cv2.resize(mask, src.shape[1::-1], interpolation=cv2.INTER_AREA)

    for it, item in seg_data.items():
        if str(it).startswith("item") :
            pts = np.array(item["segmentation"][0], np.int32).reshape((-1,1,2))
            cv2.fillPoly(mask,[pts],(255,255,255), lineType=cv2.LINE_AA)

    dst = cv2.bitwise_and(src, mask)
    dst = cv2.bitwise_or(dst, cv2.bitwise_not(mask))

    cv2.imwrite(dst_path, dst)




        
