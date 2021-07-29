# stactools-cop-dem

- Name: cop-dem
- Package: `stactools.cop_dem`
- PyPI: https://pypi.org/project/stactools-cop-dem/
- Owner: @justinfisk
- Dataset homepages:
  - https://copernicus-dem-30m.s3.amazonaws.com/readme.html
  - https://portal.opentopography.org/datasetMetadata?otCollectionID=OT.032021.4326.1
- STAC extensions used:
  - [proj](https://github.com/stac-extensions/projection/)
- Extra fields: none

The Copernicus DEM is a Digital Surface Model (DSM) which represents the surface of the Earth including buildings, infrastructure and vegetation. We provide two instances of Copernicus DEM named GLO-30 Public and GLO-90. GLO-90 provides worldwide coverage at 90 meters. GLO-30 Public provides limited worldwide coverage at 30 meters because a small subset of tiles covering specific countries are not yet released to the public by the Copernicus Programme. Note that in both cases ocean areas do not have tiles, there one can assume height values equal to zero. Data is provided as Cloud Optimized GeoTIFFs.

(from https://copernicus-dem-30m.s3.amazonaws.com/readme.html )

## Examples

### STAC objects

- [Item](examples/Copernicus_DSM_COG_30_N53_00_W115_00_DEM.json)

### Command-line usage

Description of the command line functions

```bash
$ stac cop-dem create-item Copernicus_DSM_COG_30_N53_00_W115_00_DEM.tif Copernicus_DSM_COG_30_N53_00_W115_00_DEM.json
```

Use `stac cop-dem --help` to see all subcommands and options.
