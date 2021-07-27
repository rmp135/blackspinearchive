## Internet Archive: Black Spine Edition

For those not familiar, Red Letter Media's [Best of the Worst: Black Spine Edition](https://www.youtube.com/playlist?list=PLJ_TJFLc25JR3VZ7Xe-cmt4k3bMKBZ5Tm) is a segment where they watch completely random VHS tapes. 

Now you can do the same with the Archive.org [VHSVault](https://archive.org/details/vhsvault). 

**NSFW Warning**

Some of the videos are NSFW. 

## Usage

[Click here](https://rmp135.github.io/blackspinearchive/) to visit the GitHub hosted page. Disable any autoplay addons for the full experience.

Videos will continue to play one after the other with a static interlude. You can also use your media keys to skip to the next video.

You can find a link to the details of the currently playing video by moving your cursor to the far top right of the page.

## Running

Just an index.html, nothing special. You'll need a web server as it requests a couple of static files.

## Building

To refresh the list of available videos we need the [Internet Archive CLI](https://archive.org/services/docs/api/internetarchive/cli.html) utility.

```
curl -LOs https://archive.org/download/ia-pex/ia
chmod +x ia
./ia search vhsvault > links.txt
```