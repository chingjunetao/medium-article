import requests

for i in range(1,10):
    print(i)
    image_name_dir = 'images/' + str(i) + '.png'
    f = open(image_name_dir,'wb')
    request_url = 'https://static-nft.pancakeswap.com/mainnet/0x0a8901b0E25DEb55A87524f0cC164E9644020EBA/pancake-squad-' + str(i) + '-1000.png'

    r = requests.get(request_url)
    if r.status_code == 200: 
        f.write(requests.get(request_url).content)
        f.close()

        print(image_name_dir + ' is successfully downloaded.')

    else: 
        print('Error. Image cannot be retrieved.')

