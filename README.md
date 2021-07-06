# Template matching (normalized cross-correlation)

## Environment
- Python 3.7.1
- numpy 1.19.2
- opencv 3.4.1

## Description

1. Template matching using normalized cross-correlation.
2. Before template matching, add noise to the image.

## Zero mean normalized cross-correlation
- Formula: 
![formula](https://www.programmersought.com/imgrdrct/https://img-blog.csdnimg.cn/20190315151115295.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MTE2MTUw,size_16,color_FFFFFF,t_70)

## Demo
- The image
![img](./img/buildings.jpg)
- The template
![temp](./img/template.jpg)
- The result of template matching
![out](./img/Template%20matching.jpg)
- The cross-correlation map
![map](./img/Cross-correlation%20map.jpg)
- - -
- The image with noise
![img_noise](img/Image(noise).jpg)
- The result of template matching using the image with noise
![out_noise](./img/Template%20matching(noise).jpg)
- The cross-correlation map
![map_noise](./img/Cross-correlation%20map(noise).jpg)
