# Xcode Runner

![telegram-cloud-photo-size-2-5395861517154501244-m](https://user-images.githubusercontent.com/69932531/198831583-ddee994a-87b9-408c-91d5-3321fe0769f8.jpg)

If situation above is known to you this script will help.

## How to get started

1. Clone this repo to your device;
2. `chmod +x setup.sh`
3. `sudo ./setup.sh`
4. `xrun help`

> If `setup.sh` script fails if the error like `cp: /usr/local/bin/xrun : No such file or directory`, you should give **Full disc access** rights to your terminal in the privacy setting.

### Pro tip

Pass path to the `xcodeproj` or to `xcworkspace` file and your project will be opened:

```bash
$ xrun 14.2.0 ./
```
