# Filter-It
An Image/Video Filtering Web Application based on OpenCV

# Preview
![](https://user-images.githubusercontent.com/56351732/144137832-a0116238-cfd3-4e8c-9d73-0f0d6c648104.gif)

## How to run the application from a local host:
```
git clone https://github.com/amvarsh/Filter-It.git
pip install -r requirements.txt
streamlit run filter_it.py
```
<img src="https://user-images.githubusercontent.com/70822829/142992870-1111f86b-b48c-4bdb-b2ed-910eec4c7699.jpg" width="770">

The webapp will open on browser. The user can then upload an image or video. Accepted file types are listed.

<img src="https://user-images.githubusercontent.com/70822829/142992332-fe09391d-b1d6-452a-8730-5e62ebd28e62.png" width="770">

The user can then select from the list of filters, and depending on the filter selected, the appropriate parameter slidebars will appear. 

<img src="https://user-images.githubusercontent.com/70822829/143723562-67a59158-5e6e-4c99-a3f3-c4fac7354718.png" width="770">

For example, if brightness filter is selected, there will be one slidebar to select brightness factor, or if color extract is selected, 6 slidebars will appear for picking the lower and upper bound values of the color to be extracted. 

<img src="https://user-images.githubusercontent.com/70822829/143723574-20c2e827-4d52-4808-a75f-211d4fd3ad8d.png" width="350">


Upon submitting the filter and parameters selected, the output will be displayed below the input.

<img src="https://user-images.githubusercontent.com/70822829/143723472-03a15b37-5d29-4b48-9421-9c2bb53b7f2c.png" width="770">


## Sample Input and Output
### Brightness Filter
| Input | Ouput(darkened) | Output(brightened) |
| :---: | :---: | :---: |
|<img src="https://user-images.githubusercontent.com/56351732/143309525-d3c0835a-d24c-4647-80d4-7e25230cde9b.png" width="310">| <img src="https://user-images.githubusercontent.com/56351732/143309564-864bddce-615e-4219-ae84-a4288b80c3b8.png" width="310">| <img src="https://user-images.githubusercontent.com/56351732/143309645-4538a70d-028a-4d71-8be9-096b617a8d3e.png" width="310">|

### Color Pencil Sketch
| Input | Ouput |
| :---: | :---: |
| ![image](https://user-images.githubusercontent.com/56351732/144130416-3534621b-4a19-4976-b5db-025a7b6083d8.jpeg)| ![image](https://user-images.githubusercontent.com/56351732/144130426-7212f30e-a4ca-4637-b057-2239d2190f1d.jpeg) | 

### Negative
| Input | Ouput |
| :---: | :---: |
| ![image](https://user-images.githubusercontent.com/70822829/142995051-77c932cb-533d-409c-b2d5-8e049a2cbd95.png)| ![image](https://user-images.githubusercontent.com/70822829/142995109-446ac629-88ad-4d54-9d2e-ceeefea76014.png) | 

### Color Extract
| Input | Ouput |
| :---: | :---: |
| ![image](https://user-images.githubusercontent.com/56351732/144130912-78b6c606-58d4-4311-8542-0dcb7285287d.jpeg) | ![image](https://user-images.githubusercontent.com/56351732/144130905-7e10b125-4ebd-462b-a02b-bcbd532436fb.jpeg) | 

### Color Focus
| Input | Ouput |
| :---: | :---: |
| ![image](https://user-images.githubusercontent.com/56351732/144131988-68515282-f80a-413a-9f30-109e8eecba9c.jpeg)| ![image](https://user-images.githubusercontent.com/56351732/144131995-4d7f66d9-add0-40da-ae56-7e74fb775a88.jpeg) |

### Cartoon
| Input | Ouput |
| :---: | :---: |
| <img src="https://user-images.githubusercontent.com/70822829/144203186-5fa9da01-f594-42bf-8b63-047faa294228.png" width="400">|<img src="https://user-images.githubusercontent.com/70822829/144203222-42b880d0-29f4-4947-b0bc-7dfe6cceb8c3.png" width="400"> |

