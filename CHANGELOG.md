# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/). This project attempts to match the major and minor versions of [stactools](https://github.com/stac-utils/stactools) and increments the patch number as needed.

## [Unreleased]

## Changed

- Item `platform` value from `TanDEM-X` to `tandem-x` ([#15](https://github.com/stactools-packages/cop-dem/pull/15))

## Fixed

- Fixed license link to a valid URL ([#17](https://github.com/stactools-packages/cop-dem/pull/17))
- Item now propertly advertises use of the Raster Extension via stac_extensions ([#18](https://github.com/stactools-packages/cop-dem/pull/18))

## [0.1.1] - 2023-01-30

### Added

- Package description ([#10](https://github.com/stactools-packages/cop-dem/pull/10))

## [0.1.0] - 2023-01-30

### Added

- create-collection and matching tests for both glo-30 and glo-90
- New: `--host` option to specify a Provider HOST from a list of options in constants. `AWS` and `OT` are the current valid options.
- added python 3.10

### Removed

- remove python 3.7 support

[Unreleased]: https://github.com/stactools-packages/cop-dem/compare/v0.1.1..main
[0.1.1]: https://github.com/stactools-packages/cop-dem/compare/v0.1.0..v0.1.1
[0.1.0]: https://github.com/stactools-packages/cop-dem/tags/v0.1.0
