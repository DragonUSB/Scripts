import cv2
import mediapipe as mp

mp_selfie_segmentation = mp.solutions.selfie_segmentation

with mp_selfie_segmentation.SelfieSegmentation(
     model_selection=1) as selfie_segmentation:

     image = cv2.imread('Scripts\Python Scripts\MediaPipe\Image_0001.jpg')
     image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
     results = selfie_segmentation.process(image_rgb)

     cv2.imshow("Image", image)
     cv2.imshow("Mask", results.segmentation_mask)
     cv2.waitKey(0)
cv2.destroyAllWindows()