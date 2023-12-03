# Efficient QR Code Generator with UTM

This Project is to make a QR Code Generator which support to make a bundle of QR Code with UTM Parameters

## How to use

before you run this program, you need to install some packages

```bash
    pip install -r requirements.txt
```

and write some utm parameters in a file like below:


```bash
    campaign1,source1,medium1,term1,content1
    campaign2,source2,medium2,term2,content2
    campaign3,source3,medium3,term3,content3
    campaign4,source4,medium4,term4,content4
    campaign5,source5,medium5,term5,content5
```
if you leave it blank, the program will automatically skip it.

(but you need to fill the ***campaign name*** at least)

finally, you are able to run this program

```bash
    python main.py [base_url] [file_path] [folder_path]
```
it will generate a QR Code with utm parameters and save it as a file in a folder

## How it works

1. Read a file which contains a list of utm parameters (sep:,)
2. Generate a QR Code with the utm parameters (e.g base_url + ?utm_campaign=... &utm_source=...&utm_medium=...)
2-1. if some param is empty, skip it
3. Save the QR Code as a file in a folder