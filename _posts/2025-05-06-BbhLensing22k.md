---
---

# Happy Black Hole Week!

<div id="openseadragon1" style="width: 800px; height: 600px;"></div>
<script src="{{ site.baseurl }}/js/openseadragon.min.js"></script>
<script type="text/javascript">
    var viewer = OpenSeadragon({
        id: "openseadragon1",
        prefixUrl: "{{ site.baseurl }}/images/openseadragon/images/",
        tileSources: "{{ site.baseurl }}/images/lensing/BbhLensing22k.dzi"
    });
</script>
