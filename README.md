# rainbowup
This is a script created by Mt. Front to bulk apply rainbow filter to images.

On 7/7/2021, Chinese government banned all Wechat (largest Chinese social network) channels related to LGBT rights. 
This script is just a silent protest.

Find the source code at https://github.com/mfcndw/rainbowup

***Warning: This script has only been tested on MacOS***

## Example
| Original      | Rainbowed | Smooth |
| ----------- | ----------- | ----------- |
| <img width="300" alt="test_profile" src="https://user-images.githubusercontent.com/5817602/124720941-84046d80-debd-11eb-9c74-d61eaffef99f.png">|<img width="300" alt="test_profile_rainbowed" src="https://user-images.githubusercontent.com/5817602/124720953-86ff5e00-debd-11eb-8ba0-ae2effaa281c.png">|<img width="300" alt="test_profile" src="https://user-images.githubusercontent.com/5817602/124829818-f9a82200-df2d-11eb-8eaa-5164aca65d1b.png">|



## Usage:
`python3 rainbowup.py path [-a] [-s] [-f] [-h]`

### required arguments:
 * path: The path of image or directory needs to be rainbowed up

### optional arguments:
 * -h, --help: show this help message and exit
 * -a, --alpha: The opacity of the filter, default to 130. range from 0 (not visible) - 255
 * -s, --smooth: Switch to a smooth rainbow filter. Default to false
 * -f, --filter: Path to custom filter image