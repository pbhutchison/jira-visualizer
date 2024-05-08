# jira-visualizer

Nicegui web tool that uses Jira REST API data to create GANTT charts.

## Dependencies

This project runs in Python 3.8 with the following dependencies:
* nicegui

If on a linux machine, I recomend running the code within the supplied conda environment. To run the code in the conda environment in a terminal run `conda env create -f environment.yaml` to create the environment, `conda activate gui` to start the environment, and `conda deactivate gui` to deactivate the environment when you are done using it.

## Usage

> TODO (Hutchison): Update this later so that it is descriptive

## Testing

> TODO (Hutchison): Set up once we actually have a test suite

## Packaging and deployment

> TODO (Hutchison): Update this section once we actually have the 

## Contributing

This repository follows the [https://google.github.io/styleguide/pyguide.html](Python Google Style Guide).

To lint the code, run the following from the root of the directory: `pylint --rcfile pylintrc ./src/jirawg`.

