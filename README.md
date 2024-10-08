# About

This repository is intended to store the scripts and tools curated and worked on during the 2024 Land Working Group Workshop. Depending on the outcomes from the workshop, this repository may be either continued or used as a template for the end goal: A repository for storing the many scripts and auxiliary tools used by the land community within Australia as part of their research. This includes processes such as re-gridding, aggregation and disaggregation, statistical analyses and reductions, resampling, as well as tools to prepare datasets for ingestion by either CABLE or JULES.

# Why

Many groups within the land community are using similar workflows and have similar requirements. By collecting and cataloguing the tools created by the community in one place, we achieve the following objectives:

* Reduce duplicated work by reusing existing functionality
* Ensure comparability between scientific runs made by different groups by using unified methods of interpolation, aggregation etc.
* Results are reproducible, as we have a history of any changes made to the tools

# What to do

Place your script or tool in the relevant directory within the repository and include a README. The README should be named according to the name of your script e.g. if your script is called ```interpolate_met_data.py```, then your README should be named ```interpolate_met_data_README.txt```.

## Contents of the README

The README should have three headings: __Purpose__, __Usage__, __Method__. Please be verbose in the descriptions. For example:

### Purpose
BAD: Interpolates met data
GOOD: Interpolates the CRU-JRA met data to the desired resolution and writes the output to NetCDF in a format readable by CABLE.

### Usage
BAD: interpolate_met_data.py -r lat_resolution,lon_resolution -o output.nc -b lat_min,lat_max,lon_min,lon_max
GOOD: Call from the command line via ```interpolate_met_data.py -r lat_resolution,lon_resolution -o output.nc -b lat_min,lat_max,lon_min,lon_max```, where:
* "-r lat_resolution,lon_resolution" are the grid spacings (required).
* "-o output.nc" specifies the name of the output file to write to (required).
* "-b lat_min,lat_max,lon_min,lon_max" specify the domain to interpolate (optional). If no bounds are specified, then the original domain is used.

### Method
BAD: uses linear interpolation
GOOD: Reads the dataset using [xarray](https://docs.xarray.dev/en/stable/) and uses scipy's [LinearNDInterpolator](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.LinearNDInterpolator.html#scipy.interpolate.LinearNDInterpolator) to perform the interpolation.

## Repository Structure

The current plan is to distinguish tools at the highest level by the land models that they target i.e. CABLE or JULES. Further structure is up for discussion- do we then separate by pre- and post-processing? Interpolation and aggregation/disaggregation?

![Repository Structure](LWG-Workshop-Day2-RepoStructure.png)
