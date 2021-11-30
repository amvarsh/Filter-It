# Filter-It
An Image/Video Filtering Web Application based on OpenCV

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
| Input | Ouput (Extracts out green) |
| :---: | :---: |
| ![image](https://user-images.githubusercontent.com/70822829/142995579-ebc6bcba-8c18-40d6-85c6-2871c2f78fc4.png)| ![image](https://user-images.githubusercontent.com/70822829/142995611-4de8d4e0-0a71-47c7-83a5-0782d0df175d.png) | 

### Color Focus
| Input | Ouput (Focuses green) |
| :---: | :---: |
| ![image](https://user-images.githubusercontent.com/70822829/143008068-fb185799-7a5c-4941-9a98-b0936cfb07b3.png)| ![image](https://user-images.githubusercontent.com/70822829/143008104-c3585d73-7a93-4154-bc7f-2c12372e9315.png) |

