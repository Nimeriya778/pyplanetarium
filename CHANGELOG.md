# Changelog
All notable changes to this project will be documented in this file.

## [0.1.1] - 2021-11-18

### CI configuration

- Build Python package source distribution
- Test install from the Python package source

### Documentation

- Add a usage example to the module docstring

### Features

- Add support for RAW image formats and more
- Add `SpotShape` class constructor variants
- Implement `__str__` and `__repr__` for classes

### Miscellaneous Tasks

- Add `git-cliff` config file

### Testing

- Add spot parameters adjustment unit test

### Build

- Update `planetarium` dependency to v0.1.1

## [0.1.0] - 2021-11-11

### CI configuration

- Add a basic GitLab CI config file
- Build and publish `win_amd64` wheels
- Perform test install on Linux and Windows.

### Testing

- Add some integration tests in Python
- Add canvas image export test case

### Build

- Add python3.dll exported symbol definitions
- Add Windows cross compile environment script

<!-- generated by git-cliff -->