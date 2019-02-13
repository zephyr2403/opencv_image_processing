import cv2
import numpy as np 

featureImage = cv2.imread('/home/dragonbreath/Music/target.jpg',0)
image = cv2.imread('/home/dragonbreath/Music/image.jpg',0)

featureImage = cv2.resize(featureImage,(800,800))
image = cv2.resize(image,(800,800))

#########
###ORB###
#########
'''
orb = cv2.ORB_create()
keypoints1,descriptor1=orb.detectAndCompute(featureImage,mask=None)
keypoints2,descriptor2=orb.detectAndCompute(image,mask=None)

matching object
bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
matches = bf.match(descriptor1,descriptor2)

matches = sorted(matches,key=lambda x:x.distance)

'''

'''
############
####SIFT####
############
#SCALE INVARIENT FEATURE TRANSFORM

sift = cv2.xfeatures2d.SIFT_create()
keypoints1,descriptor1=sift.detectAndCompute(featureImage)
keypoints2,descriptor2=sift.detectAndCompute(image)

bf = cv2.BFMatcher()
matches = bf.knnMatch(descriptor1,descriptor2,key=2)

#RATIO TEST
goodMatches = []

for match1,match2 in matches:
    if match1.distance < .75*match2.distance:
        good.append([match1])

#sorting in order of distance 
#smaller distance good match 

sift_matches = cv2.drawMatchesKnn(featureImage,keypoints1,image,keypoints2,matches[:3],None,flags=2)
'''

###########
###FLANN###
###########
#Fast Library For Approx Nearest Neighbour

flann_idx_kdtree=0
idx_params = dict(algorithm=flann_idx_kdtree,trees=5)
search_params=dict(checks=50)

flann = cv2.FlannBasedMatcher(indexParams,search_params)
matches = flann.knnMatch(descriptor1,descriptor2,k=2)

good = []

for match1,match2 in matches:
    if match1.distance < .75*match2.distance:
        good.append([match1])
flann_matches = sift_matches = cv2.drawMatchesKnn(featureImage,keypoints1,image,keypoints2,matches[:3],None,flags=2)

cv2.imshow('matches',sift_matches)
cv2.waitKey(0)
cv2.destroyAllWindows()

