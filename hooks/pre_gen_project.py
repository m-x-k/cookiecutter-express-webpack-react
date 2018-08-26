import json
from subprocess import call

def update_package_js():
    package = {}
    with open('./package.json', 'r') as f:
        package = json.load(f)

    with open('./package.json', 'w') as f:
        scripts = {
            'build': 'webpack --mode production --config webpack.config.js',
            'start': 'node bin/www'
        }
        package['scripts'].update(scripts)
        json.dump(package, f, indent=4)

def create_babelrc():
    with open('.babelrc', 'w') as f:
        presets = {
            'presets': ['env', 'react', 'stage-2']
        }
        json.dump(presets, f, indent=4)

def webpack_config():
    data = """
var path = require('path');
var webpack = require('webpack');
module.exports = {
    node: {
        fs: "empty",
        net: "empty"
    },
    entry: './src/client/app.jsx',
    output: {
        path: path.resolve(__dirname, './public'),
        publicPath: '/',
        filename: 'bundle.js'
    },
    resolve: {
        extensions: ['*', '.js', '.jsx']
    },    
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                loader: 'babel-loader'
            }
        ]
    },
    stats: {
        colors: true
    },
    devServer: {
        contentBase: './dist'
    }
};
     """
    with open('webpack.config.js', 'w') as f:
        f.write(data)

def install_requirements():
    call(['npm','init', '-y'])
    call(['npm', 'install', 'express', 'http-errors', 'path', 'cookie-parser', 'morgan', 'js-beautify', 'ejs', 'debug'])
    call(['npm', 'install', '--save-dev', 'webpack', 'webpack-cli', 'webpack-dev-server'])
    call(['npm', 'install', '--save-dev', 'babel-loader', 'babel-core', 'babel-preset-env', 'babel-preset-react', 'babel-preset-stage-2'])
    call(['npm', 'install', '--save', 'react', 'react-dom'])
    update_package_js()
    create_babelrc()
    webpack_config()

install_requirements()
print('http://localhost:3000')
