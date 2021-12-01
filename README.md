# Filter-It <img src="https://cdn-icons-png.flaticon.com/512/5848/5848802.png" width="50">
An Image/Video Filtering Web Application based on OpenCV


## Preview <img src="https://cdn-icons.flaticon.com/png/512/2116/premium/2116837.png?token=exp=1638376196~hmac=1bc46c817e20527c189ac726fa36371a" width="30">

![](https://codimd.s3.shivering-isles.com/demo/uploads/upload_6e3209856bbd2450dbe7e6092f1f223e.gif)


## Packages Used <img src="https://cdn-icons.flaticon.com/png/512/3038/premium/3038089.png?token=exp=1638376160~hmac=360a42fcec6d84c3494396f1740a38a9" width="30">
* OpenCV: opencv_python==4.5.4.58
* Streamlit: streamlit==1.1.0
* Pillow: Pillow==8.4.0
* NumPy: numpy==1.21.3
* libgtk2.0-dev
* FFmpeg: http://www.ffmpeg.org/download.html


## Getting Started <img src="https://cdn-icons-png.flaticon.com/512/495/495530.png" width="30">
Access Filter-It! at the following link: <a 
   href="https://share.streamlit.io/amvarsh/filter-it/main/filter_it.py">
  <img src="https://img.shields.io/badge/Filter--It-Streamlit-red" width=130>

</a>

![](https://codimd.s3.shivering-isles.com/demo/uploads/upload_56a56bb683ae8ac5963fb9cc822be1be.png)

The webapp will open on browser. The user can then upload an image or video of any of the listed file formats.


## Supported File Formats <img src="https://cdn-icons-png.flaticon.com/512/1205/1205526.png" width="30">
* .jpg
* .png
* .jpeg
* .mp4

![](https://codimd.s3.shivering-isles.com/demo/uploads/upload_5bd1556e9f674b109ff45831730b6f84.png)


## Image/Video Filters <img src="https://cdn-icons-png.flaticon.com/512/3204/3204021.png" width="30">
1. **Brightness**: Increase or decrease brightness
2. **Pencil Sketch**: Pencil sketch of image
3. **Negative**: Invert image to create a negative effect
4. **Color Extract**: Extract pixels in image of specified color-range
5. **Color Focus**: Focus on pixels specified color-range by changing others to grayscale 
6. **Cartoon**: Cartoonistic illustration of image

Select any of the filters available from the dropdown meny on side panel.

![](https://codimd.s3.shivering-isles.com/demo/uploads/upload_ab8bee5b3f2069aaaff7386ea750fdea.png)




Depending on the filter selected, the appropriate parameter slidebars will appear.

## Customisable Filter Parameters <img src="https://cdn-icons-png.flaticon.com/512/3132/3132084.png" width="30">

* Brightness
    * Scale
* Pencil Sketch
    * Kernel Size
* Color Extract, Color Focus
    * Hue, Saturation, Values
        * Upper Bound
        * Lower Bound
* Cartoon
    * Kernel Size
    * Area Size

## Output Display <img src="https://cdn-icons-png.flaticon.com/512/916/916054.png" width="30">

Upon clicking <img src="https://img.shields.io/badge/Submit-_-green" width="70"> button and parameters selected, the output will be displayed below the input.

<img src="https://codimd.s3.shivering-isles.com/demo/uploads/upload_54d4ceda4c9ece36dc4dc7546e334655.png" width="770">


## Sample Input and Output <img src="https://cdn-icons.flaticon.com/png/512/2914/premium/2914192.png?token=exp=1638375841~hmac=4dbf0560287ffb6f46020bb19cbbed4e" width="30">
### Brightness Filter
| Input | Output(darkened) | Output(brightened) |
| :---: | :---: | :---: |
|<img src="https://user-images.githubusercontent.com/56351732/143309525-d3c0835a-d24c-4647-80d4-7e25230cde9b.png" width="310">| <img src="https://user-images.githubusercontent.com/56351732/143309564-864bddce-615e-4219-ae84-a4288b80c3b8.png" width="310">| <img src="https://user-images.githubusercontent.com/56351732/143309645-4538a70d-028a-4d71-8be9-096b617a8d3e.png" width="310">|

### Color Pencil Sketch
| Input | Output |
| :---: | :---: |
| ![image](https://user-images.githubusercontent.com/56351732/144130416-3534621b-4a19-4976-b5db-025a7b6083d8.jpeg)| ![image](https://user-images.githubusercontent.com/56351732/144130426-7212f30e-a4ca-4637-b057-2239d2190f1d.jpeg) | 

### Negative
| Input | Output |
| :---: | :---: |
| ![image](https://user-images.githubusercontent.com/70822829/142995051-77c932cb-533d-409c-b2d5-8e049a2cbd95.png)| ![image](https://user-images.githubusercontent.com/70822829/142995109-446ac629-88ad-4d54-9d2e-ceeefea76014.png) | 

### Color Extract
| Input | Output |
| :---: | :---: |
| ![image](https://user-images.githubusercontent.com/56351732/144130912-78b6c606-58d4-4311-8542-0dcb7285287d.jpeg) | ![image](https://user-images.githubusercontent.com/56351732/144130905-7e10b125-4ebd-462b-a02b-bcbd532436fb.jpeg) | 

### Color Focus
| Input | Output |
| :---: | :---: |
| ![image](https://user-images.githubusercontent.com/56351732/144131988-68515282-f80a-413a-9f30-109e8eecba9c.jpeg)| ![image](https://user-images.githubusercontent.com/56351732/144131995-4d7f66d9-add0-40da-ae56-7e74fb775a88.jpeg) |

### Cartoon
| Input | Output |
| :---: | :---: |
| <img src="https://user-images.githubusercontent.com/70822829/144203186-5fa9da01-f594-42bf-8b63-047faa294228.png" width="400">|<img src="https://user-images.githubusercontent.com/70822829/144203222-42b880d0-29f4-4947-b0bc-7dfe6cceb8c3.png" width="400"> |

## Contributors <img src="https://cdn-icons-png.flaticon.com/512/3791/3791146.png" width="30">
<p href="https://github.com/arunimadivya/">
  <img src="https://cdn-icons.flaticon.com/png/512/4140/premium/4140047.png?token=exp=1638372244~hmac=eba20986161a85e71137f22b87e93630" width=40>
    Arunima Divya
</p> 

<p href="https://github.com/amvarsh/">
  <img src="https://cdn-icons.flaticon.com/png/512/4140/premium/4140038.png?token=exp=1638372231~hmac=864f4904c49dcb5826af0e9ccaf1c858" width=40>
    Amrita Varshini E R
</p> 
