# <img src="https://cdn-icons-png.flaticon.com/512/5848/5848802.png" width="50"> Filter-It 
An Image/Video Filtering Web Application based on OpenCV


## <img src="https://cdn-icons.flaticon.com/png/512/2116/premium/2116837.png?token=exp=1638376196~hmac=1bc46c817e20527c189ac726fa36371a" width="30"> Preview 

![final](https://user-images.githubusercontent.com/56351732/144272641-b50d475e-d368-4ff1-a3ed-178f0515fdf1.gif)


## <img src="https://cdn-icons.flaticon.com/png/512/3038/premium/3038089.png?token=exp=1638376160~hmac=360a42fcec6d84c3494396f1740a38a9" width="30"> Packages Used 
* OpenCV: opencv_python==4.5.4.58
* Streamlit: streamlit==1.1.0
* Pillow: Pillow==8.4.0
* NumPy: numpy==1.21.3
* libgtk2.0-dev
* FFmpeg: http://www.ffmpeg.org/download.html


## <img src="https://cdn-icons-png.flaticon.com/512/495/495530.png" width="30"> Getting Started 
Access Filter-It! at the following link: <a 
   href="https://share.streamlit.io/amvarsh/filter-it/main/filter_it.py">
  <img src="https://img.shields.io/badge/Filter--It-Streamlit-red" width=130>

</a>

![image](https://user-images.githubusercontent.com/56351732/144272956-bb0e9c7a-576f-4a38-b4c7-c1bfe3d7ef97.png)

The webapp will open on browser. The user can then upload an image or video of any of the listed file formats.


## <img src="https://cdn-icons-png.flaticon.com/512/1205/1205526.png" width="30"> Supported File Formats 
* .jpg
* .png
* .jpeg
* .mp4

![upload_e85dc01429c536bda3822daed0dd543c](https://user-images.githubusercontent.com/56351732/144273114-9e9b5d80-51c0-4b40-9765-07f13ce8dc53.png)

## <img src="https://cdn-icons-png.flaticon.com/512/3204/3204021.png" width="30"> Image/Video Filters 
1. **Brightness**: Increase or decrease brightness
2. **Pencil Sketch**: Pencil sketch of image
3. **Negative**: Invert image to create a negative effect
4. **Color Extract**: Extract pixels in image of specified color-range
5. **Color Focus**: Focus on pixels specified color-range by changing others to grayscale 
6. **Cartoon**: Cartoonistic illustration of image

Select any of the filters available from the dropdown meny on side panel.

![Screenshot 2021-12-01 211722](https://user-images.githubusercontent.com/56351732/144273146-dd66a576-76c1-4f22-a9d4-28f1bf03b4be.png)


Depending on the filter selected, the appropriate parameter slidebars will appear.

## <img src="https://cdn-icons-png.flaticon.com/512/3132/3132084.png" width="30"> Customisable Filter Parameters 

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

## <img src="https://cdn-icons-png.flaticon.com/512/916/916054.png" width="30"> Output Display 

Upon clicking <img src="https://img.shields.io/badge/Submit-_-green" width="70"> button and parameters selected, the output will be displayed below the input.

![Screenshot 2021-12-01 212820](https://user-images.githubusercontent.com/56351732/144273242-fa485c4c-a5d5-4243-8442-e544e16419be.png)


## <img src="https://cdn-icons.flaticon.com/png/512/2914/premium/2914192.png?token=exp=1638375841~hmac=4dbf0560287ffb6f46020bb19cbbed4e" width="30"> Sample Input and Output 
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

## <img src="https://cdn-icons-png.flaticon.com/512/3791/3791146.png" width="30"> Contributors 

<img src="https://user-images.githubusercontent.com/56351732/144274356-b4e1bcfc-3010-4fd0-8393-af090a461270.png" width=40> [**Arunima Divya**](https://github.com/arunimadivya/)

<img src="https://user-images.githubusercontent.com/56351732/144274340-4a1f243f-ea68-4636-b660-01cb377821d9.png" width=40> [**Amrita Varshini E R**](https://github.com/amvarsh/)

