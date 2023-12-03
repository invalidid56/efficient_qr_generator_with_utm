import shutil
import sys
import os
import qrcode


def make_url(base_url: str, params: list):
    res = base_url
    res += '?utm_campaign=' + params[0] if params[0] else 'default'
    res += ('&utm_medium=' + params[1]) if params[1] else ''
    res += ('&utm_source=' + params[2]) if params[2] else ''
    return res


def main(file_path, folder_path, base_url):
    """
    main function
    :param file_path: file path to read utm parameters
    :param folder_path: folder path to save QR Code
    :return: None
    """
    # read a file
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # make a folder
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    else:
        shutil.rmtree(folder_path)
        os.makedirs(folder_path)

    # generate QR Code
    for line in lines:
        params = line.strip().split(',')
        if len(params) < 3:
            params += ['' for _ in range(3 - len(params))]

        url = make_url(base_url, params)
        if url is None:
            continue
        img = qrcode.make(url)

        # save QR Code
        if (params[0] + '.png') in os.listdir(folder_path):
            print("Warning: duplicated file name")
        img.save(os.path.join(folder_path, params[0] + '.png'))


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage: python main.py [base_url] [file_path] [folder_path]')
        sys.exit(1)

    main(base_url=sys.argv[1], file_path=sys.argv[2], folder_path=sys.argv[3])
