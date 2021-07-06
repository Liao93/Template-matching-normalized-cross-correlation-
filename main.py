import cv2
import numpy as np
import random

def template_match(template, img):
	img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.float32)
	template_g = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY).astype(np.float32)
	H_i, W_i = img_g.shape
	H_t, W_t = template_g.shape
	corr_map = np.zeros((H_i, W_i))
	# Templete matching
	mean_t = np.mean(template_g)
	x_max, y_max = -1, -1
	v = -1
	for y in range(H_i - H_t):
		for x in range(W_i - W_t):
			# compute normalized cross-correlation
			mean_patch = np.mean(img_g[y:y+H_t, x:x+W_t])
			_v = np.sum((img_g[y:y+H_t, x:x+W_t]-mean_patch) * (template_g-mean_t))
			_v /= (np.sqrt(np.sum((img_g[y:y+H_t, x:x+W_t]-mean_patch)**2)) * np.sqrt(np.sum((template_g-mean_t)**2)))
			corr_map[y, x] = _v
			if _v > v:
				v = _v
				x_max, y_max = x, y
	return (corr_map, x_max, y_max)

img = cv2.imread("buildings.jpg").astype(np.float32)
template = img[193:294, 95:153]
cv2.imwrite("template.jpg", template)
H_t, W_t = template.shape[0], template.shape[1]

(corr_map, x_max, y_max) = template_match(template, img)
#Normalize Cross-correlation map to 0~255
corr_map = 255.0 * (corr_map - np.amin(corr_map)) / (np.amax(corr_map) - np.amin(corr_map))
cv2.imwrite("Cross-correlation map.jpg", corr_map.astype(np.uint8))

#Mark template in image
out = img.copy()
cv2.rectangle(out, pt1=(x_max, y_max), pt2=(x_max+W_t, y_max+H_t), color=(0,0,255), thickness=2)
cv2.imwrite("Template matching.jpg", out.astype(np.uint8))

cv2.imshow("Image",img.astype(np.uint8))
cv2.imshow("Template", template.astype(np.uint8))
cv2.imshow("Template matching", out.astype(np.uint8))
cv2.imshow("Cross-correlation map", corr_map.astype(np.uint8))
cv2.waitKey(0)