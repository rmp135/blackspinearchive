## Internet Archive: Black Spine Edition

For those not familiar, Red Letter Media's [Best of the Worst: Black Spine Edition](https://www.youtube.com/playlist?list=PLJ_TJFLc25JR3VZ7Xe-cmt4k3bMKBZ5Tm) is a segment where they watch completely random VHS tapes. 

Now you can do the same with the Archive.org [VHSVault](https://archive.org/details/vhsvault). Refresh the page and see what random VHS video you land on!

**NSFW Warning**

Some of the videos are NSFW. 

## Usage

Click here to visit the GitHub hosted page.

## Running

Just an index.html, nothing special. You'll need some sort of host as it requests the links.txt file.

## Building

To refresh the list of available videos we need the internet archive CLI utility.

```
curl -LOs https://archive.org/download/ia-pex/ia
chmod +x ia
./ia search vhsvault > links.txt
```

Then filter out everything but the name. 

```
sed -i "" -E 's/{"identifier": "(.*)"}/\1/' links.txt
```