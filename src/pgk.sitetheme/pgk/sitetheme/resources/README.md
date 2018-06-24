#  Documentation

This theme project uses the Gulp task-runner as a build system to compile a production ready distribution.

While the setup builds upon a production ready closed standalone static application it can also generate a Plone deployment build and provide a development environment for Plone integration via Diazo transform engine and integration via *plone.app.theming*.

**Note:** the best way to develop this theme is by using a local proxy server inside a docker container.


## Getting Started

The different gulp tasks are located in dedicated task specific files that can be found inside the themes 'tasks' subdirectory. The tasks are organized for separation of concerns and can all be run individually though in practice you will most of the time stick to the prepared top level tasks documented here that are configured to run corresponding sub tasks in a predefined specific order to provide complete builds ready for deployment.

An overview of all available tasks can be found by running

````bash
gulp --tasks
````

The usual workflow when starting development on a new theme would be:

1. Initialize the build directory and compile all theme assets via `gulp init`
2. Start working on the new theme by executing `gulp serve`

Using the recommended setup including a docker container containing a web server acting as a proxy to a running zope instance running a development environment would look something like this (example):

```bash
$ cd project
$ docker-compose up -f build/docker-compose.yml  # Requires a running traefik setup
$ bin/instance fg  # start plone
$ cd src/project.sitetheme/project/sitetheme/resources
$ gulp build  # build a distribution
$ gulp watch  # automatically compile assets when changes are detected
...
$ gulp dist  # build revisions of assets ready for deployment
```


## Build tasks

### `init` - Initialize a production theme build

Completely erase the `./dist` directory if available and prepare a fresh build by collecting the static resources and assets needed for a successful build like *fonts* or *images*.

```bash
$ gulp init
$ (alias) gulp build:init
```

### `build` - Build production ready distribution

Regenerates the __/dist/__ directory with compiled and minified CSS and JavaScript files and builds the index files via Jekyll task. Includes revved css and js resources for cache busting optimized for page speed and performance.

**Note**: this task should ideally only be run prior to pushing and deploying changes to the production server and is not suitable for development use since it might require extensive processing time. Ideally it is only necessary to run this task once for the initial deployment and the follow up changes can be build through the more dedicated and light weight specific tasks.

```bash
$ gulp build
$ (alias) gulp build:dist:full
```

### `dist`  - Build production ready distribution assets

Builds theme style and script dependencies with cache busting parameters for production deployment

**Note**: this task does not rebuild the whole theme distribution like the corresponding legacy grunt task did, since most of the time we only care for updated styles and javascript resources. Therefore the dist task only adds updated assets with cache busting parameters.

```bash
$ gulp dist
$ (alias) gulp build:dist:base
```

## Development tasks

TODO: document all development tasks like serve, watch etc

### Troubleshooting

Should you encounter problems with installing dependencies or running build commands, first delete the /node_modules/ directory generated by npm and then, rerun npm install.